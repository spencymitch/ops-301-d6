#!bin/bash

# Script: Ops 301 Class 03 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 3/15/23
# Purpose: Change permissions of  a directory

# enter directory path
read -p "Enter directory path: " directory

# enter permission number
read -p "Enter permission number: " permission

# navigate to directory
cd "$directory"

# change permissions of all files in directory
chmod -R "$permission" .

# Print directory contents and new permissions settings
ls -l "$directory"