#!/usr/bin/env python3

# Script: Ops 301 Class 10 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 3/24/23
# Purpose: Using file handling commands, create a Python script that creates a new .txt file,
# appends three lines, prints to the screen the first line, then deletes the .txt file.


import os

# Create a new text file called "example.txt" in the current directory
with open("example.txt", "w") as f:
    # Append three lines
    f.write("This is line 1.\n")
    f.write("This is line 2.\n")
    f.write("This is line 3.\n")

# read the first line
with open("example.txt", "r") as f:
    print(f.readline())

# delete the file
os.remove("example.txt")