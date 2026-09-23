from pathlib import Path
import json
import pandas as pd


data_directory = Path("data/raw")

metadata_files = list(data_directory.rglob("assembly_data_report.jsonl"))

results = []


for metadata_file in metadata_files:

    with open(metadata_file, "r") as file:
        line = file.readline()

    data = json.loads(line)

    results.append({
        "accession": data["accession"],
        "organism": data["organism"]["organismName"],
        "strain": data["organism"]["infraspecificNames"]["strain"],
        "assembly": data["assemblyInfo"]["assemblyName"],
        "contigs": data["assemblyStats"]["numberOfContigs"],
        "length_bp": int(data["assemblyStats"]["totalSequenceLength"]),
        "gc_percent": data["assemblyStats"]["gcPercent"],
        "protein_coding_genes": data["annotationInfo"]["stats"]["geneCounts"]["proteinCoding"],
        "total_genes": data["annotationInfo"]["stats"]["geneCounts"]["total"]
    })


df = pd.DataFrame(results)

print(df)

output_file = "results/tables/ncbi_genome_metadata.tsv"

df.to_csv(output_file, sep="\t", index=False)

print()
print("Saved:", output_file)
