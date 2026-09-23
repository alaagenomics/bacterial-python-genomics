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


# Create sets of protein fingerprints
k12_hashes = set(
    k12["protein_hash"]
)

ar0346_hashes = set(
    ar0346["protein_hash"]
)


# Find fingerprints present in both genomes
shared_hashes = (
    k12_hashes
    & ar0346_hashes
)


print(
    "K-12 unique proteins:",
    len(k12_hashes)
)

print(
    "AR0346 unique proteins:",
    len(ar0346_hashes)
)

print(
    "Identical protein sequences shared:",
    len(shared_hashes)
)


# Keep only proteins whose exact sequence
# occurs in both genomes.
shared_k12 = k12[
    k12["protein_hash"].isin(shared_hashes)
].copy()

shared_ar0346 = ar0346[
    ar0346["protein_hash"].isin(shared_hashes)
].copy()


print()
print(
    "K-12 proteins with identical match:",
    len(shared_k12)
)

print(
    "AR0346 proteins with identical match:",
    len(shared_ar0346)
)


# Save the shared proteins from each genome.
shared_k12.to_csv(
    "results/tables/"
    "shared_identical_proteins_k12.tsv",
    sep="\t",
    index=False
)

shared_ar0346.to_csv(
    "results/tables/"
    "shared_identical_proteins_ar0346.tsv",
    sep="\t",
    index=False
)


print()
print(
    "Saved shared protein tables."
)
