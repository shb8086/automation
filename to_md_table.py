import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

def create_markdown_table(data):
  """
  Convert a DataFrame to a Markdown table with centered alignment.

  Parameters:
  - data (dict): A dictionary containing the data for the DataFrame.

  Returns:
  - markdown_table (str): The Markdown table as a string.
  """
  # Creating DataFrame
  df = pd.DataFrame(data)

  # Convert DataFrame to Markdown table with centered alignment
  markdown_table = tabulate(df, headers='keys', tablefmt='pipe').split('\n')
  markdown_table.insert(1, '|:-:|' + '|'.join([':-:'] * (len(df.columns))) + '|')

  return '\n'.join(markdown_table)

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
