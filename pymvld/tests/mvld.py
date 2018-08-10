import pytest
from pymvld.mvld import *
from dataclasses import FrozenInstanceError


@pytest.fixture
def ad_v600e():
    return {
        'genome_version': 'GRCh37',
        'gene': 'BRAF',
        'chromosome': 'chr7',
        'dna_position': 'NC_000007.13:g.140453136A>T',
        'refseq_transcript': ['NM_004333.4'],
        'refseq_protein': ['NP_004324.2']
    }


class TestAlleleDescriptive():
    def test_instantiate(self, ad_v600e):
        assert AlleleDescriptive(**ad_v600e)

    def test_hashable(self, ad_v600e):
        # This test implicitly evaluates immutability
        ad = AlleleDescriptive(**ad_v600e)
        assert hash(ad)

    def test_protein_string_to_tuple(self, ad_v600e):
        ad_v600e['refseq_protein'] = 'NP_004324'
        ad = AlleleDescriptive(**ad_v600e)
        assert ad.refseq_protein == ('NP_004324',)

    def test_transcript_string_to_tuple(self, ad_v600e):
        ad_v600e['refseq_transcript'] = 'NM_004333'
        ad = AlleleDescriptive(**ad_v600e)
        assert ad.refseq_transcript == ('NM_004333',)

    def test_lists_to_tuple(self, ad_v600e):
        ad_v600e['refseq_transcript'] = 'NM_004333'
        ad = AlleleDescriptive(**ad_v600e)
        assert ad.refseq_protein == ('NP_004324.2',)
        assert ad.refseq_transcript == ('NM_004333.4',)


class TestAlleleInterpretive():
    def test_instantiate(self):
        assert AlleleInterpretive()


class TestSomaticInterpretive():
    def test_instantiate(self):
        assert SomaticInterpretive()


class TestMVLD():
    def test_instantiate(self):
        assert MVLD()
