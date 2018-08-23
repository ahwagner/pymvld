# pyMVLD
pyMVLD is a Python implementation of the Minimum Variant Level Data standard, first defined by the ClinGen Somatic Working Group in 2016 ([paper](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-016-0367-z)).

![MVLD Figure](https://media.springernature.com/full/springer-static/image/art%3A10.1186%2Fs13073-016-0367-z/MediaObjects/13073_2016_367_Fig3_HTML.gif)

## Why use pyMVLD
pyMVLD provides a concrete implementation for ensuring compliance with the MVLD standard. Use of this module provides:
* Validation of correct data types and values when generating MVLD objects
* Immutable, standardized objects for downstream applications
* Framework versioning

## How to use pyMVLD
Creating an MVLD object first requires construction of three sub-objects corresponding to the three field sets described by the framework: _AlleleDescriptive_, _AlleleInterpretive_, and _SomaticInterpretive_.

### Allele Descriptive Fields
The Allele Descriptive fields are expected to conform to the following rules:

#### Genome Version
The paper designates that the Genome Version must be in the GRCh37/GRCh38 format, preferably with the build version (e.g. GRCh38.p12). This implementation explicitly limits the values to a `str` describing GRCh37 or GRCh38, the two major GRC assemblies that are currently available. The assembly version, if provided, is checked only for syntactic correctness, not that it corresponds to a published version.

#### Gene
