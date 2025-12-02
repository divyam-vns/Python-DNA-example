# Reads FASTA, builds dictionary {seq_id: sequence}.
#!/usr/bin/env python3
"""
read_fasta_to_dict.py
Reads a FASTA file and stores entries in a dictionary:
{sequence_name: sequence_string}
"""

import sys

def read_fasta(filename):
    seqs = {}

    try:
        f = open(filename, "r")
    except IOError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    current_name = None

    for line in f:
        line = line.rstrip()

        if line.startswith(">"):
            words = line.split()
            current_name = words[0][1:]  # remove '>'
            seqs[current_name] = ""
        else:
            seqs[current_name] += line

    f.close()
    return seqs


def main():
    if len(sys.argv) < 2:
        print("Usage: read_fasta_to_dict.py <FASTA file>")
        sys.exit(1)

    filename = sys.argv[1]
    seqs = read_fasta(filename)

    for name, seq in seqs.items():
        print(f"{name} -> {seq[:50]}... (length={len(seq)})")


if __name__ == "__main__":
    main()
