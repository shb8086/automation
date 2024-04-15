"""
@file
@brief Script to rename files with specific extensions in a directory

This script renames files with the extensions '.jpg', '.jpeg', '.png', and '.pdf'
in the specified directory by combining the modified date and a cleaned-up version
of the original filename. It removes special characters, replaces spaces with underscores,
and ensures there is only one underscore between words in the filename.

@author Shima Bani (baniadam.shima@gmail.com)
@date January 4, 2024
"""

import os
import re
from datetime import datetime
import sys

def rename_files(directory_path):
  for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)

    if os.path.isfile(file_path):
      # Check if the file is an image or PDF (you can add more extensions if needed)
      if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf')):
        # Get the modified date of the file
        modified_time = os.path.getmtime(file_path)
        modified_date = datetime.utcfromtimestamp(modified_time).strftime('%Y_%m_%d')

        # Split the filename and extension
        base_filename, file_extension = os.path.splitext(filename)

        # Remove signs and replace spaces with underscores in the base filename
        new_base_filename = re.sub(r'[^\w\s]', '', base_filename)
        new_base_filename = re.sub(r'\s+', '_', new_base_filename)

        # Remove multiple underscores with just one underscore
        new_base_filename = re.sub(r'_+', '_', new_base_filename)

        # Combine the modified base filename and the original extension
        new_filename = modified_date + '_' + new_base_filename + file_extension
        new_file_path = os.path.join(directory_path, new_filename)

        os.rename(file_path, new_file_path)
        print(f'Renamed: {filename} to {new_filename}')

if __name__ == "__main__":
  # Get the directory path from the command-line argument, default to './' if no argument
  directory_path = sys.argv[1] if len(sys.argv) > 1 else './'

  # Check if the provided path exists
  if not os.path.exists(directory_path):
      print(f"Error: The provided path '{directory_path}' does not exist.")
  else:
      rename_files(directory_path)
