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
