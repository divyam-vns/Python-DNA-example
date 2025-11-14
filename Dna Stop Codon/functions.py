# functions.py
# Boolean-style function to detect in-frame stop codons


# List of canonical stop codons
STOP_CODONS = ["tga", "tag", "taa"]


def has_stop_codon(dna, frame=0):
"""
Check whether a DNA sequence contains an in-frame stop codon.


Args:
dna (str): DNA sequence (A/T/G/C)
frame (int): reading frame (0, 1, or 2). Default = 0.


Returns:
bool: True if an in-frame stop codon exists, False otherwise.
"""


dna = dna.lower() # Normalize case
stop_found = False # Default return value


# Iterate 3 bases at a time
for i in range(frame, len(dna), 3):
codon = dna[i:i+3]


# If codon is shorter than 3 bases, ignore it
if len(codon) != 3:
break


if codon in STOP_CODONS:
stop_found = True
break


return stop_found
