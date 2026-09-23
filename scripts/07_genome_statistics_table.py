from pathlib import Path
from Bio import SeqIO
import pandas as pd


def calculate_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100


data_directory = Path("data/raw")

fasta_files = list(data_directory.rglob("*.fna"))

results = []

for fasta_file in fasta_files:
    record = SeqIO.read(fasta_file, "fasta")

    genome_length = len(record.seq)
    gc_content = calculate_gc_content(record.seq)

    results.append({
        "file": fasta_file.name,
        "genome": record.id,
        "length_bp": genome_length,
        "gc_percent": round(gc_content, 2)
    })


df = pd.DataFrame(results)

print(df)

output_file = "results/tables/genome_statistics.tsv"

df.to_csv(output_file, sep="\t", index=False)

print()
print("Saved:", output_file)
