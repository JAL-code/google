#!/usr/bin/env python3
# Line above runs program in Linux
# Overview
# Basic processing file for "how_to_make_things.py".
# Steps:
#       1. Load the data
#       2. Process the regx
#       3. Parse data to the proper matrix

import csv # read text files line by line
import sys # interact with the os
import re # Process the regx
import os # interact with the folder

'''Enter "./process_data_array.py how_to_make_things.py" at terminal.'''

# Load the data
def load_data(filename):
    print("Running Main")
    # Open the current_update.txt file
    try:
        file = open(filename)
    except OSError:
        print("Check Filename")
        return None
    lines = file.readlines()
    lines.remove('\n')

    for line in lines:
        print(line)

# Process the data
# regx string
# Items to look for

# Levels and the components and buildings which can be researched.


# procedural run
def main():
    print(os.getcwd())
    print(print(os.path.exists(sys.argv[1])))
    # With correct directory selected load the data.
    load_data(sys.argv[1])

if __name__ == '__main__':
    main()