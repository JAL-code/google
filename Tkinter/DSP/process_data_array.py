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

# regx string
# set the regx string
def test_regex(test_data, test_line):
    regex = test_data
    result = re.search(regex, test_line)
    # print(result[1])
    return result

# Load the data
def load_data(filename):
    print("Running Main")
    test_reg = ""
    # Open the current_update.txt file
    try:
        file = open(filename)
    except OSError:
        print(f"Check Filename: {filename}")
        return None
    lines = file.readlines()
    lines.remove('\n')

    for line in lines:
        if printFileData:
            print(f"Current input: {line}")

        # Process the data
        if line[:7] == '# final':
            print(f"Assigning filter: {line[10:]}")
            test_reg = line[10:]

        if test_reg != "":
            print("Testing line")

            cpattern = re.compile(test_reg, re.VERBOSE|re.MULTILINE)
            # default is re.finditer
            matches = re.finditer(cpattern, line)  
        
            # test = test_regex(test_reg, line)
            print(f"Test: {matches}")

            for matchNum, match in enumerate(matches, start=1):
                if printCapture:
                    print(f"Match {matchNum} was found at {match.start()}-{match.end()}: {match.group()}")
                if printCapture:
                    print(f"MatchNum: {matchNum} \nMatch: {match} \nNames:{match.groupdict()}")

        # Items to look for

        # Levels and the components and buildings which can be researched.


# procedural run
def main():
    keyterm = f"{strDir}{strFolderSep}how_to_make_things.py"
    regex = []
    print(os.getcwd())
    try:
        if sys.argv[1] != "":
            print("Running terminal setup")
            if printFileData:
                print(print(os.path.exists(sys.argv[1])))
            # With correct directory selected load the data.
            load_data(sys.argv[1])
        else:
            print("Running windows setup")
            if printFileData:                
                print(os.getcwd())
                print( f"Full Path    :{strPath}" )
            strPath = os.path.realpath(__file__)
            
            load_data(keyterm)

    except IndexError:
        if printFileData: 
            print("Running with default file.")
        load_data(keyterm)

if __name__ == '__main__':
    printFileData = False
    printCapture = True
    strPath = os.path.realpath(__file__)
    strDir = os.path.dirname(__file__)    
    strBase = os.path.basename(__file__) 
    strFolderSep = os.path.sep
    if printFileData: 
        print( f"Full Path    :{strPath}" )
        print( f"Dir name     :{strDir}" ) 
        print( f"Base Name    :{strBase}" )     
        print( f"Alt Name     :{strFolderSep}")
    main()