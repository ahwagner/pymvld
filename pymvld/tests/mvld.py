import pytest
from pymvld.mvld import *
from dataclasses import FrozenInstanceError


@pytest.fixture(scope="module")
def ad_v600e():
    return {
        'genome_version': 'GRCh37',
        'gene': 'BRAF',
        'chromosome': 'chr7',
        'dna_position': 'NC_000007.13:g.140453136A>T',
        'refseq_transcript': ['NM_004333.4:c.1799T>A', 'NM_004333.4:c.1799_1800delinsAA'],
        'refseq_protein': 'NP_004324.2:p.Val600Glu'
    }


class TestAlleleDescriptive():
    def test_instantiate(self, ad_v600e):
        assert AlleleDescriptive(**ad_v600e)

    def test_immutable(self, ad_v600e):
        ad = AlleleDescriptive(**ad_v600e)
        with pytest.raises(FrozenInstanceError):
            ad.chromosome = '12'
        with pytest.raises(FrozenInstanceError):
            ad.refseq_transcript.append('BLAT')


class TestAlleleInterpretive():
    def test_instantiate_allele_interpretive(self):
        assert AlleleInterpretive()


class TestSomaticInterpretive():
    def test_instantiate_somatic_interpretative(self):
        assert SomaticInterpretive()


class TestMVLD():
    def test_instantiate_MVLD(self):
        assert MVLD()