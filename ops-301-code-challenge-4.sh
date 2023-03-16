#!bin/bash

# Script: Ops 301 Class 03 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 3/16/23
# Purpose: Create a script that launches a menu system with different options.

# loop 

while true; do
    # print menu options
    echo "Menu Options:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    # input option
    read -p "Enter option number: " option

    # options
    if [[ $option -eq 1 ]]; then
        echo "Hello world!"
    elif [[ $option -eq 2 ]]; then
        ping -c 5 192.168.0.152
    elif [[ $option -eq 3 ]]; then
        ip a
    elif [[ $option -eq 4 ]]; then
        exit 0
    else
        echo "Options are 1-4. Please try again."
    fi

done






Regenerate response