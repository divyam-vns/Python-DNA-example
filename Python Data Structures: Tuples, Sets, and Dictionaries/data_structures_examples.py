#!/usr/bin/env python3
# data_structures_examples.py
# Author: Your Name
# Description: Python examples of tuples, sets, and dictionaries
# To upload: git add data_structures_examples.py && git commit -m "Add tuple, set, and dictionary examples" && git push origin main

# ===============================
# 1. Tuples
# ===============================
print("\n=== Tuples ===")

# Define a tuple
t = 1, 2, 3, 4
print("Tuple t:", t)

# Equivalent definition with parentheses
t2 = (1, 2, 3, 4)
print("Tuple t2:", t2)

# Tuples are immutable
try:
    t[0] = 10
except TypeError as e:
    print("Error: Tuples are immutable ->", e)

# Tuples can contain mixed types
t3 = ("gene", 42, 3.14, True)
print("Heterogeneous tuple:", t3)


# ===============================
# 2. Sets
# ===============================
print("\n=== Sets ===")

# Define sets with duplicate entries
brca1 = {"DNA repair", "cell cycle", "DNA repair", "chromatin organization"}
print("BRCA1 GO terms (duplicates removed):", brca1)

brca2 = {"DNA repair", "cell cycle", "replication fork processing"}
print("BRCA2 GO terms:", brca2)

# Union (all unique elements)
union_terms = brca1 | brca2
print("Union (BRCA1 ∪ BRCA2):", union_terms)

# Intersection (common terms)
intersection_terms = brca1 & brca2
print("Intersection (BRCA1 ∩ BRCA2):", intersection_terms)

# Difference (terms in BRCA1 but not in BRCA2)
difference_terms = brca1 - brca2
print("Difference (BRCA1 - BRCA2):", difference_terms)


# ===============================
# 3. Dictionaries
# ===============================
print("\n=== Dictionaries ===")

# Define a dictionary of transcription factor motifs
TF_motif = {
    "ATF": "TGACGTCA",
    "c-Myc": "CACGTG",
    "SP1": "GGGCGG"
}
print("Initial TF_motif dictionary:", TF_motif)

# Access values by key
print("ATF motif:", TF_motif["ATF"])

# Check if a key exists
print("Is NF-1 in TF_motif?", "NF-1" in TF_motif)

# Add a new key-value pair
TF_motif["AP-1"] = "TGACTCA"
print("After adding AP-1:", TF_motif)

# Modify an existing entry
TF_motif["AP-1"] = "TGACACA"
print("After modifying AP-1:", TF_motif)

# Delete a key-value pair
del TF_motif["SP1"]
print("After deleting SP1:", TF_motif)

# Add multiple entries using update()
TF_motif.update({
    "NF-κB": "GGGACTTTCC",
    "CREB": "TGACGTCA",
    "E2F": "TTTCGCGC"
})
print("After bulk update:", TF_motif)

# Get dictionary length
print("Number of entries:", len(TF_motif))

# Get all keys and values
print("Keys:", list(TF_motif.keys()))
print("Values:", list(TF_motif.values()))

# Sorted keys and values
print("Sorted keys:", sorted(TF_motif.keys()))
print("Sorted values:", sorted(TF_motif.values()))

print("\n=== Summary ===")
print("We explored tuples (immutable), sets (unique unordered), and dictionaries (key-value pairs).")
