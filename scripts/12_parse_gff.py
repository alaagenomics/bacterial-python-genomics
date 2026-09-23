from pathlib import Path


gff_file = Path(
    "data/raw/k12_annotation/ncbi_dataset/data/"
    "GCF_000005845.2/genomic.gff"
)


feature_counts = {}


with open(gff_file, "r") as file:

    for line in file:

        if line.startswith("#"):
            continue

        columns = line.rstrip().split("\t")

        feature_type = columns[2]

        if feature_type not in feature_counts:
            feature_counts[feature_type] = 0

        feature_counts[feature_type] += 1


print("Feature counts:")

for feature, count in feature_counts.items():
    print(feature, count)
