# symbolic_overlay.py
# AURA | Dream Mapper Overlay on EBUDS CSV

import csv
import json

with open("auradb_glyph.json") as f:
    glyph_tags = json.load(f)

def tag(glyph):
    return glyph_tags.get(str(glyph), "🌀")

with open("ebuds.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        glyphs = list(map(int, row["Glyphs"].split()))
        meanings = [tag(g) for g in glyphs]
        print(f"{row['ID']}: {' → '.join(meanings)}")
