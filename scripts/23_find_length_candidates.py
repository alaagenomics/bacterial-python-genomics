import pandas as pd


k12_file = (
    "results/tables/"
    "k12_protein_fingerprints.tsv"
)

ar0346_file = (
    "results/tables/"
    "ar0346_protein_fingerprints.tsv"
)


k12 = pd.read_csv(
    k12_file,
    sep="\t"
)

ar0346 = pd.read_csv(
    ar0346_file,
    sep="\t"
)


candidate_pairs = []


for _, k12_row in k12.iterrows():

    k12_length = k12_row["protein_length"]

    minimum_length = k12_length * 0.80
    maximum_length = k12_length * 1.20

    candidates = ar0346[
        (ar0346["protein_length"] >= minimum_length)
        & (ar0346["protein_length"] <= maximum_length)
    ]

    for _, ar_row in candidates.iterrows():

        candidate_pairs.append({
            "k12_protein": k12_row["protein_id"],
            "ar0346_protein": ar_row["protein_id"],
            "k12_length": k12_length,
            "ar0346_length": ar_row["protein_length"],
            "k12_sequence": k12_row["protein_sequence"],
            "ar0346_sequence": ar_row["protein_sequence"]
        })


candidates_df = pd.DataFrame(candidate_pairs)


output_file = (
    "results/tables/"
    "protein_length_candidates.tsv"
)


candidates_df.to_csv(
    output_file,
    sep="\t",
    index=False
)


print("K-12 proteins:", len(k12))
print("AR0346 proteins:", len(ar0346))
print()
print(
    "Candidate protein pairs:",
    len(candidates_df)
)
print()
print("Saved:", output_file)
