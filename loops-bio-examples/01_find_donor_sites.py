# Scan DNA for canonical donor splice sites ("gt").
# Example DNA sequence
dna = "acgtgagtccgtatgtttaggtttgt"

# Find all "gt" donor splice sites
pos = dna.find("gt")

while pos > -1:
    print("Found donor site (gt) at position:", pos)
    pos = dna.find("gt", pos + 1)

# output 
# Found donor site (gt) at position: 2
# Found donor site (gt) at position: 6
# Found donor site (gt) at position: 10
# Found donor site (gt) at position: 14
# Found donor site (gt) at position: 20
# Found donor site (gt) at position: 24
