# Contents

- `README.md`: This file.
- `LICENSE`: License file.
- `to_md_table.py`: Python script to convert a csv/txt file to a markdown table.
- `rename_date.py`: Python script to rename files with adding the creation date to the filename.
- `rename_underline.py`: Python script to rename all the files in a directory with replacing spaces with underscores.
- `change_passwords.sh`: Script to change users' password based on a file with the format username:password.
- `generate_user_accounts.sh`: Script to generate and add a user with a securely hashed password to a Linux system.
- `single_user_config.sh`: Script to create a user account, set up SSH access, and option of granting sudo privileges based on the Linux distribution.
- `feed_catcher.py`: Script that fetches posts from your desired RSS feeds in the last 24 hours and saves the posts' title to a README.md file.


## Usage

### [to_md_table.py](to_md_table.py)

```bash
python to_md_table.py <input_file_name_ext> <output_file_name>

# Example
python to_md_table.py test.csv test

# Output
# test.md
```

### [rename_date.py](rename_date.py)

```bash
python rename_date.py <input_file_name_ext>

# Example
python rename_date.py test.pdf

# Output
# 2024_03_25_test.pdf
```

### [rename_underline.py](rename_underline.py)

```bash
python rename_underline.py [directory_path]

# Hint:
# The directory path is optional. If not provided, the current directory will be considered.

# Example
python rename_underline.py /Documents

# Output
# All the files in the directory will be renamed with replacing spaces with underscores.
```

### [change_passwords.sh](change_passwords.sh)

1. Make the script executable with the command `chmod +x change_passwords.sh`.
2. Ensure there is a file named `passwords.txt` in the same directory as the script.
3. Run the script as root with the command `sudo ./change_passwords.sh`.


### [generate_user_accounts.sh](generate_user_accounts.sh)

1. Make the script executable with the command `chmod +x generate_user_accounts.sh`.
2. Run the script as root with the command `sudo ./generate_user_accounts.sh <number_of_accounts> <username_prefix>`.
3. The created user accounts will be saved in `user_accounts.csv` as well as their passwords.


### [single_user_config.sh](single_user_config.sh)

1. Make the script executable with the command `chmod +x single_user_config.sh`.
2. Run the script as root with the command `sudo ./single_user_config.sh <username> <path_to_ssh_key> [sudo]`.

### [feed_catcher.py](feed_catcher.py)

1. Open a terminal and navigate to the directory where feed_catcher.py is saved.
2. Execute the script by running the following command in the terminal: `python ./feed_catcher.py`

