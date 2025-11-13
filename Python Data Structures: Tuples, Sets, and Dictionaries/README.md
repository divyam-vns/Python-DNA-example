# Python Data Structures: Tuples, Sets, and Dictionaries

This repository contains a simple and well-documented Python script (`data_structures_examples.py`) demonstrating the use of **tuples**, **sets**, and **dictionaries** — three fundamental data structures in Python.

---

## Overview

### Tuples
- Immutable ordered collections.
- Elements cannot be modified once defined.
- Often used for heterogeneous data (mixed data types).

Example:
```python
t = (1, 2, 3)
print(t[0])   # Output: 1
Sets
Unordered collections with no duplicate elements.

Useful for mathematical operations like union, intersection, and difference.

Example:

python
brca1 = {"DNA repair", "cell cycle", "DNA repair"}
print(brca1)  # Output: {'DNA repair', 'cell cycle'}
Operations:

python
union = brca1 | brca2
intersection = brca1 & brca2
difference = brca1 - brca2
Dictionaries
Store key-value pairs.

Keys are unique and immutable.

Values can be of any type.

Example:

python
TF_motif = {"ATF": "TGACGTCA", "SP1": "GGGCGG"}
print(TF_motif["ATF"])  # Access value by key
Updating a dictionary:

python
TF_motif["AP-1"] = "TGACTCA"   # Add new key-value
del TF_motif["SP1"]            # Delete key-value
🚀 How to Run
Clone this repository:

bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
Run the script:

bash
python3 data_structures_examples.py
You’ll see example outputs showing how tuples, sets, and dictionaries behave.

Topics Covered
Tuple creation and immutability

Set creation, uniqueness, and operations (|, &, -)

Dictionary creation, lookup, update, and deletion

Retrieving and sorting keys and values

Learning Objective
This project is designed for beginners learning Python data structures in a bioinformatics or computational biology context — including examples with gene ontology and transcription factor motifs.

