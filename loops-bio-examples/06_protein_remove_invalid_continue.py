protein = "MRTGWUASDJKLQWERUITYPAAJCH"
valid_aas = "ARNDCEQGHILKMFPSTWYV"
corrected = ""
for i in range(len(protein)):
    if protein[i] not in valid_aas:
        continue
    corrected += protein[i]
print("Corrected protein:", corrected)