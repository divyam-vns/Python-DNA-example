# test_stopcodon.py
# Simple tests for validation


from functions import has_stop_codon


# Realistic DNA test sequence containing a stop codon at frame 1
real_dna = "AAATGAACCGTACGTTAGGACCTTAA"


print("DNA:", real_dna)
print("Frame 0:", has_stop_codon(real_dna, 0))
print("Frame 1:", has_stop_codon(real_dna, 1))
print("Frame 2:", has_stop_codon(real_dna, 2))
