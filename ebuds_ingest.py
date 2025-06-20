# ebuds_ingest.py
# AURA | EBUDS CSV Ingestor

import csv

def load_ebuds(file_path="ebuds.csv"):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            glyphs = list(map(int, row["Glyphs"].split()))
            print(f"{row['ID']}: {' → '.join(map(str, glyphs))}")

if __name__ == "__main__":
    load_ebuds()
