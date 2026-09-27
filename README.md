# Bacterial Python Genomics

A Python-based bacterial comparative genomics project focused on genome statistics, gene annotation analysis, protein sequence comparison, and antimicrobial-resistance-associated protein screening.

The project uses *Escherichia coli* K-12 MG1655 and *E. coli* AR Bank #0346 as a comparative dataset. The workflow progresses from basic Python programming and genome analysis to sequence-level protein comparisons using BLASTP.

## Project objectives

This project was developed to build practical Python skills for bacterial genomics while answering several comparative questions:

- How do the two bacterial genomes compare in basic genome statistics?
- Which annotated genes are shared between the genomes?
- Which genes and functional annotations differ?
- How similar are the predicted protein sequences?
- Which AR0346 proteins carrying AMR-associated annotations have detectable sequence similarity to the K-12 proteome?

The workflow is script-based and reproducible rather than relying on manual spreadsheet analysis.

## Dataset

The project compares:

- *E. coli* K-12 MG1655
- *E. coli* AR Bank #0346

The K-12 reference genome used in the project is:

- NCBI assembly: GCF_000005845.2
- Genome length: 4,641,652 bp
- GC content: 50.79%

Genome annotations were obtained from NCBI genome datasets and parsed using Python.

## Workflow

The project is organized as a progressive Python genomics workflow.

### 1. Python and genome basics

Early scripts establish the Python environment and introduce basic sequence analysis:

```text
01_python_test.py
02_genome_statistics.py
03_gc_analysis.py
04_compare_genomes.py
05_find_genomes.py
06_batch_genome_statistics.py
## Protein-level analysis

The project then moves from gene annotations to predicted protein sequences.

### Protein extraction

`20_extract_proteins.py` parses CDS features from the genome annotations and extracts protein sequences using Biopython.

The translation workflow accounts for:

- CDS coordinates
- strand orientation
- CDS length
- bacterial translation table 11
- protein identifiers
- gene names
- locus tags
- functional product annotations

Clean protein tables are generated for both genomes:

```text
results/tables/k12_protein_sequences_clean.tsv
results/tables/ar0346_protein_sequences_clean.tsv

### Strong sequence matches

Three proteins met the strong-match screening criteria:

| AR0346 protein | K-12 protein | Identity | Query coverage | E-value |
|---|---|---:|---:|---:|
| CMY-2 | AmpC | 76.8% | 99% | 0 |
| MdtQ | MdtP | 35.4% | 96% | 1.12 × 10⁻⁸⁴ |
| QacEΔ1 | EmrE | 43.9% | 99% | 1.29 × 10⁻²⁴ |

The CMY-2/AmpC comparison showed the strongest sequence similarity, with 76.8% identity across 99% of the AR0346 query sequence.

Two additional strict BLASTP hits were below the strong-match criteria:

- FloR → Bcr: 29.6% identity, 92% coverage
- Tet(A) → YajR: 28.6% identity, 46% coverage

These matches were therefore not interpreted as evidence that the K-12 proteins perform the same biological function as the AR0346 AMR-associated proteins.

Two additional AR0346 proteins, MphR(A) and TetR(A), produced only weak/local similarities when the BLASTP search was relaxed to an E-value threshold of 0.1.

The remaining nine proteins had no detected BLASTP hit under the searches performed.

## Important interpretation

The BLASTP analysis identifies sequence similarity under defined search parameters. It does not by itself establish:

- that a protein is biologically absent from K-12
- that two proteins have identical functions
- that an AMR phenotype is caused by a particular protein
- that proteins without BLASTP hits have no homologs

Therefore, results are described as detected or undetected sequence similarity rather than definitive biological presence or absence.

The AMR annotations themselves were obtained from annotation/product descriptions used in the project and were not independently validated with a dedicated AMR database in this Python workflow.

More rigorous follow-up could include:

- domain analysis
- profile-based homology searches
- DIAMOND or MMseqs2 searches
- curated AMR databases
- phylogenetic analysis
- genomic-context analysis

## Main outputs

### Genome-level results

```text
results/tables/genome_statistics.tsv
results/tables/combined_genome_table.tsv
results/tables/genome_validation.tsv

```text
results/tables/ar0346_amr_final_comparison.tsv
results/tables/ar0346_amr_functional_category_summary.tsv
results/tables/ar0346_amr_matches.tsv
results/tables/ar0346_amr_sensitive_blastp.tsv
results/tables/ar0346_amr_unmatched_blastp.faa
results/tables/ar0346_amr_vs_k12_blastp.tsv


## Project structure


bacterial_python_genomics/
├── data/
│   ├── raw/
│   └── metadata/
├── scripts/
├── results/
│   ├── figures/
│   └── tables/
├── .gitignore
└── README.md

The project scripts are numbered according to the progression of the workflow, from basic Python tests and genome statistics through annotation parsing, protein analysis, and BLASTP comparison.

## Tools and libraries

### Programming
- Python
- Bash
- Git

### Python libraries
- Biopython
- pandas
- NumPy
- Matplotlib

### Bioinformatics software
- NCBI Datasets CLI
- BLASTP
- makeblastdb
### Data sources

- NCBI genome assemblies
- NCBI genome annotation files
- Protein sequence annotations associated with the comparative datasets

## Reproducibility

The analysis was developed in a Conda environment named:

bacterial-python

The workflow was designed to run from the project directory:

cd ~/bacterial_python_genomics
conda activate bacterial-python

Raw datasets and generated results are excluded from version control through .gitignore.

The scripts generate intermediate tables and final comparison files so that individual stages of the analysis can be inspected independently.

Because some steps depend on external sequence databases and annotation resources, exact output may vary if database versions, source annotations, or search parameters change.

## Scientific interpretation

This project demonstrates a progression from basic Python programming to sequence-level bacterial comparative genomics.

The protein comparison is intended as a computational screening workflow rather than a definitive functional annotation pipeline.

In particular:

- sequence similarity does not automatically establish identical biological function
- annotation differences do not automatically establish gene absence
- lack of a BLASTP hit does not prove that homologs are absent
- AMR-associated annotations should not by themselves be interpreted as experimental evidence of resistance phenotype
- the selected identity and coverage thresholds are screening criteria rather than universal definitions of homology or functional equivalence

The results therefore provide candidates and sequence-level observations that can be investigated with more specialized bioinformatics approaches.

## Future extensions

Possible extensions of the project include:

- automated genome downloading and metadata collection
- additional bacterial genomes for comparative analysis
- ortholog detection
- pangenome analysis
- domain and motif analysis
- profile-based homology searches
- DIAMOND or MMseqs2 protein searches
- curated AMR database comparison
- phylogenetic analysis
- genomic-context analysis
- automated visualization and reporting
- statistical comparison of larger bacterial datasets

## Summary

This project demonstrates a complete beginner-to-intermediate Python workflow for bacterial comparative genomics.

Starting with genome statistics and metadata validation, the workflow progresses through gene annotation analysis, protein extraction, exact sequence comparison, similarity screening, AMR-associated protein identification, and BLASTP-based comparison between E. coli AR Bank #0346 and E. coli K-12 MG1655.

The project emphasizes reproducible Python-based analysis and cautious interpretation of sequence similarity results.

It is designed as a portfolio project demonstrating practical skills in Python, Biopython, pandas, sequence analysis, bacterial genomics, and bioinformatics workflow development.
