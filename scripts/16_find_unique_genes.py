import pandas as pd


input_file = "results/tables/gene_presence_absence.tsv"


df = pd.read_csv(input_file, sep="\t")


ar0346_only = df[
    (df["AR0346_present"] == True)
    & (df["K12_present"] == False)
]


k12_only = df[
    (df["K12_present"] == True)
    & (df["AR0346_present"] == False)
]


print("AR0346-only gene names:")
print(ar0346_only.head(20))


print()
print("Number of AR0346-only gene names:", len(ar0346_only))


print()
print("K-12-only gene names:")
print(k12_only.head(20))


print()
print("Number of K-12-only gene names:", len(k12_only))
