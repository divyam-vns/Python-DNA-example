#!/usr/bin/env python3
"""
Python Lists Tutorial Script
This script demonstrates basic and advanced list operations in Python,
as explained in the lecture.
"""

# --- 1. Create a list with different data types ---
gene_expression = ["gene", 0.045, 0.012, 7.33e-08]
print("Initial gene_expression list:", gene_expression)

# --- 2. Access elements by index ---
print("Third element (index 2):", gene_expression[2])
print("Last element (index -1):", gene_expression[-1])

# --- 3. Modify list elements (mutable type) ---
gene_expression[0] = "Lif"
print("After modifying first element:", gene_expression)

# --- 4. Strings are immutable ---
motif = "NCGT"
print("\nOriginal motif string:", motif)
try:
    motif[0] = "A"
except TypeError as e:
    print("Error when trying to modify string:", e)

# --- 5. Slicing lists ---
print("\nSlicing from -3 to end:", gene_expression[-3:])
print("Full copy using slice:", gene_expression[:])

# --- 6. Assigning to a slice (modifies list) ---
gene_expression[1:3] = ["New_value"]
print("After assigning to slice:", gene_expression)

# --- 7. Clearing a list using slice assignment ---
gene_expression[:] = []
print("After clearing list:", gene_expression)

# --- 8. Concatenating lists ---
gene_expression = ["Lif", 0.045, 7.33e-08]
new_data = ["extra", 0.999]
combined = gene_expression + new_data
print("\nConcatenated list:", combined)

# --- 9. len() and del statement ---
print("Length of combined list:", len(combined))
del combined[1]
print("After deleting index 1:", combined)

# --- 10. Using extend() (modifies list in place) ---
combined.extend(["added1", "added2"])
print("After extend():", combined)

# --- 11. Using count() ---
print("Count of 'Lif':", combined.count("Lif"))
print("Count of 'gene':", combined.count("gene"))

# --- 12. reverse() method ---
combined.reverse()
print("After reverse():", combined)

# --- 13. Using append() and pop() as a stack ---
stack = ["a", "b", "c", "d"]
stack.append("e")
print("\nStack after append:", stack)

stack.append(["x", "y"])  # Append a list as single element
print("Stack after appending a list:", stack)

elem = stack.pop()
print("Popped element:", elem)
print("Stack after pop:", stack)

# --- 14. Sorting lists ---
mylist = [3, 1, 4, 2]
print("\nOriginal mylist:", mylist)
print("Sorted(mylist):", sorted(mylist))
print("After calling sorted(), mylist remains:", mylist)

mylist.sort()
print("After mylist.sort():", mylist)

# --- 15. Sorting strings (alphabetical) ---
bases = ["A", "T", "G", "C"]
print("\nOriginal bases:", bases)
print("Sorted bases:", sorted(bases))
bases.sort()
print("After bases.sort():", bases)

print("\n✅ Tutorial completed successfully.")
