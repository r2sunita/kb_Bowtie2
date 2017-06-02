from pprint import pprint

import os
import time
import traceback

from kb_Bowtie2.util.Bowtie2Runner import Bowtie2Runner
from kb_Bowtie2.util.Bowtie2IndexBuilder import Bowtie2IndexBuilder

from ReadsUtils.ReadsUtilsClient import ReadsUtils

from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from Workspace.WorkspaceClient import Workspace
from GenomeAnnotationAPI.GenomeAnnotationAPIServiceClient import GenomeAnnotationAPI
from DataFileUtil.DataFileUtilClient import DataFileUtil


class Bowtie2Aligner(object):

    def __init__(self, scratch_dir, workspace_url, callback_url, srv_wiz_url, provenance):
        self.scratch_dir = scratch_dir
        self.workspace_url = workspace_url
        self.ws = Workspace(self.ws_url)
        self.callback_url = callback_url
        self.srv_wiz_url = srv_wiz_url
        self.bowtie2 = Bowtie2Runner(self.scratch_dir)
        self.provenance = provenance


    def run(self, params):
        validated_params = self.validate_params(params)
        run_mode = self.determine_run_mode(validated_params)

        if run_mode == 'single_library':
            read_lib_ref = validated_params['input_ref']
            assembly_or_genome_ref = validated_params['assembly_or_genome_ref']
            return self.single_reads_run(read_lib_ref, assembly_or_genome_ref,
                                         validated_params, create_report=True)

        if run_mode == 'sample_set':
            raise('sample set runs not yet supported')

        raise('Improper run mode')



    def single_reads_run(self, read_lib_info, assembly_or_genome_ref, validated_params,
            create_report=False, bowtie2_index_dir=None):
        ''' run on one reads '''

        # download reads and 

        setup_options = self.prepare_run(read_lib_info, assembly_or_genome_ref, bowtie2_index_dir)
        self.run_bowtie2_align_cli(setup_options, validated_params)
        self.save_output()

        if create_report:
            self.create_report()

        self.clean()


    def prepare_single_run(self, read_lib_info, assembly_or_genome_ref, bowtie2_index_dir,
                           ws_for_cache):
        ''' Given a reads ref and an assembly, setup the bowtie2 index '''
        # first setup the bowtie2 index of the assembly
        setup = {'bowtie2_index_dir': bowtie2_index_dir}
        if not bowtie2_index_dir:
            bowtie2IndexBuilder = Bowtie2IndexBuilder(self.scratch_dir, self.workspace_url,
                                                      self.callback_url, self.srv_wiz_url,
                                                      self.provenance)

            index_result = bowtie2IndexBuilder.get_index({'ref': assembly_or_genome_ref,
                                                          'ws_for_cache': ws_for_cache})
            setup['bowtie2_index_dir'] = index_result['output_dir']

        # next download the reads
        read_lib_type = read_lib_info[1].split('-')[0]
        read_lib_ref = str(read_lib_info[6]) + '/' + str(read_lib_info[0]) + '/' + str(read_lib_info[4])
        reads_params = {'read_libraries': [read_lib_ref],
                        'interleaved': 'false',
                        'gzipped': None
                        }
        ru = ReadsUtils(self.callbackURL)
        reads = ru.download_reads(reads_params)['files']

        setup['reads_lib_type'] = read_lib_info[1].split('-')[0].split('.')[1]
        setup['reads_files'] = reads

        return setup



    def validate_params(self, params):
        validated_params = {}
        if 'input_ref' in params and params['input_ref']:
            validated_params['input_ref'] = params['input_ref']
        else:
            raise ValueError('"input_ref" field pointing to reads or a sampleset required to run bowtie2 aligner')

        if 'assembly_or_genome_ref' in params and params['assembly_or_genome_ref']:
            validated_params['assembly_or_genome_ref'] = params['assembly_or_genome_ref']
        else:
            raise ValueError('"assembly_or_genome_ref" field required to run bowtie2 aligner')

        return validated_params



    def determine_run_mode(self, validated_params):
        info = self.get_obj_info(validated_params['input_ref'])
        obj_type = info[2]
        if obj_type in ['KBaseAssembly.PairedEndLibrary', 'KBaseAssembly.SingleEndLibrary',
                        'KBaseFile.PairedEndLibrary', 'KBaseFile.SingleEndLibrary']:
            return 'single_run'
        if obj_type == 'KBaseRNASeq.SampleSet':
            return 'sample_set'

        raise ValueError('Object type of input_ref is not valid, was: ' + str(obj_type))

    def get_obj_info(self, ref):
        return self.ws.get_object_info3({'objects': [{'ref': ref}]})['infos'][0]
