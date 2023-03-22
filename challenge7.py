#!/usr/bin/env python3

# Script: Ops 301 Class 07 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 3/21/23
# Purpose: Script that generates all directoreis, subdirectores and files for a user-provided directory path.

#Main
import os 

# Variable for the path
path = input("Please enter a file path\n")

# Loop containing an array using the os.walk() function

for (root, dirs, files) in os.walk(path):
    print("Root:", root)
    print("Directories: ", dirs)
    print("Files: ", files)