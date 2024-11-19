# this file just calls find_files.py and compare_files.py
import argparse
from pathlib import Path
import os

def main():
    parser = argparse.ArgumentParser(description="Compare two folders containing file lists.")
    parser.add_argument("folder1", type=Path, help="First folder containing file paths.")
    parser.add_argument("folder2", type=Path, help="Second folder containing file paths.")
    
    args = parser.parse_args()

    folder1 = args.folder1.resolve()
    folder2 = args.folder2.resolve()
    
    if not folder1.is_dir():
        print(f"Error: {folder1} is not a valid directory.")
        return
    
    if not folder2.is_dir():
        print(f"Error: {folder2} is not a valid directory.")
        return

    # run python find_files.py folder1 folder1_files.csv
    os.system(f"python find_files.py {args.folder1} {args.folder1}_files.csv")

    # run python find_files.py folder2 folder2_files.csv
    os.system(f"python find_files.py {args.folder2} {args.folder2}_files.csv")

    # run python compare_files.py folder1_files.csv folder2_files.csv
    os.system(f"python compare_files.py {args.folder1}_files.csv {args.folder2}_files.csv")


if __name__ == "__main__":
    main()