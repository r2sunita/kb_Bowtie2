# -*- coding: utf-8 -*-
#BEGIN_HEADER
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
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass


    def align_reads_to_assembly(self, ctx, params):
        """
        :param params: instance of type "AlignReadsParams" -> structure:
           parameter "reads_ref" of String, parameter "assembly_ref" of
           String, parameter "genome_ref" of String, parameter "output_name"
           of String, parameter "ws_id" of String, parameter "sampleset_id"
           of String, parameter "genome_id" of String, parameter
           "bowtie_index" of String, parameter "phred33" of String, parameter
           "phred64" of String, parameter "local" of String, parameter
           "very-fast" of String, parameter "fast" of String, parameter
           "very-sensitive" of String, parameter "sensitive" of String,
           parameter "very-fast-local" of String, parameter
           "very-sensitive-local" of String, parameter "fast-local" of
           String, parameter "fast-sensitive" of String
        """
        # ctx is the context object
        #BEGIN align_reads_to_assembly
        #END align_reads_to_assembly
        pass

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
