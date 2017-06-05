from pprint import pprint

import os
import time
import traceback

from kb_Bowtie2.util.Bowtie2Runner import Bowtie2Runner
from kb_Bowtie2.util.Bowtie2IndexBuilder import Bowtie2IndexBuilder

from ReadsUtils.ReadsUtilsClient import ReadsUtils

from Workspace.WorkspaceClient import Workspace
from GenomeAnnotationAPI.GenomeAnnotationAPIServiceClient import GenomeAnnotationAPI
from DataFileUtil.DataFileUtilClient import DataFileUtil


class Bowtie2Aligner(object):

    def __init__(self, scratch_dir, workspace_url, callback_url, srv_wiz_url, provenance):
        self.scratch_dir = scratch_dir
        self.workspace_url = workspace_url
        self.ws = Workspace(self.workspace_url)
        self.callback_url = callback_url
        self.srv_wiz_url = srv_wiz_url
        self.bowtie2 = Bowtie2Runner(self.scratch_dir)
        self.provenance = provenance


    def align(self, params):
        validated_params = self.validate_params(params)
        input_info = self.determine_input_info(validated_params)
        # input info provides information on the input and tells us if we should
        # run as a single_library or as a set:
        #     input_info = {'run_mode': '', 'info': [..], 'ref': '55/1/2'}

        if input_info['run_mode'] == 'single_library':
            assembly_or_genome_ref = validated_params['assembly_or_genome_ref']
            single_lib_result = self.single_reads_lib_run(input_info, assembly_or_genome_ref,
                                                          validated_params, create_report=True)
            return single_lib_result['report_info']


        if input_info['run_mode'] == 'sample_set':
            raise('sample set runs not yet supported')


        raise ('Improper run mode')



    def single_reads_lib_run(self, read_lib_info, assembly_or_genome_ref, validated_params,
                             create_report=False, bowtie2_index_dir=None):
        ''' run on one reads '''

        # download reads and prepare any bowtie2 index files
        input_configuration = self.prepare_single_run(read_lib_info, assembly_or_genome_ref,
                                                      bowtie2_index_dir, validated_params['output_workspace'])
        pprint(input_configuration)

        # run the actual program
        self.run_bowtie2_align_cli(input_configuration, validated_params)

        # process the result and save the output
        output_info = self.save_output()

        report_info = None
        if create_report:
            report_info = self.create_report(output_info)

        self.clean(output_info)

        results = {'output_info': output_info}
        if report_info:
            results['report_info'] = report_info

        return results


    def prepare_single_run(self, input_info, assembly_or_genome_ref,
                           bowtie2_index_dir, ws_for_cache):
        ''' Given a reads ref and an assembly, setup the bowtie2 index '''
        # first setup the bowtie2 index of the assembly
        input_configuration = {'bowtie2_index_dir': bowtie2_index_dir}
        if not bowtie2_index_dir:
            bowtie2IndexBuilder = Bowtie2IndexBuilder(self.scratch_dir, self.workspace_url,
                                                      self.callback_url, self.srv_wiz_url,
                                                      self.provenance)

            index_result = bowtie2IndexBuilder.get_index({'ref': assembly_or_genome_ref,
                                                          'ws_for_cache': ws_for_cache})
            input_configuration['bowtie2_index_dir'] = index_result['output_dir']

        # next download the reads
        read_lib_ref = input_info['ref']
        read_lib_info = input_info['info']
        reads_params = {'read_libraries': [read_lib_ref],
                        'interleaved': 'false',
                        'gzipped': None}
        ru = ReadsUtils(self.callback_url)
        reads = ru.download_reads(reads_params)['files']

        input_configuration['reads_lib_type'] = read_lib_info[2].split('-')[0].split('.')[1]
        input_configuration['reads_files'] = reads

        return input_configuration



    def validate_params(self, params):
        validated_params = {}

        required_string_fields = ['input_ref', 'assembly_or_genome_ref', 'output_name', 'output_workspace']
        for field in required_string_fields:
            if field in params and params[field]:
                validated_params[field] = params[field]
            else:
                raise ValueError('"' + field + '" field required to run bowtie2 aligner app')

        return validated_params


    def determine_input_info(self, validated_params):
        ''' get info on the input_ref object and determine if we run once or run on a set '''
        info = self.get_obj_info(validated_params['input_ref'])
        obj_type = info[2].split('-')[0]
        if obj_type in ['KBaseAssembly.PairedEndLibrary', 'KBaseAssembly.SingleEndLibrary',
                        'KBaseFile.PairedEndLibrary', 'KBaseFile.SingleEndLibrary']:
            return {'run_mode': 'single_library', 'info': info, 'ref': validated_params['input_ref']}
        if obj_type == 'KBaseRNASeq.SampleSet':
            return {'run_mode': 'sample_set', 'info': info, 'ref': validated_params['input_ref']}

        raise ValueError('Object type of input_ref is not valid, was: ' + str(obj_type))


    def get_obj_info(self, ref):
        return self.ws.get_object_info3({'objects': [{'ref': ref}]})['infos'][0]
