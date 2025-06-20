# glyph_plotter.py
# AURA | Indus Glyph Frequency Plotter

import matplotlib.pyplot as plt

bigrams = {
    (267, 99): 168,
    (336, 89): 75,
    (342, 176): 59,
    (8, 342): 58,
    (391, 99): 56,
    (347, 342): 56,
    (342, 1): 48,
    (293, 123): 40
}

labels = [f"{a}→{b}" for (a, b) in bigrams]
frequencies = list(bigrams.values())

plt.figure(figsize=(10, 6))
plt.bar(labels, frequencies)
plt.xticks(rotation=45)
plt.title("Top Indus Bigrams by Frequency")
plt.ylabel("Frequency")
plt.xlabel("Glyph Pair")
plt.tight_layout()
plt.show()
