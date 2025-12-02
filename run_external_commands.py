#!/usr/bin/env python3
"""
run_external_commands.py
Demonstrates using subprocess to run:
- unix commands like ls
- real bioinformatics tools (example shown)
"""

import subprocess

def main():
    print("Running 'ls -l' ...")
    subprocess.call(["ls", "-l"])   # example unix command

    print("\nExample bioinformatics command (placeholder):")
    # Replace with real files and tools you have installed
    # subprocess.call([
    #     "tophat",
    #     "mouse_index",
    #     "reads_1.fq",
    #     "reads_2.fq"
    # ])    
    print("Bioinformatics command skipped (uncomment to run).")

if __name__ == "__main__":
    main()

# Demonstrates running external UNIX/bioinformatics programs.
