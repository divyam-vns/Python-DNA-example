# Decision Making and Repetition in Python (DNA Example)

This project demonstrates **Python decision-making and repetition concepts** using a simple biological context — analyzing DNA sequences.

It covers:
- `if`, `elif`, and `else` statements
- Boolean, comparison, membership, and identity operators
- Logical operators (`and`, `or`, `not`)
- Loops (`while`)

---

## Overview

This script allows you to input DNA sequences and provides feedback about undefined bases (`N` or `n`), using a series of examples that showcase Python’s control structures.

Each section illustrates a new concept with short examples and outputs.

---

## 🧩 Topics Covered

| Concept | Example Section |
|----------|----------------|
| Simple if–else | Section 1 |
| Boolean Expressions | Section 2 |
| Comparison & Membership | Section 3 |
| Identity Operators | Section 4 |
| if–elif–else | Section 5 |
| Logical Operators | Section 6 |
| Repetition (while loop) | Section 7 |

---

## How to Run

### Clone the Repository
```bash
git clone https://github.com/<your-username>/python-decision-making.git
cd python-decision-making
2️⃣ Run the Script
bash
Copy code
python3 decision_making_dna.py
💡 Example Output
text
Copy code
Enter a DNA sequence: ATGCnTTGCA
DNA sequence has 1 undefined bases (lowercase n).

--- Boolean Expression Examples ---
0 < 1: True
len('atgcgt') >= 10: False
'A' < 'C': True

--- Logical Operators Example ---
Enter a DNA sequence to test logical operators: ATGCNNTA
DNA sequence has 2 undefined bases (either N or n).

--- Repetition Example (while loop) ---
Enter a DNA sequence (or type 'exit' to quit): ATGC
DNA sequence has no undefined bases.
Enter a DNA sequence (or type 'exit' to quit): exit
Exiting program.
Learning Goals
Understand decision-making flow in Python

Learn to use if, elif, and else

Practice logical and membership operators

Explore repetition using loops

Apply programming logic in a biological data context

License
This project is open-source and free to use for educational purposes.
