#!/usr/bin/env python3

from pathlib import Path
import pandas as pd


INPUT_FILE = Path(
    "results/tables/ar0346_no_strong_k12_match.tsv"
)

CLASSIFIED_OUTPUT = Path(
    "results/tables/ar0346_no_strong_k12_match_classified.tsv"
)

SUMMARY_OUTPUT = Path(
    "results/tables/ar0346_no_strong_k12_match_categories.tsv"
)

MIN_PROTEIN_LENGTH = 50


def classify_product(product):
    product = str(product).lower()

    if any(term in product for term in [
        "antibiotic resistance",
        "antimicrobial resistance",
        "beta-lactamase",
        "efflux",
        "multidrug",
        "aminoglycoside",
        "tetracycline",
        "macrolide",
        "chloramphenicol",
        "colistin",
    ]):
        return "antimicrobial_resistance"

    if any(term in product for term in [
        "transporter",
        "transport",
        "permease",
        "porin",
        "pump",
    ]):
        return "transport"

    if any(term in product for term in [
        "virulence",
        "adhesin",
        "adhesion",
        "fimbr",
        "pilus",
        "secretion",
        "toxin",
    ]):
        return "virulence_or_adhesion"

    if any(term in product for term in [
        "stress",
        "oxidative",
        "heat shock",
        "cold shock",
    ]):
        return "stress_response"

    if any(term in product for term in [
        "lipopolysaccharide",
        "o-antigen",
        "glycosyltransferase",
        "cell envelope",
        "peptidoglycan",
    ]):
        return "cell_envelope"

    if any(term in product for term in [
        "dna",
        "replication",
        "repair",
        "recombinase",
        "restriction",
    ]):
        return "dna_replication_or_repair"

    if any(term in product for term in [
        "ribosomal",
        "translation",
        "rna polymerase",
        "trna",
    ]):
        return "rna_or_translation"

    if any(term in product for term in [
        "transcriptional regulator",
        "regulator",
        "repressor",
        "activator",
    ]):
        return "regulation"

    if any(term in product for term in [
        "dehydrogenase",
        "synthetase",
        "synthase",
        "metabolic",
        "metabolism",
        "enzyme",
    ]):
        return "metabolism"

    if any(term in product for term in [
        "hypothetical protein",
        "uncharacterized",
    ]):
        return "hypothetical_or_uncharacterized"

    return "other"


print("Loading AR0346 proteins without strong K-12 matches...")

df = pd.read_csv(
    INPUT_FILE,
    sep="\t"
)

print(f"Total proteins loaded: {len(df)}")

df = df[
    df["protein_length"] >= MIN_PROTEIN_LENGTH
].copy()

print(
    f"Proteins >= {MIN_PROTEIN_LENGTH} aa: {len(df)}"
)

df["functional_category"] = df["product"].apply(
    classify_product
)

summary = (
    df["functional_category"]
    .value_counts()
    .rename_axis("functional_category")
    .reset_index(name="protein_count")
)

print()
print("Functional categories:")
print(summary.to_string(index=False))

df.to_csv(
    CLASSIFIED_OUTPUT,
    sep="\t",
    index=False
)

summary.to_csv(
    SUMMARY_OUTPUT,
    sep="\t",
    index=False
)

print()
print(f"Saved classified proteins: {CLASSIFIED_OUTPUT}")
print(f"Saved category summary: {SUMMARY_OUTPUT}")
