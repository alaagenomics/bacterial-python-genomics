from pathlib import Path


data_directory = Path("data/raw")

fasta_files = list(data_directory.rglob("*.fna"))


print("FASTA files found:", len(fasta_files))

for fasta_file in fasta_files:
    print(fasta_file)
