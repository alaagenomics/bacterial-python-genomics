from Bio import SeqIO

genome_file = "data/raw/genome.fasta"

record = SeqIO.read(genome_file, "fasta")

sequence = record.seq

genome_length = len(sequence)

a_count = sequence.count("A")
t_count = sequence.count("T")
g_count = sequence.count("G")
c_count = sequence.count("C")

gc_content = ((g_count + c_count) / genome_length) * 100

print("Genome:", record.id)
print("Genome length:", genome_length, "bp")
print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)
print("GC content:", round(gc_content, 2), "%")
