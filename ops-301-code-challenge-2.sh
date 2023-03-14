#!bin/bash

# Script: Ops 301 Class 02 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 3/14/23
# Purpose: 

# Set variable
file="syslog_$(date +%Y-%m-%d_%H:%M:%S).log"


# Copy syslog to the current working directory with new filename
cp /var/log/syslog "$file"


# File name changed message
echo "The syslog file name has been changed to todays date."