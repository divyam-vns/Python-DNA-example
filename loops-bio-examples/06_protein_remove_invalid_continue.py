# The continue statement causes the program to continue with the next iteration of  the nearest enclosing loop, skipping the rest of the code in the loop.
# Problem - Delete all invalid amino acid characters from a protein sequence.
# Remove invalid amino acids using continue.
protein = "MRTGWUASDJKLQWERUITYPAAJCH"
valid_aas = "ARNDCEQGHILKMFPSTWYV"
corrected = ""
for i in range(len(protein)):
    if protein[i] not in valid_aas:
        continue
    corrected += protein[i]
print("Corrected protein:", corrected)

# output
# Corrected protein: MRTGWASDKLQWERITYPAACH
