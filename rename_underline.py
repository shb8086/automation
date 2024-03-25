import sys
import os
import re

def rename_files(directory=None):
  if directory is None:
    # Get the current working directory if no directory is provided
    directory = os.getcwd()
  else:
    # Check if the provided directory exists
    if not os.path.exists(directory):
      print("Directory does not exist. Using the current working directory instead.")
      directory = os.getcwd()

  # Get list of visible files in the directory
  files = [f for f in os.listdir(directory) if not f.startswith('.')]

  # Iterate through each file
  for filename in files:
    # Check if it's a file
    if os.path.isfile(os.path.join(directory, filename)):
      # Split filename into base name and extension
      base_name, extension = os.path.splitext(filename)

      # Remove non-alphanumeric characters and replace them with a single underscore
      new_base_name = re.sub(r'\W+', '_', base_name)
      new_base_name = re.sub(r'_+', '_', new_base_name)

      # Rename the file and keep the original extension
      new_filename = f"{new_base_name}{extension}"
      os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
      print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
  # Get the directory path from command-line arguments
  if len(sys.argv) > 1:
    directory = sys.argv[1]
  else:
    directory = None

  # Call the function to rename files
  rename_files(directory)