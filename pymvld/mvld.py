from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class AlleleDescriptive:
    genome_version: str
    gene: str
    chromosome: str
    dna_position: str
    refseq_transcript: Tuple[str]
    refseq_protein: Tuple[str]

    def __post_init__(self):
        if isinstance(self.refseq_transcript, str):
            object.__setattr__(self, 'refseq_transcript', (self.refseq_transcript, ))
        else:
            object.__setattr__(self, 'refseq_transcript', tuple(self.refseq_transcript))
        if isinstance(self.refseq_protein, str):
            object.__setattr__(self, 'refseq_protein', (self.refseq_protein, ))
        else:
            object.__setattr__(self, 'refseq_protein', tuple(self.refseq_protein))

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
