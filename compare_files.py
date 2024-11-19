import argparse
import csv
from pathlib import Path

def read_files_from_csv(csv_file: Path) -> set:
    """Reads file paths from a CSV file and returns them as a set."""
    with csv_file.open('r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        return [Path(row[0]) for row in csv_reader]

def main():
    parser = argparse.ArgumentParser(description="Compare two CSV files containing file lists.")
    parser.add_argument("csv_file1", type=Path, help="First CSV file containing file paths.")
    parser.add_argument("csv_file2", type=Path, help="Second CSV file containing file paths.")
    
    args = parser.parse_args()
    
    csv_file1 = args.csv_file1.resolve()
    csv_file2 = args.csv_file2.resolve()
    
    if not csv_file1.is_file():
        print(f"Error: {csv_file1} is not a valid file.")
        return
    
    if not csv_file2.is_file():
        print(f"Error: {csv_file2} is not a valid file.")
        return

    # Read file lists
    files1 = read_files_from_csv(csv_file1)
    files2 = read_files_from_csv(csv_file2)

    # file names
    file_names_1 = {file.name for file in files1}
    file_names_2 = {file.name for file in files2}

    # Differences
    files_only_in_1 = [file for file in files1 if file.name not in file_names_2]
    files_only_in_2 = [file for file in files2 if file.name not in file_names_1]
    files_in_both = [file for file in files1 if file.name in file_names_2]
    
    # Print results
    # green color
    print("\033[92m", end='')
    print(f"Files only in {csv_file1.name} ({len(files_only_in_1)})")
    for idx, file in enumerate(sorted(files_only_in_1)):
        print(f"{idx + 1:<3} {file}")
    print()

    # red color
    print(f"\033[91m", end='')
    print(f"Files only in {csv_file2.name} ({len(files_only_in_2)})")
    for idx, file in enumerate(sorted(files_only_in_2)):
        print(f"{idx + 1:<3} {file}")
    print()

    # yellow color
    print(f"\033[93m", end='')
    print(f"Files in both files ({len(files_in_both)})")
    for idx, file in enumerate(sorted(files_in_both)):
        print(f"{idx + 1:<3} {file.name}")
    print()

    # reset color
    print("\033[0m", end='')


if __name__ == "__main__":
    main()
