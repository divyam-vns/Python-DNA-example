# python_basics_dna.py
# This file contains Python examples from a lecture on basic Python operations and string handling,
# including examples for DNA sequences.

# -----------------------------
# 1. Hello World
# -----------------------------
print("Hello world!")

# -----------------------------
# 2. Numbers and basic operations
# -----------------------------
# Addition
print(5 + 5)  # 10

# More complex operation
print(10.5 - 2 * 3)  # 4.5

# Powers
print(10 ** 2)  # 100

# Floor division and remainder
print(17 % 3)  # 2

# Order of operations
print(5 * 3 + 2)  # 17

# -----------------------------
# 3. Number types
# -----------------------------
# Integers
print(type(5))  # <class 'int'>

# Float (real numbers)
print(type(3.5))  # <class 'float'>

# Division examples (Python 3 style)
print(12 / 5)      # 2.4
print(12.0 / 5)    # 2.4

# Complex numbers
c = 3 + 2j
print(type(c))      # <class 'complex'>
print(c ** 2)       # Complex number operation

# -----------------------------
# 4. Strings
# -----------------------------
# Single and double quotes
dna1 = 'atg'
dna2 = "atg"
print(dna1, dna2)

# String with quotes inside
print("This is a codon, isn't it?")  # Use double quotes to include single quote
print('This is a codon, isn\'t it?') # Use escape character for single quote

# Multi-line string
dna_multi = """ATGCGTAC
GCTAGCTA
TTAGGC"""
print(dna_multi)

# -----------------------------
# 5. Printing nicely
# -----------------------------
# Using print function with multi-line string
print("""ATGCGTAC\
GCTAGCTA\
TTAGGC""")  # Backslash removes automatic newlines

# -----------------------------
# 6. String operators
# -----------------------------
# Concatenation
dna_concat = "ATG" + "CGA"
print(dna_concat)

# Replication
dna_copy = "ATG" * 3
print(dna_copy)

# Membership testing
print("ATG" in "ATGCGT")  # True
print("N" in "ATGCGT")    # False

# -----------------------------
# 7. Example: GC content calculation
# -----------------------------
dna_sequence = "ATGCGCGTACGATCGTACG"
gc_count = dna_sequence.count('G') + dna_sequence.count('C')
gc_content = (gc_count / len(dna_sequence)) * 100
print(f"GC content of sequence: {gc_content:.2f}%")
