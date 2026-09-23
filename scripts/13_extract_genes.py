from pathlib import Path
import pandas as pd


def parse_gff(gff_file):

    genes = {}
    cds_products = {}

    with open(gff_file, "r") as file:

        for line in file:

            if line.startswith("#"):
                continue

            columns = line.rstrip().split("\t")

            feature_type = columns[2]

            attributes = columns[8]

            attribute_dict = {}

            for item in attributes.split(";"):

                if "=" in item:
                    key, value = item.split("=", 1)
                    attribute_dict[key] = value

            if feature_type == "gene":

                gene_id = attribute_dict.get("ID", "unknown")

                genes[gene_id] = {
                    "gene_name": attribute_dict.get(
                        "Name",
                        "unknown"
                    ),
                    "locus_tag": attribute_dict.get(
                        "locus_tag",
                        "unknown"
                    ),
                    "start": int(columns[3]),
                    "end": int(columns[4]),
                    "strand": columns[6],
                    "length": (
                        int(columns[4])
                        - int(columns[3])
                        + 1
                    )
                }

            elif feature_type == "CDS":

                parent = attribute_dict.get(
                    "Parent",
                    "unknown"
                )

                product = attribute_dict.get(
                    "product",
                    "unknown"
                )

                cds_products[parent] = product

    for gene_id in genes:

        genes[gene_id]["product"] = cds_products.get(
            gene_id,
            "unknown"
        )

    return pd.DataFrame(genes.values())


k12_gff = Path(
    "data/raw/k12_annotation/ncbi_dataset/data/"
    "GCF_000005845.2/genomic.gff"
)


k12_df = parse_gff(k12_gff)


print("K-12 genes:", len(k12_df))

print()
print("First 5 genes:")

print(k12_df.head())


output_file = "results/tables/k12_gene_annotations.tsv"

k12_df.to_csv(
    output_file,
    sep="\t",
    index=False
)


print()
print("Saved:", output_file)

ar0346_gff = Path(
    "data/raw/ar0346_annotation/ncbi_dataset/data/"
    "GCF_017579865.1/genomic.gff"
)


ar0346_df = parse_gff(ar0346_gff)


print()
print("AR Bank #0346 genes:", len(ar0346_df))

print()
print("First 5 AR Bank #0346 genes:")

print(ar0346_df.head())


ar0346_output = "results/tables/ar0346_gene_annotations.tsv"

ar0346_df.to_csv(
    ar0346_output,
    sep="\t",
    index=False
)


print()
print("Saved:", ar0346_output)
