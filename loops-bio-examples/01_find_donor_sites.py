dna = "acgtgagtccgtatgtttaggtttgt"
pos = dna.find("gt")
while pos > -1:
    print("Found donor site (gt) at position:", pos)
    pos = dna.find("gt", pos + 1)