# src/basic_examples.py
dna = input("Enter a DNA sequence: ")
if "n" in dna or "N" in dna:
    n_count = dna.count("n") + dna.count("N")
    print(f"Sequence contains {n_count} undefined bases (N).")
else:
    print("No undefined bases found.")
