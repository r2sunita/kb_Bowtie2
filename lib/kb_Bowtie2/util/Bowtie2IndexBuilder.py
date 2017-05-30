from pprint import pprint

import os
import time

from kb_Bowtie2.util.Bowtie2Runner import Bowtie2Runner

from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from Workspace.WorkspaceClient import Workspace
from GenomeAnnotationAPI.GenomeAnnotationAPIServiceClient import GenomeAnnotationAPI


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
        if index_info:
            index_info['from_cache'] = 1
            index_info['pushed_to_cache'] = 0
        else:
            # on a cache miss, build the index
            index_info = self._build_index(assembly_info, validated_params)
            index_info['from_cache'] = 0
            # pushed_to_cache will be set in return from _build_index

        return index_info


    def _validate_params(self, params):
        ''' validate parameters; can do some processing here to produce validated params '''
        validated_params = {'ref': None}
        if 'assembly_ref' in params and params['assembly_ref']:
            if 'genome_ref' in params:
                raise ValueError('Both "genome_ref" and "assembly_ref" are set; use one and only one of these fields.')
            validated_params['ref'] = params['assembly_ref']
        else:
            if 'genome_ref' in params and params['genome_ref']:
                validated_params['ref'] = params['genome_ref']
            else:
                raise ValueError('Either "genome_ref" or "assembly_ref" are required.')

        if 'output_dir' in params:
            validated_params['output_dir'] = params['output_dir']
        else:
            validated_params['output_dir'] = os.path.join(self.scratch_dir,
                                                          'bowtie2_build' + str(int(time.time() * 100)))

        if os.path.exists(validated_params['output_dir']):
            raise('Output directory name specified (' + validated_params['output_dir'] +
                  ') already exists. Will not overwrite, so aborting.')

        if 'ws_for_cache' in params and params['ws_for_cache']:
            validated_params['ws_for_cache'] = params['ws_for_cache']
        else:
            print('WARNING: bowtie2 index if created will not be cached because "ws_for_cache" field not set')
            validated_params['ws_for_cache'] = None

        return validated_params


    def _get_assembly_info(self, ref):
        ''' given a ref to an assembly or genome, figure out the assembly and return its info '''
        ws = Workspace(self.ws_url)
        info = ws.get_object_info3({'objects': [{'ref': ref}]})['infos'][0]
        obj_type = info[2]
        if obj_type.startswith('KBaseGenomeAnnotations.Assembly') or obj_type.startswith('KBaseGenomes.ContigSet'):
            return {'info': info, 'ref': ref}

        if obj_type.startswith('KBaseGenomes.Genome'):
            # we need to get the assembly for this genome
            ga = GenomeAnnotationAPI(self.service_wizard_url)
            assembly_ref = ga.get_assembly({'ref': ref})
            # using the path ensures we can access the assembly even if we don't have direct access
            ref_path = ref + ';' + assembly_ref
            info = ws.get_object_info3({'objects': [{'ref': ref_path}]})['infos'][0]
            return {'info': info, 'ref': ref_path}

        raise ValueError('Input object was not of type: Assembly, ContigSet or Genome.  Cannot get Bowtie2 Index.')



    def _get_cached_index(self, assembly_info):

        return None

    def _put_cached_index(self, assembly_info, output_folder, ws_for_cache):

        if not ws_for_cache:
            print('WARNING: bowtie2 index cannot be cached becase "ws_for_cache" field not set')
            return False



        # zip up the folder and save to shock
        # TODO: contact the file caching service
        # right now: create the Bowtie2 index file and save to the WS

        return False


    def _build_index(self, assembly_info, validated_params):
        # get the assembly as a fasta file using AssemblyUtil
        au = AssemblyUtil(self.callback_url)
        fasta_info = au.get_assembly_as_fasta({'ref': assembly_info['ref']})

        # make the target destination folder (check again it wasn't created yet)
        if os.path.exists(validated_params['output_dir']):
            raise('Output directory name specified (' + validated_params['output_dir'] +
                  ') already exists. Will not overwrite, so aborting.')
        os.makedirs(validated_params['output_dir'])

        # configure the command line args and run it
        cli_params = self._build_cli_params(fasta_info, validated_params)
        self.bowtie2.run('bowtie2-build', cli_params)
        index_info = {'output_dir': validated_params['output_dir']}

        # cache the result, mark if it worked or not
        cache_success = self._put_cached_index(assembly_info,
                                               validated_params['output_dir'],
                                               validated_params['ws_for_cache'])
        if cache_success:
            index_info['pushed_to_cache'] = 1
        else:
            index_info['pushed_to_cache'] = 0

        return index_info


    def _build_cli_params(self, fasta_info, validated_params):
        cli_params = []

        # always run in quiet mode
        cli_params.append('--quiet')

        # positional args: first the fasta path, then the base name used for the index files
        cli_params.append(fasta_info['path'])
        cli_params.append(os.path.join(validated_params['output_dir'], fasta_info['assembly_name']))

        return cli_params
