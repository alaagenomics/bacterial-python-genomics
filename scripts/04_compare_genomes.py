from Bio import SeqIO
from pathlib import Path


def calculate_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100


genome_files = Path("data/raw").glob("*.fasta")

for genome_file in genome_files:
    record = SeqIO.read(genome_file, "fasta")

    genome_length = len(record.seq)
    gc_content = calculate_gc_content(record.seq)

    print("File:", genome_file.name)
    print("Genome:", record.id)
    print("Length:", genome_length, "bp")
    print("GC content:", round(gc_content, 2), "%")
    print()
