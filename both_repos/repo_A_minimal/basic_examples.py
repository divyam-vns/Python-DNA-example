# basic_examples.py - Minimal examples
dna = input("Enter a DNA sequence: ")
if "n" in dna or "N" in dna:
    n_count = dna.count("n") + dna.count("N")
    print(f"Sequence contains {n_count} undefined bases (N).")
else:
    print("No undefined bases found.")

motif = "ATG"
if motif in dna:
    print("Start codon (ATG) found in sequence.")
else:
    print("Start codon not found.")
