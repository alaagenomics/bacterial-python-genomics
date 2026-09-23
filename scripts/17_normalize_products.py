import pandas as pd


def normalize_product(product):
    """
    Clean a protein product description
    so similar descriptions are easier to compare.
    """

    if pd.isna(product):
        return "unknown"

    product = str(product).lower()

    # Remove extra whitespace
    product = " ".join(product.split())

    return product


k12_file = "results/tables/k12_gene_annotations.tsv"
ar0346_file = "results/tables/ar0346_gene_annotations.tsv"

k12 = pd.read_csv(k12_file, sep="\t")
ar0346 = pd.read_csv(ar0346_file, sep="\t")


k12["normalized_product"] = k12["product"].apply(
    normalize_product
)

ar0346["normalized_product"] = ar0346["product"].apply(
    normalize_product
)


print("K-12 products:")
print(k12["normalized_product"].head(10))

print()
print("AR0346 products:")
print(ar0346["normalized_product"].head(10))


k12_output = "results/tables/k12_gene_annotations_normalized.tsv"
ar0346_output = "results/tables/ar0346_gene_annotations_normalized.tsv"


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


print()
print("Saved:", k12_output)
print("Saved:", ar0346_output)
