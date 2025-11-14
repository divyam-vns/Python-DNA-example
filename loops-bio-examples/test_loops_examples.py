import subprocess

def test_file(file_name):
    result = subprocess.run(['python3', file_name], capture_output=True, text=True)
    print(f"\n--- Output for {file_name} ---")
    print(result.stdout)

if __name__ == "__main__":
    files = [
        '01_find_donor_sites.py',
        '02_iterate_motifs.py',
        '03_range_examples.py',
        '04_protein_validator_all_positions.py',
        '05_protein_validator_break.py',
        '06_protein_remove_invalid_continue.py',
        '07_prime_numbers_with_else.py',
        '08_pass_statement_example.py'
    ]
    for f in files:
        test_file(f)