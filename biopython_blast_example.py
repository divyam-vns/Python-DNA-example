#!/usr/bin/env python3
"""
Biopython BLAST Example
-----------------------
This script demonstrates how to:
1. Check Biopython installation
2. Load a FASTA file
3. Run BLAST remotely using NCBI
4. Parse BLAST XML output
5. Filter hits by e-value
6. Print formatted alignment results

Author: Your Name
"""

# --------------------------------------------------------
# 1. Import Biopython and print the version (optional)
# --------------------------------------------------------
import Bio
print("Biopython version:", Bio.__version__)   # Shows installed version

# --------------------------------------------------------
# 2. Import the NCBI BLAST web API
# --------------------------------------------------------
from Bio.Blast import NCBIWWW   # Allows remote BLAST queries

# --------------------------------------------------------
# 3. Read your input FASTA file into a string
# --------------------------------------------------------
# Replace "myseq.fa" with your file name
with open("myseq.fa") as f:
    fasta_string = f.read()     # Reads the entire FASTA sequence as a string

# --------------------------------------------------------
# 4. Run BLASTN against the NCBI NT (nucleotide) database
# --------------------------------------------------------
# qblast(program, database, sequence)
# "blastn" → nucleotide BLAST
# "nt"     → NCBI non-redundant nucleotide database
print("Running BLAST... this may take 1–2 minutes.")
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

# --------------------------------------------------------
# 5. Parse the BLAST XML output using NCBIXML parser
# --------------------------------------------------------
from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)   # Converts XML into a BLAST record object

# --------------------------------------------------------
# 6. Print number of total alignments returned
# --------------------------------------------------------
print("Total BLAST hits returned:", len(blast_record.alignments))

# --------------------------------------------------------
# 7. Filtering BLAST results by e-value threshold
# --------------------------------------------------------
e_value_thresh = 0.01   # Accept hits with e-value < 0.01

print("\n=== Significant BLAST Hits (E < 0.01) ===\n")

# Loop through all alignments
for alignment in blast_record.alignments:
    # Each alignment may have multiple high-scoring pairs (HSPs)
    for hsp in alignment.hsps:

        # Check if this HSP is significant based on e-value
        if hsp.expect < e_value_thresh:
            # ------------------------------------------------------------
            # Print match metadata: title, length, e-value
            # ------------------------------------------------------------
            print("Alignment:", alignment.title)
            print("Length:", alignment.length)
            print("E-value:", hsp.expect)

            # ------------------------------------------------------------
            # Print sequence alignment: query vs subject
            # HSP contains:
            #   hsp.query   → query aligned region
            #   hsp.match   → match line ('|' = matches)
            #   hsp.sbjct   → subject (database hit) aligned region
            # ------------------------------------------------------------
            print("Query : ", hsp.query)
            print("Match : ", hsp.match)
            print("Subject:", hsp.sbjct)
            print("-" * 60)
