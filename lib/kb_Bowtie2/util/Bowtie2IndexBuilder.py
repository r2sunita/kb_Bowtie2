from pprint import pprint

from kb_Bowtie2.util.Bowtie2Runner import Bowtie2Runner

from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from Workspace.WorkspaceClient import Workspace


class Bowtie2IndexBuilder(object):

    def __init__(self, scratch_dir, ws_url, callback_url, service_wizard_url):
        self.scratch_dir = scratch_dir
        self.ws_url = ws_url
        self.callback_url = callback_url
        self.service_wizard_url = service_wizard_url
        self.bowtie2 = Bowtie2Runner(self.scratch_dir)


    def get_index(self, params):
        ''' The key function of this module- get a bowtie2 index for the specified input '''

        # validate the parameters and fetch assembly_info
        validated_params = self._validate_params(params)
        assembly_info = self._get_assembly_info(validated_params['ref'])

        # check the cache (keyed off of assembly_info)
        index_info = self._get_cached_index(assembly_info)
        if not index_info:
            # on a cache miss, build the index
            index_info = self._build_index(assembly_info, validated_params)

        return index_info


    def _validate_params(self, params):
        ''' validate parameters; can do some processing here to produce validated params '''
        validated_params = {'ref': None}
        if 'assembly_ref' not in params:
            if 'genome_ref' in params:
                validated_params['ref'] = params['genome_ref']
            else:
                raise ValueError('Either "genome_ref" or "assembly_ref" are required.')

        else:
            if 'genome_ref' in params:
                raise ValueError('Both "genome_ref" and "assembly_ref" are set; use one and only one of these fields.')
            validated_params['ref'] = params['assembly_ref']

        if 'output_dir' in params:
            validated_params['output_dir'] = params['output_dir']

        return validated_params




    def _get_assembly_info(self, ref):
        ''' given a ref to an assembly or genome, figure out the assembly and return its info '''
        ws = Workspace(self.ws_url)
        info = ws.get_object_info3({'objects': [{'ref': ref}]})['infos'][0]
        obj_type = info[2]
        if obj_type.startswith('KBaseGenomeAnnotations.Assembly') or obj_type.startswith('KBaseGenomes.ContigSet'):
            return info

        if obj_type.startswith('KBaseGenomes.Genome'):
            # we need to get the assembly for this genome
            raise ValueError('Getting index for genome not yet supported')
            # todo:
            # use genome_annotation_api to get assembly ref
            # use ws call to get info

        raise ValueError('Input object was not of type: Assembly, ContigSet or Genome.  Cannot get Bowtie2 Index.')




    def _get_cached_index(self, assembly_info):
        return None

    def _put_cached_index(self, assembly_info, output_folder):
        pass


    def _build_index(self, assembly_info, validated_params):
        ref = self._build_obj_ref(assembly_info)
        au = AssemblyUtil(self.callback_url)
        fasta_info = au.get_assembly_as_fasta({'ref': ref})
        pprint(fasta_info)
        # {u'assembly_name': u'test_assembly',
        # u'path': u'/kb/module/work/tmp/test_assembly.fa'}

        cli_params = self._build_cli_params(fasta_info, validated_params)

        self.bowtie2.run('bowtie2-build', cli_params)




        self._put_cached_index(assembly_info, validated_params['output_folder'])
        pass


    def _build_cli_params(self, fasta_info, validated_params):
        cli_params = []

        return cli_params


    def _build_obj_ref(self, info):
        return str(info[6]) + '/' + str(info[0]) + '/' + str(info[4])

