import argparse
import csv
from pathlib import Path

def list_files_in_directory(root_dir: Path) -> list:
    """Recursively lists all files (not folders) in the root directory."""
    return [file.relative_to(root_dir) for file in root_dir.rglob('*') if file.is_file()]

def write_files_to_csv(files: list, output_file: Path):
    """Writes the list of files to a CSV file."""
    with output_file.open('w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for file in files:
            csv_writer.writerow([file])

def main():
    parser = argparse.ArgumentParser(description="List all files in a directory and save to a CSV.")
    parser.add_argument("root_dir", type=Path, help="Root directory to search for files.")
    parser.add_argument(
        "outdir", 
        type=Path, 
        help="Output CSV file path (default: cwd/files.csv)."
    )
    
    args = parser.parse_args()
    
    root_dir = args.root_dir.resolve()
    output_file = args.outdir.resolve()
    
    if not root_dir.is_dir():
        print(f"Error: {root_dir} is not a valid directory.")
        return

    # Get the list of files
    files = list_files_in_directory(root_dir)
    print(f"Found {len(files)} files.")
    
    # Write to the CSV file
    write_files_to_csv(files, output_file)
    print(f"File list written to {output_file}")
    print()

if __name__ == "__main__":
    main()
