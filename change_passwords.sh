#!/bin/bash
##############################################################################
# @file        change_passwords.sh
# @brief       Script to change user passwords based on a file with the format
#              username:password.
# @author      Shima Bani
# @date        January 9, 2024
# @email       baniadam.shima@gmail.com
# @platform    Tested on Ubuntu 20.04 LTS
#
# @details     This script reads a file containing usernames and passwords,
#              checks if the users exist, changes their passwords, and sets
#              their shell to /bin/bash.
#
#              IMPORTANT: Make sure to run this script as root!
#
# @note        You can uncomment the actual password change command
#              (echo "$username:$password" | chpasswd) to apply changes.
##############################################################################

# Specify the path to the file containing usernames and passwords
password_file="passwords.txt"

# Specify the default shell to set for users
shell="/bin/bash"

# Check if the script is executed as root
if [ "$(id -u)" -eq 0 ]; then

  # Check if the password file exists
  if [ -e "$password_file" ]; then

    # Read the password file line by line
    while IFS=: read -r username password; do

      # Check if the user already exists
      if id "$username" &>/dev/null; then

        # Change the user's password
        echo "Changing password for user $username to $password"
        # Uncomment the next line to actually change the password
        # echo "$username:$password" | chpasswd

        # Change the user's shell to /bin/bash
        sudo chsh -s "$shell" "$username"

        # Check if the shell change was successful
        if [ $? -eq 0 ]; then
          echo "Password changed for user $username."
        else
          echo "Failed to change the password for user $username."
        fi
      else
          echo "User $username does not exist, skipping."
      fi

    done < "$password_file"

  else
    echo "Error: The '$password_file' file does not exist."
  fi

else
  echo "Error: Only root can change user passwords."
  exit 2
fi