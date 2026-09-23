from pathlib import Path

import pandas as pd
from Bio import SeqIO


def extract_proteins(genome_file, gff_file):

    genome_records = SeqIO.to_dict(
        SeqIO.parse(genome_file, "fasta")
    )

    proteins = []

    skipped = 0

    with open(gff_file, "r") as file:

        for line in file:

            if line.startswith("#"):
                continue

            columns = line.rstrip().split("\t")

            if len(columns) != 9:
                continue

            if columns[2] != "CDS":
                continue

            sequence_id = columns[0]

            start = int(columns[3])
            end = int(columns[4])

            strand = columns[6]

            attributes = columns[8]

            attribute_dict = {}

            for item in attributes.split(";"):

                if "=" in item:

                    key, value = item.split("=", 1)

                    attribute_dict[key] = value

            protein_id = attribute_dict.get(
                "protein_id",
                "unknown"
            )

            parent = attribute_dict.get(
                "Parent",
                "unknown"
            )

            gene = attribute_dict.get(
                "gene",
                "unknown"
            )

            locus_tag = attribute_dict.get(
                "locus_tag",
                "unknown"
            )

            product = attribute_dict.get(
                "product",
                "unknown"
            )

            dna = genome_records[sequence_id].seq[
                start - 1:end
            ]

            if strand == "-":
                dna = dna.reverse_complement()

            # Check that the CDS contains complete codons.
            if len(dna) % 3 != 0:
                skipped += 1
                continue

            protein = dna.translate(
                table=11,
                to_stop=True
            )

            proteins.append({
                "protein_id": protein_id,
                "parent": parent,
                "gene": gene,
                "locus_tag": locus_tag,
                "product": product,
                "strand": strand,
                "cds_length": len(dna),
                "protein_length": len(protein),
                "protein_sequence": str(protein)
            })

    return pd.DataFrame(proteins), skipped


# --------------------------------------------------
# K-12
# --------------------------------------------------

k12_genome = Path(
    "data/raw/k12_annotation/ncbi_dataset/data/"
    "GCF_000005845.2/"
    "GCF_000005845.2_ASM584v2_genomic.fna"
)

k12_gff = Path(
    "data/raw/k12_annotation/ncbi_dataset/data/"
    "GCF_000005845.2/"
    "genomic.gff"
)

k12, k12_skipped = extract_proteins(
    k12_genome,
    k12_gff
)

k12_output = (
    "results/tables/k12_protein_sequences_clean.tsv"
)

k12.to_csv(
    k12_output,
    sep="\t",
    index=False
)

print("K-12 proteins:", len(k12))
print("K-12 skipped:", k12_skipped)
print("Saved:", k12_output)


# --------------------------------------------------
# AR Bank #0346
# --------------------------------------------------

ar0346_genome = Path(
    "data/raw/ar0346_annotation/ncbi_dataset/data/"
    "GCF_017579865.1/"
    "GCF_017579865.1_ASM1757986v1_genomic.fna"
)

ar0346_gff = Path(
    "data/raw/ar0346_annotation/ncbi_dataset/data/"
    "GCF_017579865.1/"
    "genomic.gff"
)

ar0346, ar0346_skipped = extract_proteins(
    ar0346_genome,
    ar0346_gff
)

ar0346_output = (
    "results/tables/ar0346_protein_sequences_clean.tsv"
)

ar0346.to_csv(
    ar0346_output,
    sep="\t",
    index=False
)

print("AR0346 proteins:", len(ar0346))
print("AR0346 skipped:", ar0346_skipped)
print("Saved:", ar0346_output)
