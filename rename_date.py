#!/usr/bin/env python3

import os
from datetime import datetime

def add_date_to_filename(file_path):
    """
    Adds the current date to the filename of a given file path.

    Args:
        file_path (str): The path of the file to be renamed.

    Returns:
        None

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If there is an error renaming the file.

    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    # Rest of the code...
def add_date_to_filename(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    # Get the current date
    current_date = datetime.now().strftime("%Y_%m_%d")

    # Split the file path into directory and filename
    directory, filename = os.path.split(file_path)

    # Split the filename into base and extension
    base, extension = os.path.splitext(filename)

    # Create the new filename with the current date
    new_filename = f"{current_date}_{base}{extension}"

    # Construct the new file path
    new_file_path = os.path.join(directory, new_filename)

    try:
        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"File '{file_path}' renamed to '{new_file_path}' with the current date.")
    except Exception as e:
        print(f"Error renaming file: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script_name.py /path/to/your/file.txt")
        sys.exit(1)

    file_path_to_rename = sys.argv[1]
    add_date_to_filename(file_path_to_rename)
