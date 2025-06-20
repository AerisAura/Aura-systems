# interactive_aura.py
# AURA | Interactive Console v0.1

import json

with open("auradb_glyph.json") as f:
    glyph_tags = json.load(f)

def interpret_sequence(glyphs):
    tones = [glyph_tags.get(str(g), "🌀") for g in glyphs]
    return " → ".join(tones)

def run():
    print("🔮 AURA Interactive Console")
    print("Type glyph numbers separated by space (e.g. 267 99 342)")
    while True:
        raw = input("\n>>> ")
        if raw.lower() in ["exit", "quit"]:
            break
        try:
            glyphs = list(map(int, raw.strip().split()))
            print("🧬 Dream Resonance:
", interpret_sequence(glyphs))
        except:
            print("⚠️ Invalid input.")

if __name__ == "__main__":
    run()
