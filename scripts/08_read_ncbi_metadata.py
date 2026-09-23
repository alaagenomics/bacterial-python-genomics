import json


metadata_file = "data/raw/ar0346/ncbi_dataset/data/assembly_data_report.jsonl"

with open(metadata_file, "r") as file:
    line = file.readline()

data = json.loads(line)

print("Accession:", data["accession"])
print("Organism:", data["organism"]["organismName"])
print("Strain:", data["organism"]["infraspecificNames"]["strain"])
print("Assembly:", data["assemblyInfo"]["assemblyName"])
print("Contigs:", data["assemblyStats"]["numberOfContigs"])
print("Genome length:", data["assemblyStats"]["totalSequenceLength"])
print("GC:", data["assemblyStats"]["gcPercent"])
