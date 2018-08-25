from dataclasses import dataclass
from typing import Tuple
from pymvld.gene import HGNC
import re

TRANSCRIPT_RE = re.compile(r'NM_\d+(\.\d+)?$')
PROTEIN_RE = re.compile(r'NP_\d+(\.\d+)?$')
GENOME_VERSION_RE = re.compile(r'GRCh3(7|8)(\.p\d+)?$')

GENES = HGNC()

@dataclass(frozen=True)
class AlleleDescriptive:
    genome_version: str
    gene: str
    chromosome: str
    dna_position: str
    refseq_transcript: Tuple[str]
    refseq_protein: Tuple[str]

    GENOME_VERSIONS = ('GRCh37', 'GRCh38')

    def __post_init__(self):
        # Tuple creation
        if isinstance(self.refseq_transcript, str):
            object.__setattr__(self, 'refseq_transcript', (self.refseq_transcript, ))
        else:
            object.__setattr__(self, 'refseq_transcript', tuple(self.refseq_transcript))
        if isinstance(self.refseq_protein, str):
            object.__setattr__(self, 'refseq_protein', (self.refseq_protein, ))
        else:
            object.__setattr__(self, 'refseq_protein', tuple(self.refseq_protein))

        # Genome Version
        assert isinstance(self.genome_version, str), "Expected a string for genome version"
        assert GENOME_VERSION_RE.match(self.genome_version), \
            "Expected a value of GRCh37/GRCh38, with optional .pXX version"

        # Gene
        assert isinstance(self.gene, str), "Expected a string for gene"
        lookup = GENES.lookup(self.gene)
        assert lookup is not None, "Gene is not a recognized HGVS approved Gene Symbol or alias"
        if lookup.type == 'Approved':
            pass
        # TODO: Add other types--likely alias, retired, etc.

        # RefSeq Transcript Testing
        assert all([TRANSCRIPT_RE.match(x) for x in self.refseq_transcript]), \
            "Expected all RefSeq transcripts to be of form NM_*."

        # RefSeq Protein Testing
        assert all([PROTEIN_RE.match(x) for x in self.refseq_protein]), \
            "Expected all RefSeq proteins to be of form NP_*."

@dataclass
class AlleleInterpretive:
    hello: str


@dataclass
class SomaticInterpretive:
    hello: str


@dataclass
class MVLD:
    allele_descriptive: AlleleDescriptive
    allele_interpretive: AlleleInterpretive
    somatic_interpretive: SomaticInterpretive
