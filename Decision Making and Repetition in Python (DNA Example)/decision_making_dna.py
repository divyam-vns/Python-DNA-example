#!/usr/bin/env python3
"""
decision_making_dna.py

Demonstration of decision making and repetition in Python using DNA sequence examples.
Covers:
- if / elif / else statements
- Boolean expressions
- Comparison, membership, and identity operators
- Logical operators (and, or, not)
- Simple repetition (while loop)
"""

# --- Section 1: Simple if-else condition ---
dna = input("Enter a DNA sequence: ")

if 'n' in dna:
    nbases = dna.count('n')
    print("DNA sequence has", nbases, "undefined bases (lowercase n).")
else:
    print("DNA sequence has no undefined bases (lowercase n).")


# --- Section 2: Boolean expressions ---
print("\n--- Boolean Expression Examples ---")
print("0 < 1:", 0 < 1)
print("len('atgcgt') >= 10:", len("atgcgt") >= 10)
print("'GT' != 'AG':", 'GT' != 'AG')
print("'A' < 'C':", 'A' < 'C')
print("10 + 1 == 11:", 10 + 1 == 11)


# --- Section 3: Comparison and membership operators ---
print("\n--- Comparison and Membership Examples ---")
print("'a' == 'A':", 'a' == 'A')
print("'a' != 'A':", 'a' != 'A')

motif = "ACGT"
dna_sample = "GGCACGTTA"
print("motif in dna_sample:", motif in dna_sample)
print("'TTA' not in dna_sample:", 'TTA' not in dna_sample)


# --- Section 4: Identity operators ---
print("\n--- Identity Operator Example ---")
alphabet = ['a', 'c', 'g', 't']
new_alphabet = alphabet[:]  # Copy of the list
print("alphabet == new_alphabet:", alphabet == new_alphabet)
print("alphabet is new_alphabet:", alphabet is new_alphabet)


# --- Section 5: if–elif–else example ---
print("\n--- if–elif–else Example ---")
dna = input("Enter a DNA sequence for extended check: ")

if 'n' in dna:
    nbases = dna.count('n')
    print("DNA sequence has", nbases, "undefined bases (lowercase n).")
elif 'N' in dna:
    nbases = dna.count('N')
    print("DNA sequence has", nbases, "undefined bases (uppercase N).")
else:
    print("DNA sequence has no undefined bases.")


# --- Section 6: Logical operators (and, or, not) ---
print("\n--- Logical Operators Example ---")
dna = input("Enter a DNA sequence to test logical operators: ")

if 'n' in dna or 'N' in dna:
    nbases = dna.count('n') + dna.count('N')
    print("DNA sequence has", nbases, "undefined bases (either N or n).")
else:
    print("DNA sequence has no undefined bases.")


# --- Section 7: Repetition example (while loop) ---
print("\n--- Repetition Example (while loop) ---")
while True:
    dna = input("Enter a DNA sequence (or type 'exit' to quit): ")
    if dna.lower() == 'exit':
        print("Exiting program.")
        break
    elif 'n' in dna or 'N' in dna:
        nbases = dna.count('n') + dna.count('N')
        print("DNA sequence has", nbases, "undefined bases.")
    else:
        print("DNA sequence has no undefined bases.")
