# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import shutil

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from kb_Bowtie2.kb_Bowtie2Impl import kb_Bowtie2
from kb_Bowtie2.kb_Bowtie2Server import MethodContext
from kb_Bowtie2.authclient import KBaseAuth as _KBaseAuth

from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from ReadsUtils.ReadsUtilsClient import ReadsUtils


class kb_Bowtie2AlignerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('kb_Bowtie2'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'kb_Bowtie2',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = kb_Bowtie2(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        # return 'test_kb_Bowtie2_1499812859552'
        suffix = int(time.time() * 1000)
        wsName = "test_kb_Bowtie2_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName


    def loadSingleEndReads(self):
        if hasattr(self.__class__, 'se_reads_ref'):
            return self.__class__.se_reads_ref
        # return '23735/2/1'
        fq_path = os.path.join(self.scratch, 'reads_1_se.fq')
        shutil.copy(os.path.join('data', 'bt_test_data', 'reads_1.fq'), fq_path)

        ru = ReadsUtils(self.callback_url)
        se_reads_ref = ru.upload_reads({'fwd_file': fq_path,
                                        'wsname': self.getWsName(),
                                        'name': 'test_readsSE',
                                        'sequencing_tech': 'artificial reads'})['obj_ref']
        self.__class__.se_reads_ref = se_reads_ref
        print('Loaded SingleEndReads: ' + se_reads_ref)
        return se_reads_ref


    def loadPairedEndReads(self):
        if hasattr(self.__class__, 'pe_reads_ref'):
            return self.__class__.pe_reads_ref
        # return '23735/3/1'
        fq_path1 = os.path.join(self.scratch, 'reads_1.fq')
        shutil.copy(os.path.join('data', 'bt_test_data', 'reads_1.fq'), fq_path1)
        fq_path2 = os.path.join(self.scratch, 'reads_2.fq')
        shutil.copy(os.path.join('data', 'bt_test_data', 'reads_2.fq'), fq_path2)

        ru = ReadsUtils(self.callback_url)
        pe_reads_ref = ru.upload_reads({'fwd_file': fq_path1, 'rev_file': fq_path2,
                                        'wsname': self.getWsName(),
                                        'name': 'test_readsPE',
                                        'sequencing_tech': 'artificial reads'})['obj_ref']
        self.__class__.pe_reads_ref = pe_reads_ref
        print('Loaded PairedEndReads: ' + pe_reads_ref)
        return pe_reads_ref


    def loadAssembly(self):
        if hasattr(self.__class__, 'assembly_ref'):
            return self.__class__.assembly_ref
        # return '23735/1/1'
        fasta_path = os.path.join(self.scratch, 'test_ref.fa')
        shutil.copy(os.path.join('data', 'bt_test_data', 'test_ref.fa'), fasta_path)
        au = AssemblyUtil(self.callback_url)
        assembly_ref = au.save_assembly_from_fasta({'file': {'path': fasta_path},
                                                    'workspace_name': self.getWsName(),
                                                    'assembly_name': 'test_assembly'
                                                    })
        self.__class__.assembly_ref = assembly_ref
        print('Loaded Assembly: ' + assembly_ref)
        return assembly_ref


    def loadSampleSet(self):
        if hasattr(self.__class__, 'sample_set_ref'):
            return self.__class__.sample_set_ref
        # return '23735/4/1'
        pe_reads_ref = self.loadPairedEndReads()
        sample_set_name = 'TestSampleSet'
        sample_set_data = {'Library_type': 'PairedEnd',
                           'domain': "Prokaryotes",
                           'num_samples': 3,
                           'platform': None,
                           'publication_id': None,
                           'sample_ids': [pe_reads_ref, pe_reads_ref, pe_reads_ref],
                           'sampleset_desc': None,
                           'sampleset_id': sample_set_name,
                           'condition': ['c1', 'c2', 'c3'],
                           'source': None
                           }

        ss_obj = self.getWsClient().save_objects({'workspace': self.getWsName(),
                                                  'objects': [{'type': 'KBaseRNASeq.RNASeqSampleSet',
                                                               'data': sample_set_data,
                                                               'name': sample_set_name,
                                                               'provenance': [{}]
                                                               }]
                                                  })
        ss_ref = "{}/{}/{}".format(ss_obj[0][6], ss_obj[0][0], ss_obj[0][4])
        print('Loaded SampleSet: ' + ss_ref)
        return ss_ref


    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx


    def test_bowtie2_aligner(self):
        assembly_ref = self.loadAssembly()
        se_lib_ref = self.loadSingleEndReads()
        params = {'input_ref': se_lib_ref,
                  'assembly_or_genome_ref': assembly_ref,
                  'output_obj_name_suffix': 'readsAlignment1',
                  'output_alignment_suffix': '_some_ext',
                  'output_workspace': self.getWsName(),
                  'concurrent_njsw_tasks': 0,
                  'concurrent_local_tasks': 1}
        pprint(params)
        res = self.getImpl().align_reads_to_assembly_app(self.getContext(), params)[0]
        pprint(res)
        self.assertIn('report_info', res)
        self.assertIn('report_name', res['report_info'])
        self.assertIn('report_ref', res['report_info'])

        ss_ref = self.loadSampleSet()
        params = {'input_ref': ss_ref,
                  'assembly_or_genome_ref': assembly_ref,
                  'output_obj_name_suffix': 'readsAlignment1',
                  'output_alignment_suffix': '_some_ext',
                  'output_workspace': self.getWsName(),
                  'concurrent_njsw_tasks': 0,
                  'concurrent_local_tasks': 1}
        pprint('Running with a SampleSet')
        pprint(params)
        res = self.getImpl().align_reads_to_assembly_app(self.getContext(), params)[0]
        pprint(res)
        self.assertIn('report_info', res)
        self.assertIn('report_name', res['report_info'])
        self.assertIn('report_ref', res['report_info'])
