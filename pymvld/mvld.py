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
