# Problem- suppose we are only interested in finding if a protein sequence is valid, not where are all the invalid characters in the sequence.

# Stop at the first invalid amino acid.
protein = "MRTGWUASDJKLQWERUITYPAAJCH"
valid_aas = "ARNDCEQGHILKMFPSTWYV"  # 20 letters to represent 20 amimo acids.
for i in range(len(protein)):
    if protein[i] not in valid_aas:
        print("Not a valid protein sequence.")
        break


# Output
# Not a valid protein sequence.
