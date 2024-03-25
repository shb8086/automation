# Contents

- `README.md`: This file.
- `LICENSE`: License file.
- `to_md_table.py`: Python script to convert a csv/txt file to a markdown table.
- `rename_date.py`: Python script to rename files with adding the creation date to the filename.
- `rename_underline.py`: Python script to rename all the files in a directory with replacing spaces with underscores.


## Usage

### to_md_table.py

```bash
python to_md_table.py <input_file_name_ext> <output_file_name>

# Example
python to_md_table.py test.csv test

# Output
# test.md
```

### rename_date.py

```bash
python rename_date.py <input_file_name_ext>

# Example
python rename_date.py test.pdf

# Output
# 2024_03_25_test.pdf
```

### rename_underline.py

```bash
python rename_underline.py {directory_path}

# Hint:
# The directory path is optional. If not provided, the current directory will be considered.

# Example
python rename_underline.py /Documents

# Output
# All the files in the directory will be renamed with replacing spaces with underscores.
```
