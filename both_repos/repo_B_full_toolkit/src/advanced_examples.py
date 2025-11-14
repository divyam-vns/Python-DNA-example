# src/advanced_examples.py
from textwrap import wrap

codon_table = {
    'ATA':'I','ATC':'I','ATT':'I','ATG':'M',
    'ACA':'T','ACC':'T','ACG':'T','ACT':'T',
    'AAC':'N','AAT':'N','AAA':'K','AAG':'K',
    'AGC':'S','AGT':'S','AGA':'R','AGG':'R',
    'CTA':'L','CTC':'L','CTG':'L','CTT':'L',
    'CCA':'P','CCC':'P','CCG':'P','CCT':'P',
    'CAC':'H','CAT':'H','CAA':'Q','CAG':'Q',
    'CGA':'R','CGC':'R','CGG':'R','CGT':'R',
    'GTA':'V','GTC':'V','GTG':'V','GTT':'V',
    'GCA':'A','GCC':'A','GCG':'A','GCT':'A',
    'GAC':'D','GAT':'D','GAA':'E','GAG':'E',
    'GGA':'G','GGC':'G','GGG':'G','GGT':'G',
    'TCA':'S','TCC':'S','TCG':'S','TCT':'S',
    'TTC':'F','TTT':'F','TTA':'L','TTG':'L',
    'TAC':'Y','TAT':'Y','TAA':'*','TAG':'*',
    'TGC':'C','TGT':'C','TGA':'*','TGG':'W',
}

def gc_content(seq):
    s = seq.upper()
    if len(s) == 0:
        return 0.0
    return round(100 * (s.count('G') + s.count('C')) / len(s), 2)

def translate(seq):
    seq = seq.upper().replace('\n','')
    protein = []
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        protein.append(codon_table.get(codon, 'X'))
    return ''.join(protein)

def find_orfs(seq):
    seq = seq.upper()
    starts = []
    orfs = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':
            starts.append(i)
    stops = {'TAA','TAG','TGA'}
    for s in starts:
        for j in range(s+3, len(seq)-2, 3):
            if seq[j:j+3] in stops:
                orfs.append(seq[s:j+3])
                break
    return orfs

def read_fasta(path):
    with open(path) as f:
        seqs = {}
        header = None
        for line in f:
            line=line.strip()
            if not line: continue
            if line.startswith('>'):
                header = line[1:].split()[0]
                seqs[header] = []
            else:
                seqs[header].append(line)
        return {h: ''.join(seqs[h]) for h in seqs}

if __name__ == '__main__':
    import sys
    path = sys.argv[1] if len(sys.argv)>1 else 'sequences/brca1_example.fasta'
    seqs = read_fasta(path)
    for name, seq in seqs.items():
        print(f"> {name} len={len(seq)} GC%={gc_content(seq)}")
        print("First 60 bases:", seq[:60])
        print("Translated (first 60 aa):", translate(seq)[:60])
        orfs = find_orfs(seq)
        print("Found ORFs:", len(orfs))
