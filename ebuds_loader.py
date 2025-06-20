# ebuds_loader.py
# AURA | EBUDS Loader v0.1

# Simulates loading a simplified EBUDS dataset into a usable glyph token list

# Normally this would parse a full CSV or PDF; here we mock it for phase I

ebuds_sample_data = [
    {"id": "H200", "glyphs": [267, 99, 342]},
    {"id": "M133", "glyphs": [342, 176, 1]},
    {"id": "H901", "glyphs": [336, 89]},
    {"id": "X410", "glyphs": [8, 342, 1]},
    {"id": "M522", "glyphs": [391, 99, 99]}
]

def load_ebuds():
    for entry in ebuds_sample_data:
        print(f"{entry['id']}: {' → '.join(map(str, entry['glyphs']))}")

if __name__ == "__main__":
    load_ebuds()
