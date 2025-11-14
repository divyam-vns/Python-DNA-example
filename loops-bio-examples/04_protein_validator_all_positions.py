# PProblem - Find if all characters in given protein sequence are valid amino acids. Pseudocode - for each character in protein sequence, if character is not amino acid, print invalid character and its position in protein sequence.
# print all invalid amino acids with positions.

protein = "MRTGWUASDJKLQWERUITYPAAJCH"  # contains invalid U, J

valid_aas = "ARNDCEQGHILKMFPSTWYV"

for i in range(len(protein)):
    if protein[i] not in valid_aas:
        print("Invalid amino acid", protein[i], "at position", i)
# output 
# Invalid amino acid U at position 5
# Invalid amino acid J at position 9
# Invalid amino acid U at position 16
# Invalid amino acid J at position 23
