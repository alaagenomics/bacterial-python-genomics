import hashlib
import pandas as pd


def protein_hash(sequence):
    """
    Create a SHA-256 fingerprint
    for a protein sequence.
    """

    return hashlib.sha256(
        sequence.encode("utf-8")
    ).hexdigest()


k12_file = (
    "results/tables/"
    "k12_protein_sequences_clean.tsv"
)

ar0346_file = (
    "results/tables/"
    "ar0346_protein_sequences_clean.tsv"
)


k12 = pd.read_csv(
    k12_file,
    sep="\t"
)

ar0346 = pd.read_csv(
    ar0346_file,
    sep="\t"
)


k12["protein_hash"] = (
    k12["protein_sequence"]
    .apply(protein_hash)
)

ar0346["protein_hash"] = (
    ar0346["protein_sequence"]
    .apply(protein_hash)
)


k12_output = (
    "results/tables/"
    "k12_protein_fingerprints.tsv"
)

ar0346_output = (
    "results/tables/"
    "ar0346_protein_fingerprints.tsv"
)


k12.to_csv(
    k12_output,
    sep="\t",
    index=False
)

ar0346.to_csv(
    ar0346_output,
    sep="\t",
    index=False
)


print("K-12 proteins:", len(k12))
print(
    "K-12 unique fingerprints:",
    k12["protein_hash"].nunique()
)

print()

print("AR0346 proteins:", len(ar0346))
print(
    "AR0346 unique fingerprints:",
    ar0346["protein_hash"].nunique()
)

print()

print(
    "Example K-12 fingerprint:"
)

print(
    k12.iloc[0]["protein_hash"]
)

print()

print(
    "Example AR0346 fingerprint:"
)

print(
    ar0346.iloc[0]["protein_hash"]
)

print()

print("Saved:", k12_output)
print("Saved:", ar0346_output)
