import pandas as pd


k12_file = "results/tables/k12_gene_annotations_normalized.tsv"
ar0346_file = "results/tables/ar0346_gene_annotations_normalized.tsv"


k12 = pd.read_csv(k12_file, sep="\t")
ar0346 = pd.read_csv(ar0346_file, sep="\t")


k12_products = set(
    k12["normalized_product"]
)

ar0346_products = set(
    ar0346["normalized_product"]
)


shared_products = (
    k12_products
    & ar0346_products
)

k12_only = (
    k12_products
    - ar0346_products
)

ar0346_only = (
    ar0346_products
    - k12_products
)


print("K-12 unique products:", len(k12_products))

print(
    "AR Bank #0346 unique products:",
    len(ar0346_products)
)

print()

print(
    "Shared products:",
    len(shared_products)
)

print(
    "K-12-only products:",
    len(k12_only)
)

print(
    "AR0346-only products:",
    len(ar0346_only)
)


print()
print("First 20 shared products:")

for product in sorted(shared_products)[:20]:
    print(product)


print()
print("First 20 AR0346-only products:")

for product in sorted(ar0346_only)[:20]:
    print(product)


print()
print("First 20 K-12-only products:")

for product in sorted(k12_only)[:20]:
    print(product)
