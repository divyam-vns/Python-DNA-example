#!/usr/bin/env python3
"""
This is my first Python program.
It computes the GC content of a DNA sequence.
"""

# Assign DNA sequence to a variable
dna = "AGCTCGATCGATCGATCGCGATCGATCGATCGA"

# Count the number of C's in the DNA sequence
no_c = dna.count('C')  # count C's in DNA sequence

# Count the number of G's in the DNA sequence
no_g = dna.count('G')  # count G's in DNA sequence

# Compute the length of the DNA sequence
dna_length = len(dna)  # total number of nucleotides

# Compute GC content as a percentage
gc_percent = ((no_c + no_g) / dna_length) * 100  # percentage of G and C

# Print the GC percentage
print("GC content: {:.2f}%".format(gc_percent))  # output with 2 decimal places
