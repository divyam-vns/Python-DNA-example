# Python Variables and Strings Examples

# -------------------------------
# Basic Variable Assignment
# -------------------------------
codon = "ATG"
dna_sequence = "GTACGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"

# Printing variable values
print("Codon:", codon)
print("DNA sequence:", dna_sequence)

# -------------------------------
# Using undefined variable (will raise error)
# -------------------------------
# Uncommenting the next line will raise an error
# print(DNA)  # NameError: name 'DNA' is not defined

# -------------------------------
# Copying variables and arithmetic
# -------------------------------
a = 4
b = a  # assign value of a to b
print("a =", a)
print("b =", b)

b = b + 3  # update b
print("Updated b =", b)
print("a remains =", a)

# -------------------------------
# Variable naming rules
# -------------------------------
myvariable = 1
MyVariable = 2
MYVARIABLE = 3

# Legal variable names
name = "Alice"
_str = "underscore"
DNA = "GATTACA"
sequence1 = "AGCT"

# Illegal variable names (uncomment to see errors)
# 1string = "invalid"
# name# = "invalid"
# year@20 = 2025

# -------------------------------
# String Indexing and Slicing
# -------------------------------
dna = "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAG"

# Access individual characters
print("First character:", dna[0])
print("Last character:", dna[-1])
print("Second from end:", dna[-2])

# Slicing
print("First three characters:", dna[0:3])
print("Start to 3:", dna[:3])
print("From index 2 to end:", dna[2:])

# -------------------------------
# Useful String Functions
# -------------------------------
print("Length of dna:", len(dna))
print("Count of 'c':", dna.count('c'))
print("Count of 'GC':", dna.count('GC'))

# Uppercase and lowercase
dna_upper = dna.upper()
print("Uppercase DNA:", dna_upper)

# Finding substrings
print("First 'AG' at index:", dna.find('AG'))
print("Next 'AG' after index 17:", dna.find('AG', 17))
print("Last 'AG' using rfind:", dna.rfind('AG'))

# Check if string is lowercase or uppercase
print("Is lowercase?", dna.islower())
print("Is uppercase?", dna.isupper())

# Replace characters
dna_replaced = dna.replace('a', 'A')
print("Replaced 'a' with 'A':", dna_replaced)

# -------------------------------
# End of Python Variables and Strings Demo
# -------------------------------
