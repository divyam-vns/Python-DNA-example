# Python Lists Tutorial

This folder contains a **Python tutorial script** (`lists_tutorial.py`) that demonstrates how to use **lists** in Python — one of the most important data structures.  
It follows the lecture on Python data structures, focusing on list creation, indexing, slicing, mutability, and list methods.

---

##  Files
| File | Description |
|------|--------------|
| `lists_tutorial.py` | Main tutorial script demonstrating list operations |
| `README.md` | This file — explains what the script covers and how to use it |

---

## Concepts Covered

### 1. Creating a List
```python
gene_expression = ["gene", 0.045, 0.012, 7.33e-08]

Lists can hold multiple data types — strings, integers, floats, etc.

```
### 2. Indexing and Accessing Elements

```
gene_expression[2]   # Access third element
gene_expression[-1]  # Access last element
```
Indexes start at 0 in Python.

### 3. Mutability
Lists are mutable (can be changed).
Strings are immutable (cannot be changed).

### 4. Slicing and Assigning to Slices
```
gene_expression[1:3] = ["New_value"]
```
You can modify multiple elements at once or even clear the list.

### 5. List Operations

```
+ → Concatenate lists


len() → Length of list


del → Delete elements or slices

```

### if 6. List Methods
```
MethodDescription.extend()  →  Adds multiple elements
.count(x)  → Counts occurrences of x
.reverse()  → Reverses the list
.append(x)  → Adds one element to end
.pop()  → Removes and returns last element
.sort()Sorts list in place
sorted()  → Returns sorted copy

```
### 7. Using Lists as Stacks
Demonstrates how append() and pop() make lists behave like stacks (LIFO structure).

### 8. Sorting Examples
Shows how to sort both numeric and string lists.


### Run the script:
```
python3 lists_tutorial.py
```

You’ll see step-by-step printed outputs showing how lists behave.

Example Output (Excerpt)
```
Initial gene_expression list: ['gene', 0.045, 0.012, 7.33e-08]
Third element (index 2): 0.012
Last element (index -1): 7.33e-08
After modifying first element: ['Lif', 0.045, 0.012, 7.33e-08]
Error when trying to modify string: 'str' object does not support item assignment
...
Tutorial completed successfully.
```

License
This example code is provided for educational purposes and can be freely reused or modified.
