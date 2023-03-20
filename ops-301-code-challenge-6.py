#!/usr/bin/env python3

# Script: Ops 301 Class 06 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 3/20/23
# Purpose: In ubuntu, create a python script that executes a few bash commans successfully. 


# Python module "os" utilized

import os

# three variables that execute bash functions

whoami = [os.system("whoami")]
ipa = [os.system("ip a")]
lshw = [os.system("lshw -short")]

#prints defined variables to screen
print (whoami)
print (ipa)
print (lshw)