#!/bin/bash

# Prompt user for directory path
read -p "Enter directory path: " directory

# Prompt user for permission number
read -p "Enter permission number: " permission

# Navigate to directory
cd "$directory"

# Change permissions of all files in directory
chmod -R "$permission" .

# Print directory contents and new permissions settings
ls -l "$directory"