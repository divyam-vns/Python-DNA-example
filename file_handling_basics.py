# Foundational file I/O with error handling, reading, writing, seeking.

#!/usr/bin/env python3
"""
file_handling_basics.py
Demonstrates:
- Opening files (r/w/a)
- Reading (line-by-line, full)
- Seeking
- Writing
- Error handling
"""

def main():
    filename = "myfile.txt"

    # ---- Opening a file safely ----
    try:
        f = open(filename, "r")  # Read mode
    except IOError:
        print(f"Error: File '{filename}' does not exist.")
        return

    # ---- Reading line-by-line (best for large files) ----
    print("Reading line-by-line:")
    for line in f:
        print(line.rstrip())

    # ---- Moving file pointer to the beginning ----
    f.seek(0)

    # ---- Reading whole file at once ----
    print("\nReading entire file using .read():")
    whole = f.read()
    print(whole)

    f.close()

    # ---- Writing to file ----
    with open(filename, "a") as fw:
        fw.write("This is an appended line.\n")

    print("Finished file operations.")


if __name__ == "__main__":
    main()
