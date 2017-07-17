# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
from pprint import pprint
from kb_Bowtie2.util.Bowtie2IndexBuilder import Bowtie2IndexBuilder
from kb_Bowtie2.util.Bowtie2Aligner import Bowtie2Aligner
from kb_Bowtie2.util.Bowtie2Runner import Bowtie2Runner
#END_HEADER


class kb_Bowtie2:
    '''
    Module Name:
    kb_Bowtie2

    Module Description:
    A KBase module: kb_Bowtie2
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.1.0"
    GIT_URL = "git@github.com:kbaseapps/kb_Bowtie2.git"
    GIT_COMMIT_HASH = "fc2f147ea45b59fa54ab2663b06b40043613ffc5"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.scratch_dir = os.path.abspath(config['scratch'])
        self.workspace_url = config['workspace-url']
        self.srv_wiz_url = config['srv-wiz-url']
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        #END_CONSTRUCTOR
        pass


    def align_reads_to_assembly_app(self, ctx, params):
        """
        :param params: instance of type "AlignReadsParams" (Will align the
           input reads (or set of reads specified in a SampleSet) to the
           specified assembly or assembly for the specified Genome (accepts
           Assembly, ContigSet, or Genome types) and produces a
           ReadsAlignment object, or in the case of a SampleSet, a
           ReadsAlignmentSet object. required: input_ref - ref to either a
           SingleEnd/PairedEnd reads, or a SampleSet input (eventually should
           support a ReadsSet as well) assembly_or_genome - ref to Assembly,
           ContigSet, or Genome output_name - name of the output
           ReadsAlignment or ReadsAlignmentSet output_workspace - name or id
           of the WS to save the results to optional: ...) -> structure:
           parameter "input_ref" of String, parameter
           "assembly_or_genome_ref" of String, parameter "output_name" of
           String, parameter "output_workspace" of String, parameter
           "output_alignment_filename_extension" of String, parameter
           "phred33" of String, parameter "phred64" of String, parameter
           "local" of String, parameter "very-fast" of String, parameter
           "fast" of String, parameter "very-sensitive" of String, parameter
           "sensitive" of String, parameter "very-fast-local" of String,
           parameter "very-sensitive-local" of String, parameter "fast-local"
           of String, parameter "fast-sensitive" of String, parameter
           "quality_score" of String, parameter "alignment_type" of String,
           parameter "trim5" of Long, parameter "trim3" of Long, parameter
           "np" of Long, parameter "preset_options" of String, parameter
           "minins" of Long, parameter "maxins" of Long, parameter
           "orientation" of String, parameter "concurrent_njsw_tasks" of
           Long, parameter "concurrent_local_tasks" of Long
        :returns: instance of type "AlignReadsResult" -> structure: parameter
           "reads_alignment_ref" of String, parameter
           "read_alignment_set_ref" of String, parameter "report_name" of
           String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN align_reads_to_assembly_app
        print('Running align_reads_to_assembly_app() with params=')
        pprint(params)
        bowtie2_aligner = Bowtie2Aligner(self.scratch_dir, self.workspace_url,
                                         self.callback_url, self.srv_wiz_url,
                                         ctx.provenance())
        result = bowtie2_aligner.align(params)
        #END align_reads_to_assembly_app

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method align_reads_to_assembly_app return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def align_one_reads_to_assembly(self, ctx):
        """
        aligns a single reads object to produce
        """
        # ctx is the context object
        #BEGIN align_one_reads_to_assembly
        #END align_one_reads_to_assembly
        pass

    def get_bowtie2_index(self, ctx, params):
        """
        :param params: instance of type "GetBowtie2Index" (Provide a
           reference to either an Assembly or Genome to get a Bowtie2 index.
           output_dir is optional, if provided the index files will be saved
           in that directory.  If not, a directory will be generated for you
           and returned by this function.  If specifying the output_dir, the
           directory must not exist yet (to ensure only the index files are
           added there). Currently, Bowtie2 indexes are cached to a WS
           object.  If that object does not exist, then calling this function
           can create a new object.  To create the cache, you must specify
           the ws name or ID in 'ws_for_cache' in which to create the cached
           index.  If this field is not set, the result will not be cached.
           This parameter will eventually be deprecated once the big file
           cache service is implemented.) -> structure: parameter "ref" of
           String, parameter "output_dir" of String, parameter "ws_for_cache"
           of String
        :returns: instance of type "GetBowtie2IndexResult" (output_dir - the
           folder containing the index files from_cache - 0 if the index was
           built fresh, 1 if it was found in the cache pushed_to_cache - if
           the index was rebuilt and successfully added to the cache, this
           will be set to 1; otherwise set to 0) -> structure: parameter
           "output_dir" of String, parameter "from_cache" of type "boolean"
           (A boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "pushed_to_cache" of type "boolean" (A boolean - 0 for false, 1
           for true. @range (0, 1))
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN get_bowtie2_index
        print('Running get_bowtie2_index() with params=')
        pprint(params)
        bowtie2IndexBuilder = Bowtie2IndexBuilder(self.scratch_dir, self.workspace_url,
                                                  self.callback_url, self.srv_wiz_url,
                                                  ctx.provenance())
        result = bowtie2IndexBuilder.get_index(params)
        #END get_bowtie2_index

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method get_bowtie2_index return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def run_bowtie2_cli(self, ctx, params):
        """
        general purpose local function for running tools in the bowtie2 suite
        :param params: instance of type "RunBowtie2CLIParams" (supported
           commands: bowtie2 bowtie2-align-l bowtie2-align-s bowtie2-build
           bowtie2-build-l bowtie2-build-s bowtie2-inspect bowtie2-inspect-l
           bowtie2-inspect-s) -> structure: parameter "command_name" of
           String, parameter "options" of list of String
        """
        # ctx is the context object
        #BEGIN run_bowtie2_cli
        print('Running run_bowtie2_cli() with params=')
        pprint(params)

        if 'command' not in params:
            raise ValueError('required parameter field "command" was missing.')
        if 'options' not in params:
            raise ValueError('required parameter field "options" was missing.')

        bowtie2 = Bowtie2Runner(self.scratch_dir)
        bowtie2.run(params['command'], params['options'])

        #END run_bowtie2_cli
        pass
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
