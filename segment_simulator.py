# segment_simulator.py
# AURA | Indus Segment Analyzer v0.1

# Example glyph chain (can be replaced with EBUDS data later)
glyph_line = [267, 99, 342, 176, 336, 89, 293, 123, 391, 99]

def segment_chain(glyphs):
    segments = []
    i = 0
    while i < len(glyphs):
        if i + 3 <= len(glyphs):
            segment = glyphs[i:i+3]
            segments.append(segment)
            i += 3
        elif i + 2 <= len(glyphs):
            segment = glyphs[i:i+2]
            segments.append(segment)
            i += 2
        else:
            segments.append([glyphs[i]])
            i += 1
    return segments

segments = segment_chain(glyph_line)

print("\n🧬 Segmented Glyph Chain:\n")
for s in segments:
    print(" → ".join(map(str, s)))

