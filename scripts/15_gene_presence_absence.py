import pandas as pd


k12_file = "results/tables/k12_gene_annotations.tsv"
ar0346_file = "results/tables/ar0346_gene_annotations.tsv"


k12 = pd.read_csv(k12_file, sep="\t")
ar0346 = pd.read_csv(ar0346_file, sep="\t")


k12_genes = set(k12["gene_name"])
ar0346_genes = set(ar0346["gene_name"])


all_genes = sorted(k12_genes | ar0346_genes)


presence_absence = []


for gene in all_genes:

    presence_absence.append({
        "gene_name": gene,
        "K12_present": gene in k12_genes,
        "AR0346_present": gene in ar0346_genes
    })


df = pd.DataFrame(presence_absence)


print("Presence/absence table:")
print(df.head(20))


output_file = "results/tables/gene_presence_absence.tsv"

df.to_csv(
    output_file,
    sep="\t",
    index=False
)


print()
print("Total unique gene names:", len(df))
print("Saved:", output_file)
