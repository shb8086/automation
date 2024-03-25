import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import csv

def create_md_table_from_text(text_file):
  with open(text_file, 'r') as file:
    lines = file.readlines()
    data = [line.split() for line in lines]
  return create_md_table(data)

def create_md_table_from_csv(csv_file):
  with open(csv_file, 'r', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)
  return create_md_table(data)

def create_md_table(data):
  # Calculate column widths
  col_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

  # Generate Markdown table
  md_table = "| " + " | ".join(data[0]) + " |\n"
  md_table += "| " + " | ".join("-" * width for width in col_widths) + " |\n"

  for row in data[1:]:
      md_table += "| " + " | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(data[0]))) + " |\n"

  return md_table

def save_markdown_table(data, filepath):
  """
  Convert a DataFrame to a Markdown table and save it to a file.

  Parameters:
  - data (dict): A dictionary containing the data for the DataFrame.
  - filepath (str): The path to the file where the Markdown table will be saved.
  """
  # Creating DataFrame
  df = pd.DataFrame(data)

  # Convert DataFrame to Markdown table with centered alignment
  markdown_table = tabulate(df, headers='keys', tablefmt='pipe').split('\n')
  markdown_table.insert(1, '|:-:|' + '|'.join([':-:'] * (len(df.columns))) + '|')

  # Save Markdown table to a file
  with open(filepath, 'w') as f:
    f.write('\n'.join(markdown_table))

def plot_and_save_table(data, filepath):
  """
  Plot a DataFrame as a table and save it as a PNG image.

  Parameters:
  - data (dict): A dictionary containing the data for the DataFrame.
  - filepath (str): The path to the file where the PNG image will be saved.
  """
  # Creating DataFrame
  df = pd.DataFrame(data)

  # Plot the table and save as PNG
  plt.figure(figsize=(10, 5))
  plt.table(cellText=df.values, colLabels=df.columns, loc='center')
  plt.axis('off')
  plt.savefig(filepath, bbox_inches='tight', pad_inches=0.1)


if __name__ == "__main__":
  import sys

  if len(sys.argv) != 3:
    print("Usage: python to_md_table.py <input_file_name_ext> <output_file_name>")
    sys.exit(1)
    
  input_file = sys.argv[1]
  output_file = sys.argv[2]+".md"
    
  # Create a Markdown table from the input file
  # Check the file extension to determine the file format
  # Supported formats are .txt and .csv
  if input_file.endswith('.txt'):
    md_table = create_md_table_from_text(input_file)
  elif input_file.endswith('.csv'):
    md_table = create_md_table_from_csv(input_file)
  else:
    print("Unsupported file format. Supported formats are .txt and .csv")
    sys.exit(1)

  # print(md_table)

  # Save the Markdown table to a file
  with open(output_file, 'w') as file:
    file.write(md_table)