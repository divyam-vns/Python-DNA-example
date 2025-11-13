#!/usr/bin/env python3
# user_input_examples.py
# Example script demonstrating user input, type conversion, and formatted output

def main():
    # --- Getting DNA sequence from user ---
    dna = input("Enter a DNA sequence please: ")
    print("You entered the DNA sequence:", dna)

    # --- Getting a number from user ---
    my_number = input("Please enter a number: ")
    print("You entered (as string):", my_number)

    # Convert input string to integer
    actual_number = int(my_number)
    print("You converted it to integer:", actual_number)

    # Convert input string to float
    actual_float = float(my_number)
    print("You converted it to float:", actual_float)

    # --- Demonstrating character conversion ---
    char_code = 65
    char = chr(char_code)
    print(f"The character corresponding to ASCII code {char_code} is: {char}")

    # --- GC content example ---
    # Pretend we calculated GC content
    gc_perc = 53.06122448

    # Simple print
    print("The DNA sequence's GC content is", gc_perc, "%")

    # Formatted print with 3 decimal places
    print("Formatted GC content: %5.3f %%" % gc_perc)

    # Print as integer
    print("GC content as integer: %d" % gc_perc)

    # Print padded integer
    print("Padded GC content (3 spaces): %3d" % gc_perc)

    # Scientific notation
    print("GC content in scientific notation: %e" % gc_perc)

    # Print DNA sequence using string format
    print("DNA sequence printed with %%s: %s" % dna)

if __name__ == "__main__":
    main()

# What this does:
# Asks the user for a DNA sequence and a number
# Converts the number to int and float
# Shows character conversion with chr()
# Demonstrates formatted output using %f, %d, %e, %s
