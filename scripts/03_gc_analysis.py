from Bio import SeqIO


def calculate_gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    gc_content = (gc_count / len(sequence)) * 100
    return gc_content


genome_file = "data/raw/genome.fasta"

record = SeqIO.read(genome_file, "fasta")

gc = calculate_gc_content(record.seq)

print("Genome:", record.id)
print("GC content:", round(gc, 2), "%")
