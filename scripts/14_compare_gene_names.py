import pandas as pd


k12_file = "results/tables/k12_gene_annotations.tsv"
ar0346_file = "results/tables/ar0346_gene_annotations.tsv"


k12 = pd.read_csv(k12_file, sep="\t")
ar0346 = pd.read_csv(ar0346_file, sep="\t")


k12_genes = set(k12["gene_name"])
ar0346_genes = set(ar0346["gene_name"])


shared_genes = k12_genes & ar0346_genes

k12_only = k12_genes - ar0346_genes

ar0346_only = ar0346_genes - k12_genes


print("K-12 unique gene names:", len(k12_genes))
print("AR Bank #0346 unique gene names:", len(ar0346_genes))
print()
print("Shared gene names:", len(shared_genes))
print("K-12 only:", len(k12_only))
print("AR Bank #0346 only:", len(ar0346_only))


print()
print("First 20 shared genes:")

for gene in sorted(shared_genes)[:20]:
    print(gene)


print()
print("First 20 K-12-only genes:")

for gene in sorted(k12_only)[:20]:
    print(gene)


print()
print("First 20 AR Bank #0346-only genes:")

for gene in sorted(ar0346_only)[:20]:
    print(gene)
