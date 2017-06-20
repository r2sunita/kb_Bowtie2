from pprint import pprint

import os
import time

from kb_Bowtie2.util.Bowtie2Runner import Bowtie2Runner
from kb_Bowtie2.util.Bowtie2IndexBuilder import Bowtie2IndexBuilder

from ReadsUtils.ReadsUtilsClient import ReadsUtils
from ReadsAlignmentUtils.ReadsAlignmentUtilsClient import ReadsAlignmentUtils
from KBaseReport.KBaseReportClient import KBaseReport

from Workspace.WorkspaceClient import Workspace
from SetAPI.SetAPIServiceClient import SetAPI

from KBParallel.KBParallelClient import KBParallel


class Bowtie2Aligner(object):

    def __init__(self, scratch_dir, workspace_url, callback_url, srv_wiz_url, provenance):
        self.scratch_dir = scratch_dir
        self.workspace_url = workspace_url
        self.callback_url = callback_url
        self.srv_wiz_url = srv_wiz_url
        self.provenance = provenance

        self.ws = Workspace(self.workspace_url)
        self.bowtie2 = Bowtie2Runner(self.scratch_dir)
        self.parallel_runner = KBParallel(self.callback_url)


    def align(self, params):
        validated_params = self.validate_params(params)
        input_info = self.determine_input_info(validated_params)
        # input info provides information on the input and tells us if we should
        # run as a single_library or as a set:
        #     input_info = {'run_mode': '', 'info': [..], 'ref': '55/1/2'}

        assembly_or_genome_ref = validated_params['assembly_or_genome_ref']

        if input_info['run_mode'] == 'single_library':
            single_lib_result = self.single_reads_lib_run(input_info, assembly_or_genome_ref,
                                                          validated_params, create_report=True)
            return single_lib_result['report_info']


        if input_info['run_mode'] == 'sample_set':
            reads_refs = self.fetch_reads_refs_from_sampleset(input_info['ref'], input_info['info'])
            bowtie2_index_info = self.build_bowtie2_index(assembly_or_genome_ref, validated_params['output_workspace'])
            single_lib_result_list = {}
            print('Running on set of reads=')
            pprint(reads_refs)

            tasks = []

            for k in range(0, len(reads_refs)):
                tasks.append(self.build_single_execution_task(k, reads_refs[k]['ref'], params))
                # reads_info = self.get_obj_info(readlib['ref'])
                # single_input_info = {'info': reads_info, 'ref': readlib['ref'], 'condition': readlib['condition'],
                #                     'bowtie2_index_info': bowtie2_index_info}
                # single_lib_result = self.single_reads_lib_run(single_input_info, assembly_or_genome_ref,
                #                                              validated_params, create_report=False)
                # single_lib_result_list[readlib['ref']] = single_lib_result



            batch_run_params = {'tasks': tasks, 'runner': 'local_parallel', 'concurrent_local_tasks': 2}
            results = self.parallel_runner.run_batch(batch_run_params)
            pprint(results)


            batch_result = self.process_batch_result(single_lib_result_list)
            return batch_result['report_info']

        raise ('Improper run mode')


    def build_single_execution_task(self, n, reads_lib_ref, params):
        task_params = params
        task_params['input_ref'] = reads_lib_ref
        task_params['output_name'] = params['output_name'] + '.' + str(n)

        return {'module_name': 'kb_Bowtie2',
                'function_name': 'align_reads_to_assembly_app',
                'version': 'dev',
                'parameters': task_params}



    def single_reads_lib_run(self, read_lib_info, assembly_or_genome_ref, validated_params,
                             create_report=False, bowtie2_index_info=None):
        ''' run on one reads '''

        # download reads and prepare any bowtie2 index files
        input_configuration = self.prepare_single_run(read_lib_info, assembly_or_genome_ref,
                                                      bowtie2_index_info, validated_params['output_workspace'])
        pprint(input_configuration)

        # run the actual program
        run_output_info = self.run_bowtie2_align_cli(input_configuration, validated_params)

        # process the result and save the output
        upload_results = self.save_read_alignment_output(run_output_info, input_configuration, validated_params)
        run_output_info['upload_results'] = upload_results

        report_info = None
        if create_report:
            report_info = self.create_report(run_output_info, input_configuration, validated_params)

        self.clean(run_output_info)

        return {'output_info': run_output_info, 'report_info': report_info}


    def build_bowtie2_index(self, assembly_or_genome_ref, ws_for_cache):
        bowtie2IndexBuilder = Bowtie2IndexBuilder(self.scratch_dir, self.workspace_url,
                                                  self.callback_url, self.srv_wiz_url,
                                                  self.provenance)

        return bowtie2IndexBuilder.get_index({'ref': assembly_or_genome_ref,
                                              'ws_for_cache': ws_for_cache})


    def prepare_single_run(self, input_info, assembly_or_genome_ref,
                           bowtie2_index_info, ws_for_cache):
        ''' Given a reads ref and an assembly, setup the bowtie2 index '''
        # first setup the bowtie2 index of the assembly
        input_configuration = {'bowtie2_index_info': bowtie2_index_info}
        if not bowtie2_index_info:
            bowtie2IndexBuilder = Bowtie2IndexBuilder(self.scratch_dir, self.workspace_url,
                                                      self.callback_url, self.srv_wiz_url,
                                                      self.provenance)

            index_result = bowtie2IndexBuilder.get_index({'ref': assembly_or_genome_ref,
                                                          'ws_for_cache': ws_for_cache})
            input_configuration['bowtie2_index_info'] = index_result

        # next download the reads
        read_lib_ref = input_info['ref']
        read_lib_info = input_info['info']
        reads_params = {'read_libraries': [read_lib_ref],
                        'interleaved': 'false',
                        'gzipped': None}
        ru = ReadsUtils(self.callback_url)
        reads = ru.download_reads(reads_params)['files']

        input_configuration['reads_lib_type'] = self.get_type_from_obj_info(read_lib_info).split('.')[1]
        input_configuration['reads_files'] = reads[read_lib_ref]
        input_configuration['reads_lib_ref'] = read_lib_ref

        return input_configuration


    def run_bowtie2_align_cli(self, input_configuration, validated_params):

        pprint('======== input_configuration =====')
        pprint(input_configuration)
        options = []
        run_output_info = {}

        # set the bowtie2 index location
        bt2_index_dir = input_configuration['bowtie2_index_info']['output_dir']
        bt2_index_basename = input_configuration['bowtie2_index_info']['index_files_basename']
        options.extend(['-x', bt2_index_basename])

        # set the input reads
        if input_configuration['reads_lib_type'] == 'SingleEndLibrary':
            options.extend(['-U', input_configuration['reads_files']['files']['fwd']])
            run_output_info['library_type'] = 'single_end'
        elif input_configuration['reads_lib_type'] == 'PairedEndLibrary':
            options.extend(['-1', input_configuration['reads_files']['files']['fwd']])
            options.extend(['-2', input_configuration['reads_files']['files']['rev']])
            run_output_info['library_type'] = 'paired_end'

        # setup the output file name
        output_dir = os.path.join(self.scratch_dir, 'bowtie2_alignment_output_' + str(int(time.time() * 10000)))
        output_sam_file = os.path.join(output_dir, 'reads_alignment.sam')
        os.makedirs(output_dir)
        options.extend(['-S', output_sam_file])
        run_output_info['output_sam_file'] = output_sam_file
        run_output_info['output_dir'] = output_dir

        # parse all the other parameters
        if 'quality_score' in validated_params:
            options.append('--' + str(validated_params['quality_score']))

        if 'alignment_type' in validated_params:
            options.append('--' + str(validated_params['alignment_type']))

        if 'preset_options' in validated_params:
            if 'alignment_type' in validated_params and validated_params['alignment_type'] == 'local':
                options.append('--' + str(validated_params['preset_options'] + '-local'))
            else:
                options.append('--' + str(validated_params['preset_options']))

        if 'trim5' in validated_params:
            options.extend(['--trim5', str(validated_params['trim5'])])
        if 'trim3' in validated_params:
            options.extend(['--trim3', str(validated_params['trim3'])])
        if 'np' in validated_params:
            options.extend(['--np', str(validated_params['np'])])

        if 'minins' in validated_params:
            options.extend(['--minins', str(validated_params['minins'])])
        if 'maxins' in validated_params:
            options.extend(['--maxins', str(validated_params['maxins'])])

        # unfortunately, bowtie2 expects the index files to be in the current directory, and
        # you cannot configure it otherwise.  So run bowtie out of the index directory, but
        # place the output SAM file somewhere else
        self.bowtie2.run('bowtie2', options, cwd=bt2_index_dir)

        return run_output_info


    def save_read_alignment_output(self, run_output_info, input_configuration, validated_params):
        rau = ReadsAlignmentUtils(self.callback_url)
        destination_ref = validated_params['output_workspace'] + '/' + validated_params['output_name']
        upload_params = {'file_path': run_output_info['output_sam_file'],
                         'destination_ref': destination_ref,
                         'read_library_ref': input_configuration['reads_lib_ref'],
                         'assembly_or_genome_ref': validated_params['assembly_or_genome_ref'],
                         'condition': 'unknown'}
        upload_results = rau.upload_alignment(upload_params)
        return upload_results


    def clean(self, run_output_info):
        ''' Not really necessary on a single run, but if we are running multiple local subjobs, we
        should clean up files that have already been saved back up to kbase '''
        pass

    def create_report(self, run_output_info, input_configuration, validate_params):
        report_info = {}
        report_text = ''
        kbreport = KBaseReport(self.callback_url)

        return {}

    def process_batch_result(self):
        pass


    def validate_params(self, params):
        validated_params = {}

        required_string_fields = ['input_ref', 'assembly_or_genome_ref', 'output_name', 'output_workspace']
        for field in required_string_fields:
            if field in params and params[field]:
                validated_params[field] = params[field]
            else:
                raise ValueError('"' + field + '" field required to run bowtie2 aligner app')

        optional_fields = ['quality_score', 'alignment_type', 'preset_options', 'trim5', 'trim3',
                           'np', 'minins', 'maxins']
        for field in optional_fields:
            if field in params:
                if params[field] is not None:
                    validated_params[field] = params[field]

        return validated_params


    def fetch_reads_refs_from_sampleset(self, ref, info):
        """
        Note: adapted from kbaseapps/kb_hisat2 - file_util.py

        From the given object ref, return a list of all reads objects that are a part of that
        object. E.g., if ref is a ReadsSet, return a list of all PairedEndLibrary or SingleEndLibrary
        refs that are a member of that ReadsSet. This is returned as a list of dictionaries as follows:
        {
            "ref": reads object reference,
            "condition": condition string associated with that reads object
        }
        The only one required is "ref", all other keys may or may not be present, based on the reads
        object or object type in initial ref variable. E.g. a RNASeqSampleSet might have condition info
        for each reads object, but a single PairedEndLibrary may not have that info.
        If ref is already a Reads library, just returns a list with ref as a single element.
        """
        obj_type = self.get_type_from_obj_info(info)
        refs = list()
        if "KBaseSets.ReadsSet" in obj_type:
            print("Looking up reads references in ReadsSet object")
            set_client = SetAPI(self.srv_wiz_url)
            reads_set = set_client.get_reads_set_v1({'ref': ref,
                                                     'include_item_info': 0
                                                     })
            for reads in reads_set["data"]["items"]:
                refs.append({'ref': reads['ref'],
                             'condition': reads['label']
                             })
        elif "KBaseRNASeq.RNASeqSampleSet" in obj_type:
            print("Looking up reads references in RNASeqSampleSet object")
            sample_set = self.ws.get_objects2({"objects": [{"ref": ref}]})["data"][0]["data"]
            for i in range(len(sample_set["sample_ids"])):
                refs.append({'ref': sample_set["sample_ids"][i],
                             'condition': sample_set["condition"][i]
                             })
        else:
            raise ValueError("Unable to fetch reads reference from object {} "
                             "which is a {}".format(ref, obj_type))

        return refs



    def determine_input_info(self, validated_params):
        ''' get info on the input_ref object and determine if we run once or run on a set '''
        info = self.get_obj_info(validated_params['input_ref'])
        obj_type = self.get_type_from_obj_info(info)
        if obj_type in ['KBaseAssembly.PairedEndLibrary', 'KBaseAssembly.SingleEndLibrary',
                        'KBaseFile.PairedEndLibrary', 'KBaseFile.SingleEndLibrary']:
            return {'run_mode': 'single_library', 'info': info, 'ref': validated_params['input_ref']}
        if obj_type == 'KBaseRNASeq.RNASeqSampleSet':
            return {'run_mode': 'sample_set', 'info': info, 'ref': validated_params['input_ref']}
        if obj_type == 'KBaseSets.ReadsSet':
            return {'run_mode': 'sample_set', 'info': info, 'ref': validated_params['input_ref']}

        raise ValueError('Object type of input_ref is not valid, was: ' + str(obj_type))


    def get_type_from_obj_info(self, info):
        return info[2].split('-')[0]

    def get_obj_info(self, ref):
        return self.ws.get_object_info3({'objects': [{'ref': ref}]})['infos'][0]
