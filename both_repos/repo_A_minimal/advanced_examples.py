# advanced_examples.py - Slightly more advanced
def gc_content(seq):
    seq = seq.upper()
    gc = seq.count("G") + seq.count("C")
    return round(100 * gc / len(seq), 2) if len(seq) > 0 else 0.0

dna = input("Enter DNA sequence: ")
print("Length:", len(dna))
print("GC %:", gc_content(dna))
