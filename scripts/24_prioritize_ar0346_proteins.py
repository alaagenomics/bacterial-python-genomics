#!/usr/bin/env python3

from pathlib import Path


# ------------------------------------------------------------
# Paths
# ------------------------------------------------------------

INPUT_FILE = Path(
    "results/tables/protein_length_candidates.tsv"
)

OUTPUT_FILE = Path(
    "results/tables/protein_sequence_similarity_candidates.tsv"
)


# ------------------------------------------------------------
# Parameters
# ------------------------------------------------------------

MIN_PROTEIN_LENGTH = 50
KMER_SIZE = 4
MIN_JACCARD = 0.30


# ------------------------------------------------------------
# Functions
# ------------------------------------------------------------

def get_kmers(sequence, k=4):
    """Return the set of k-mers in a protein sequence."""
    return {
        sequence[i:i + k]
        for i in range(len(sequence) - k + 1)
    }


def jaccard_similarity(set_a, set_b):
    """Calculate Jaccard similarity between two sets."""
    if not set_a or not set_b:
        return 0.0

    intersection = len(set_a & set_b)
    union = len(set_a | set_b)

    return intersection / union


# ------------------------------------------------------------
# Main analysis
# ------------------------------------------------------------

print("Reading candidate protein pairs...")
print(f"Input: {INPUT_FILE}")
print(f"Minimum protein length: {MIN_PROTEIN_LENGTH}")
print(f"K-mer size: {KMER_SIZE}")
print(f"Minimum Jaccard similarity: {MIN_JACCARD}")
print()

processed = 0
short_skipped = 0
strong_matches = 0


with INPUT_FILE.open("r") as infile, OUTPUT_FILE.open("w") as outfile:

    header = infile.readline().rstrip("\n").split("\t")

    k12_index = header.index("k12_protein")
    ar0346_index = header.index("ar0346_protein")
    k12_length_index = header.index("k12_length")
    ar0346_length_index = header.index("ar0346_length")
    k12_sequence_index = header.index("k12_sequence")
    ar0346_sequence_index = header.index("ar0346_sequence")

    output_header = [
        "k12_protein",
        "ar0346_protein",
        "k12_length",
        "ar0346_length",
        "length_ratio",
        "kmer_jaccard",
    ]

    outfile.write("\t".join(output_header) + "\n")

    for line in infile:

        processed += 1

        fields = line.rstrip("\n").split("\t")

        k12_protein = fields[k12_index]
        ar0346_protein = fields[ar0346_index]

        k12_length = int(fields[k12_length_index])
        ar0346_length = int(fields[ar0346_length_index])

        k12_sequence = fields[k12_sequence_index]
        ar0346_sequence = fields[ar0346_sequence_index]

        # Skip very short proteins
        if (
            k12_length < MIN_PROTEIN_LENGTH
            or ar0346_length < MIN_PROTEIN_LENGTH
        ):
            short_skipped += 1
            continue

        # Length ratio
        length_ratio = min(
            k12_length,
            ar0346_length
        ) / max(
            k12_length,
            ar0346_length
        )

        # Calculate k-mer similarity
        k12_kmers = get_kmers(k12_sequence, KMER_SIZE)
        ar0346_kmers = get_kmers(ar0346_sequence, KMER_SIZE)

        similarity = jaccard_similarity(
            k12_kmers,
            ar0346_kmers
        )

        # Keep strong sequence matches
        if similarity >= MIN_JACCARD:

            strong_matches += 1

            outfile.write(
                "\t".join(
                    [
                        k12_protein,
                        ar0346_protein,
                        str(k12_length),
                        str(ar0346_length),
                        f"{length_ratio:.4f}",
                        f"{similarity:.4f}",
                    ]
                )
                + "\n"
            )

        # Progress message
        if processed % 100000 == 0:
            print(
                f"Processed: {processed:,} | "
                f"strong matches: {strong_matches:,}"
            )


print()
print("Analysis complete.")
print(f"Candidate pairs processed: {processed:,}")
print(f"Short-protein pairs skipped: {short_skipped:,}")
print(f"Strong sequence matches: {strong_matches:,}")
print()
print(f"Output: {OUTPUT_FILE}")
