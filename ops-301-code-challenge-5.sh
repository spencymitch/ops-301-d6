#!bin/bash

# Script: Ops 301 Class 05 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 3/17/23
# Purpose: Print to the screen the file size of the log files before compression,
# Compress the contents of the log files listed below to a backup directory
# The file name should contain a time stamp with the following format
# Clear the contents of the log file
# Print to screen the file size of the compressed file
# Compare the size of the compressed files to the size of the original log files
# references used are chatgpt, and marco aliaga. 


FILES="/var/log/syslog /var/log/wtmp"
BACKUP_DIR="/var/log/backups"
TS=$(date +%Y%m%d%H%M%S)

# Zip must be installed with correct permissions for this script to work.

for f in $FILES; do
  s=$(du -h $f | awk '{print $1}')
  z=$BACKUP_DIR/$(basename $f)-$TS.zip
  zip -q $z $f && echo "" > $f && echo "$f size: $s compressed: $(du -h $z | awk '{print $1}')"
done