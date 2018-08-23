import pytest
from pymvld.mvld import *


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
        assert ('NP_004324',) == ad.refseq_protein

    def test_transcript_string_to_tuple(self, ad_v600e):
        ad_v600e['refseq_transcript'] = 'NM_004333'
        ad = AlleleDescriptive(**ad_v600e)
        assert ('NM_004333',) == ad.refseq_transcript

    def test_lists_to_tuple(self, ad_v600e):
        ad = AlleleDescriptive(**ad_v600e)
        assert ('NM_004333.4',) == ad.refseq_transcript
        assert ('NP_004324.2',) == ad.refseq_protein

    def test_valid_protein_reference_format(self, ad_v600e):
        # All entries start with NP_*
        with pytest.raises(AssertionError):
            ad_v600e['refseq_protein'] = ['NM_01234', 'NP_4456']
            AlleleDescriptive(**ad_v600e)
        with pytest.raises(AssertionError):
            ad_v600e['refseq_protein'] = 'NM_4456'
            AlleleDescriptive(**ad_v600e)
        with pytest.raises(AssertionError):
            ad_v600e['refseq_protein'] = ['NP_01234', 'NM_4456']
            AlleleDescriptive(**ad_v600e)
        ad_v600e['refseq_protein'] = ['NP_01234', 'NP_4456']
        assert AlleleDescriptive(**ad_v600e)

    def test_valid_transcript_reference_format(self, ad_v600e):
        # All entries start with NM_*
        with pytest.raises(AssertionError):
            ad_v600e['refseq_transcript'] = ['NM_01234', 'NP_4456']
            AlleleDescriptive(**ad_v600e)
        with pytest.raises(AssertionError):
            ad_v600e['refseq_transcript'] = 'NP_01234'
            AlleleDescriptive(**ad_v600e)
        with pytest.raises(AssertionError):
            ad_v600e['refseq_transcript'] = ['NP_01234', 'NM_4456']
            AlleleDescriptive(**ad_v600e)
        ad_v600e['refseq_transcript'] = ['NM_01234', 'NM_4456']
        assert AlleleDescriptive(**ad_v600e)

    def test_genome_version(self, ad_v600e):
        # Expecting a string
        with pytest.raises(AssertionError):
            ad_v600e['genome_version'] = 37
            AlleleDescriptive(**ad_v600e)
        # Expecting format of GRCh37, GRCh38
        with pytest.raises(AssertionError):
            ad_v600e['genome_version'] = 'HG19'
            AlleleDescriptive(**ad_v600e)
        # Case sensitive
        with pytest.raises(AssertionError):
            ad_v600e['genome_version'] = 'grch37'
            AlleleDescriptive(**ad_v600e)
        # Expecting human reference
        with pytest.raises(AssertionError):
            ad_v600e['genome_version'] = 'mm9'
            AlleleDescriptive(**ad_v600e)


class TestAlleleInterpretive():
    def test_instantiate(self):
        assert AlleleInterpretive()


class TestSomaticInterpretive():
    def test_instantiate(self):
        assert SomaticInterpretive()


class TestMVLD():
    def test_instantiate(self):
        assert MVLD()
