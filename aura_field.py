# aura_field.py
# AURA | Symbolic Tone Overlay Engine

import json

with open("auradb_glyph.json", "r") as f:
    glyph_tags = json.load(f)

def resonate(sequence):
    tones = [glyph_tags.get(str(g), "Unknown") for g in sequence]
    print("🔮 Symbolic Resonance:")
    print(" → ".join(tones))

# Example:
resonate([267, 99, 342])
resonate([336, 89, 1])
