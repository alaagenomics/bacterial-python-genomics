from pathlib import Path
from Bio import SeqIO
import pandas as pd


def calculate_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100


def extract_accession(filename):
    parts = filename.split("_")
    return parts[0] + "_" + parts[1]


data_directory = Path("data/raw")

fasta_files = list(data_directory.rglob("*.fna"))

results = []

for fasta_file in fasta_files:

    records = list(SeqIO.parse(fasta_file, "fasta"))

    total_length = sum(len(record.seq) for record in records)

    combined_sequence = "".join(str(record.seq) for record in records)

    gc_content = calculate_gc_content(combined_sequence)

    accession = extract_accession(fasta_file.name)

    results.append({
        "accession": accession,
        "file": fasta_file.name,
        "genome": records[0].id,
        "contigs": len(records),
        "length_bp": total_length,
        "gc_percent": round(gc_content, 2)
    })


df = pd.DataFrame(results)

print(df)

output_file = "results/tables/genome_statistics.tsv"

df.to_csv(output_file, sep="\t", index=False)

print()
print("Saved:", output_file)
