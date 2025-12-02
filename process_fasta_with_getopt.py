# A real-world FASTA processing tool with command-line options (-l length filter, -h help).

#!/usr/bin/env python3
"""
process_fasta_with_getopt.py
Demonstrates getopt for parsing:
    -h              help
    -l <length>     minimum sequence length filter
Usage:
    ./process_fasta_with_getopt.py -l 200 input.fa
"""

import sys
import getopt

def usage():
    print("""
Usage: process_fasta_with_getopt.py [-l length] <FASTA file>

Options:
  -h          Show this help message
  -l length   Minimum sequence length to print
""")

def read_fasta(filename):
    seqs = {}
    try:
        f = open(filename, "r")
    except IOError:
        sys.stderr.write(f"Error: Cannot open file '{filename}'\n")
        sys.exit(1)

    current = None

    for line in f:
        line = line.rstrip()
        if line.startswith(">"):
            header = line.split()[0][1:]
            seqs[header] = ""
            current = header
        else:
            seqs[current] += line

    f.close()
    return seqs


def main():
    # Parse options
    try:
        opts_list, args_list = getopt.getopt(sys.argv[1:], "l:h")
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    opts = {}
    for k, v in opts_list:
        opts[k] = v

    # Help option
    if "-h" in opts:
        usage()
        sys.exit(0)

    # Check required FASTA file
    if len(args_list) < 1:
        usage()
        sys.exit("Error: FASTA file missing")

    filename = args_list[0]

    # Optional length filter
    if "-l" in opts:
        try:
            min_len = int(opts["-l"])
            if min_len < 0:
                raise ValueError
        except ValueError:
            sys.exit("Error: Length must be a positive integer")
    else:
        min_len = 0

    seqs = read_fasta(filename)

    # Output filtered sequences
    for name, seq in seqs.items():
        if len(seq) >= min_len:
            print(f">{name}\n{seq}")

if __name__ == "__main__":
    main()
