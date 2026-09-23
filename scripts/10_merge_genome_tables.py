import pandas as pd


statistics_file = "results/tables/genome_statistics.tsv"
metadata_file = "results/tables/ncbi_genome_metadata.tsv"


statistics = pd.read_csv(statistics_file, sep="\t")
metadata = pd.read_csv(metadata_file, sep="\t")


merged = metadata.merge(
    statistics,
    on="accession",
    how="left",
    suffixes=("_ncbi", "_calculated")
)


print("Combined genome table:")
print(merged)


output_file = "results/tables/combined_genome_table.tsv"

merged.to_csv(output_file, sep="\t", index=False)

print()
print("Saved:", output_file)
