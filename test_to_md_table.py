import pandas as pd
from tabulate import tabulate

def test_save_markdown_table():
    # Test case 1: Empty DataFrame
    data = {}
    filepath = 'test_table1.md'
    save_markdown_table(data, filepath)
    # Verify that the file is created and contains the expected content

    # Test case 2: DataFrame with data
    data = {'Name': ['John', 'Alice', 'Bob'], 'Age': [25, 30, 35]}
    filepath = 'test_table2.md'
    save_markdown_table(data, filepath)
    # Verify that the file is created and contains the expected content

    # Test case 3: DataFrame with special characters
    data = {'Name': ['John', 'Alice', 'Bob'], 'Age': [25, 30, 35], 'Description': ['Hello\nWorld', 'I am Alice', 'I am Bob']}
    filepath = 'test_table3.md'
    save_markdown_table(data, filepath)
    # Verify that the file is created and contains the expected content

    # Test case 4: DataFrame with empty cells
    data = {'Name': ['John', '', 'Bob'], 'Age': [25, '', 35]}
    filepath = 'test_table4.md'
    save_markdown_table(data, filepath)
    # Verify that the file is created and contains the expected content

    # Test case 5: DataFrame with different data types
    data = {'Name': ['John', 'Alice', 'Bob'], 'Age': [25, 30, 35], 'Salary': [50000.0, 60000.0, 70000.0]}
    filepath = 'test_table5.md'
    save_markdown_table(data, filepath)
    # Verify that the file is created and contains the expected content

test_save_markdown_table()