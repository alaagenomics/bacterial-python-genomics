import pandas as pd


input_file = "results/tables/combined_genome_table.tsv"

df = pd.read_csv(input_file, sep="\t")


df["length_match"] = (
    df["length_bp_ncbi"] == df["length_bp_calculated"]
)

df["contig_match"] = (
    df["contigs_ncbi"] == df["contigs_calculated"]
)

df["gc_difference"] = (
    df["gc_percent_ncbi"] - df["gc_percent_calculated"]
).abs()

df["gc_match"] = (
    df["gc_difference"] < 0.25
)


print("Validation results:")

print(
    df[
        [
            "accession",
            "length_match",
            "contig_match",
            "gc_difference",
            "gc_match"
        ]
    ]
)


output_file = "results/tables/genome_validation.tsv"

df.to_csv(output_file, sep="\t", index=False)

print()
print("Saved:", output_file)
