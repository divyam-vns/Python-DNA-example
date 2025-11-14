protein = "MRTGWUASDJKLQWERUITYPAAJCH"
valid_aas = "ARNDCEQGHILKMFPSTWYV"
for i in range(len(protein)):
    if protein[i] not in valid_aas:
        print("Invalid amino acid", protein[i], "at position", i)