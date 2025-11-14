## What is a function?
1. A function takes input (arguments), performs calculations, and returns a result.
2. Functions help reuse code and make programs easier to understand.
3. Built-in functions: print(), len().
4. User-defined functions: functions you create yourself.

### Why create functions in bioinformatics?
Frequent operations on DNA sequences:
1. Compute GC percentage.
2. Check for in-frame stop codons.
3. Get complementary sequences.

### Python function syntax
```
def function_name(arguments):
    """Documentation string explaining function"""
    # function code
    return output
```
- Use def keyword.
- Indentation defines the function block.
- Optional docstring explains the function.
- Use return to output results.

### Example: GC percentage function
* Input: DNA sequence (string).
* Output: GC content (percentage).
* Ignore undefined bases (N).
```
# 1. Define a GC content function
def GC(DNA):
    """This function computes the GC percentage of a DNA sequence."""
    # Count undefined bases (N)
    nbases = DNA.count('N') + DNA.count('n')
    
    # Count G and C (case-insensitive)
    g_count = DNA.count('G') + DNA.count('g')
    c_count = DNA.count('C') + DNA.count('c')
    
    # Compute GC percentage
    GC_percent = (g_count + c_count) * 100 / (len(DNA) - nbases)
    
    return GC_percent

# 2. Call the GC function with a DNA sequence

dna_seq = "ATGCGCGTANNNATGC"
gc_value = GC(dna_seq)
print(gc_value)

3. Access function documentation
help(GC)
# or
print(GC.__doc__)

4. Example of local vs global variable
print(nbases)  # ❌ Error: nbases is local to the function GC # nbases exists only inside the GC function.

```

### Variable scope
* Local variables: Defined inside a function, only accessible within the function.
* Global variables: Defined outside any function, accessible anywhere in the program.
* Example: nbases in GC function is local.
```
print(nbases)  # ❌ Error: nbases is local to the function GC # nbases exists only inside the GC function.
```
