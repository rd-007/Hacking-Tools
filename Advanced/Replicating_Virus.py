"""
Simulated Self-Replicating Program (Educational Tool)

- This script demonstrates self-replication by copying itself to a specified directory.
- It is designed for educational purposes only and should not be used maliciously.

Usage: python self_replicating.py <target_directory> <number_of_copies>

Notes:
- Ensure the target directory exists before running the script.
- This program does not execute any harmful actions.

"""

import os
import shutil
import sys

def replicate(target_directory, number_of_copies):
    # Get the current script's file path
    current_file = os.path.abspath(__file__)
    
    for i in range(number_of_copies):
        # Create a new file name for the copy
        new_file_name = os.path.join(target_directory, f"self_replicating_copy_{i + 1}.py")
        
        # Copy the current script to the new file
        shutil.copy(current_file, new_file_name)
        print(f"Created: {new_file_name}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python self_replicating.py <target_directory> <number_of_copies>")
        sys.exit(1)

    target_directory = sys.argv[1]
    try:
        number_of_copies = int(sys.argv[2])
        if number_of_copies < 1:
            raise ValueError("Number of copies must be at least 1.")
    except ValueError as e:
        print(f"Invalid number of copies: {e}")
        sys.exit(1)

    if not os.path.exists(target_directory):
        print(f"Target directory '{target_directory}' does not exist.")
        sys.exit(1)

    replicate(target_directory, number_of_copies)

if __name__ == "__main__":
    main()
