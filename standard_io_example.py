#!/usr/bin/env python3
"""
standard_io_example.py
Demonstrates:
- Reading from stdin
- Writing to stdout
- Writing to stderr
"""

import sys

def main():
    sys.stderr.write("INFO: Type text and press Ctrl-D when done.\n")

    data = sys.stdin.read()   # read raw input

    sys.stdout.write("You entered:\n")
    sys.stdout.write(data)

    if data.strip() == "":
        sys.stderr.write("WARNING: No input detected.\n")


if __name__ == "__main__":
    main()

# Shows stdin, stdout, stderr usage.
