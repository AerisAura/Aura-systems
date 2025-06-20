# dream_mapper.py
# AURA | Indus Dream Mapper v0.1

glyph_dreams = {
    (267, 99): "Trade Echo",
    (342, 1): "Boundary Seal",
    (336, 89): "Wave-Bearer",
    (293, 123): "Twin Grain",
    (391, 99): "Aftermark",
    (8, 342): "Gate Reversal",
    (347, 342): "Signature Return"
}

def interpret(glyph_pair):
    meaning = glyph_dreams.get(glyph_pair, "🌀 Unknown Symbolic Thread")
    print(f"{glyph_pair[0]} → {glyph_pair[1]} : {meaning}")

# Example
test_pairs = [(267, 99), (342, 1), (293, 123), (111, 222)]

for pair in test_pairs:
    interpret(pair)
