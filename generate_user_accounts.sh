#!/bin/bash

##############################################################################
# @file        generate_user_accounts.sh
# @brief       Script to generate and add a user with a securely hashed password to a Linux system.
# @author      Shima Bani
# @date        January 10, 2024
# @email       baniadam.shima@gmail.com
# @platform    Tested on Ubuntu
#
# @details     This script generates a specified number of user accounts with
#              securely hashed passwords, add them to the Linux system, and
#              saves the usernames and passwords to a CSV file.
#
#              IMPORTANT: Ensure that you run this script with root privileges.
#
# @note        Usage: ./generate_user_accounts.sh <number_of_accounts> <username_prefix>
#
# @example     After running the script with: ./generate_user_accounts.sh 3 myprefix
#              The created user accounts will be saved in 'user_accounts.csv' as follows:
#              Username,Password
#              myprefix_00,GhTb3kD8
#              myprefix_01,fE5nZpQ2
#              myprefix_02,jR9aS6pQ
##############################################################################

# Check if the script is executed with root privileges
if [ $(id -u) -eq 0 ]; then
  # Check if the number of accounts and username prefix arguments are provided
  if [ "$#" -eq 2 ]; then
    # Get the number of accounts and username prefix from the command line arguments
    num_accounts=$1
    username_prefix=$2

    # Set the range for user accounts
    min_std=0
    max_std=$((num_accounts - 1))

    # Set the destination directory for saving usernames and passwords
    destdir=./user_accounts.csv

    # Set the characters allowed in the password
    chars=abcdefghijklmnopqrstuvwxyz0123456789

    # Create or overwrite the CSV file with header
    echo "Username,Password" > "$destdir"

    for usr in $(seq -w ${min_std} ${max_std}); do
      # Generate username
      username="${username_prefix}_${usr}"
      # Generate a random password
      password=""
      for i in {1..8}; do
          password+="${chars:RANDOM%${#chars}:1}"
      done

      # Add generated username to the system
      egrep "^$username" /etc/passwd >/dev/null
      if [ $? -eq 0 ]; then
        echo "$username exists!"
        exit 1
      else
        # Use openssl to hash the password
        pass=$(openssl passwd -6 "$password")
        useradd -m -p "$pass" "$username"
        [ $? -eq 0 ] && echo "User has been added to the system!" || echo "Failed to add a user!"
        # Append username and password to the CSV file
        echo "$username,$password" >> "$destdir"
      fi
    done
  else
    echo "Usage: $0 <number_of_accounts> <username_prefix>"
    exit 3
  fi
else
  echo "Only root can add a user to the system."
  exit 2
fi
