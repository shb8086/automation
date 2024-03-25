#!/bin/bash
##############################################################################
# @file        single_user_config.sh
# @brief       Script to create a user account, set up SSH access with provided key file,
#              and option of granting sudo privileges based on the Linux distribution.
# @author      Shima Bani
# @date        January 9, 2024
# @email       baniadam.shima@gmail.com
# @platform    Tested on Red Hat and Debian
#
# @details     This script creates a user account, sets up SSH access with
#              provided key file, and grants sudo privileges based on the Linux
#              distribution (Red Hat or Debian).
#
#              IMPORTANT: Make sure to run this script with sudo privileges.
#
# @note        Usage: ./single_user_config.sh <username> <path_to_ssh_key> [sudo]
##############################################################################

if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
    echo "Usage: $0 <username> <path_to_ssh_key> [sudo]"
    exit 1
fi

username="$1"
ssh_key_path="$2"
grant_sudo=false

if [ "$#" -eq 3 ] && [ "$3" == "sudo" ]; then
    grant_sudo=true
fi

# Create user account and set password (if not using SSH keys)
if [ -n "$username" ]; then
    # Create user account on Red Hat
    if [ -f /etc/redhat-release ]; then
        sudo useradd "$username"
        sudo passwd "$username"
    # Create user account on Debian
    elif [ -f /etc/debian_version ]; then
        sudo adduser "$username"
    else
        echo "Unsupported distribution. Please create the user manually."
        exit 1
    fi

    # Set up SSH access with provided key file
    if [ -n "$ssh_key_path" ] && [ -f "$ssh_key_path" ]; then
        sudo su "$username" -c "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cp \"$ssh_key_path\" ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
    else
        echo "Error: SSH key file not found. Please provide a valid path."
        exit 1
    fi
else
    echo "Error: Username not provided. Please set the 'username' variable."
    exit 1
fi

# Grant sudo privileges if requested
if $grant_sudo; then
    echo "Granting sudo privileges..."
    # Check group name for sudo access
    sudo_group_name=$(sudo grep -Po '^sudo\S*\s+\K(\S+)' /etc/sudoers /etc/sudoers.d/* | uniq)
    if [ -n "$sudo_group_name" ]; then
        # Add user to sudo group
        sudo usermod -aG "$sudo_group_name" "$username"
        # Check if user is in sudo group
        groups "$username"
    else
        echo "Error: Unable to determine sudo group. Please check sudo configuration."
        exit 1
    fi
fi