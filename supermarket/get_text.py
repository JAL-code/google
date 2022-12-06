#!/usr/bin/env python3
# Code by JAL-code
# Process the document for supermarket items.
# Note this file is stage 2 for converting word files to python dictionary of supermarket items.
# This file parses the text output of notepad file to a json file.

import os
import re 
import sys
import json

# SILENTMODE - should the user know if the file was found?
SILENTMODE = False
# SHOWCOUNT - should the user see how many words loaded?
SHOWCOUNT = True

def checkErrors():
    print("Checking")
    # bad primary text
    # BBBB CCC:(.)+VVV
    # Back slash Characters "\"    
    # \f      Form feed is a page-breaking ASCII control character.  print('\f',end='')
    # \n      New Line
    # \'      Single quote
    # \"      Double quote
    # \\      backslash
    # \r      Carriage Return
    # \t      Horizontal tab
    # \b      Backspace
    # \f      form feed
    # \v      vertical tab
    # \0      Null character
    # Unicode Character with 16-bit hex value XXXX
    # \ufeff
    # \u00a0  NO-BREAK SPACE
    # \u201b  SINGLE HIGH-REVERSED-9 QUOTATION MARK
    # \u201c  LEFT DOUBLE QUOTATION MARK
    # \u201d  RIGHT DOUBLE QUOTATION MARK
    # \u2014  — EM DASH
    # \u2026  HORIZONTAL ELLIPSIS
    # \u2018  LEFT SINGLE QUOTATION MARK
    # \u2019  RIGHT SINGLE QUOTATION MARK

def init_processed_data():
    next_record_id = set_record_number()
    new_saved_dictionary = {}
    # key = default, saves default data type.
    # item_num: set the store item id for the current item being loaded.
    # aisle_loc: what isle is the item id placed
    # bay_loc: what bay is the item id placed
    # bin_loc: what bin is the item id placed
    # item_price: price of item
    # item_save: name of file saved in program filename

    default_record = {
        'item_num': next_record_id,
        'aisle_loc': 1,
        'bay_loc': 1,
        'bin_loc': 0,
        'item_price': '$0.00',
        'item_save': "",
    }

    new_saved_dictionary.update(default_record)
    supermarket_items = []
    # print(f"Default dictionary ready: {new_saved_dictionary}")
    return new_saved_dictionary, supermarket_items

def set_record_number():
    """ Set the record number for the document being processed. """
    item_record_number = 1
    return item_record_number

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        if SILENTMODE:
            pass # Pass lets the error fail silently.
                 # Pass also acts as a placeholder for future changes.
        # Remove pass to allow printing the error.
        else:
            print(f"Sorry, the file {filename} does not exist.")
    # Move file into same location to split the file text.
    else:
        if SHOWCOUNT:
            # Count the number of words in the title.
            words = contents.split()
            num_words = len(words)
            print(f"The file {filename} contains {num_words}.")
            print(contents)
        return contents

def create_dict_item(item_id, 
                     aisle, 
                     bay, 
                     bin, 
                     price,
                     filename):
    mid_dict = dict(item_num=item_id, 
                    aisle_loc=aisle, 
                    bay_loc=bay, 
                    bin_loc=bin, 
                    item_price=price,
                    item_save=filename)
    return mid_dict

def regex_iter(text_for_scan, dict_storage, canonical_study, file_text):
    print("Looking for supermarket item details.")
    print_text_capture = False
    cpattern = re.compile(r"""
        ^I(?P<item_num>[\w]+),|
        A(?P<aisle_loc>[\d]{1,3}),|
        B(?P<bay_loc>[\d]{1,2}),|
        BI(?P<bin_loc>[\d]{1,2}),|
        (?P<item_price>\$[\d]{1,3}.[\d]{2})
        """, re.VERBOSE|re.MULTILINE)
    # default is re.finditer
    matches = re.finditer(cpattern, text_for_scan)  

    last_position = 0
    last_match = 0
    if print_text_capture:
        pass
        # print(f"Start searching the loaded data. Matches: {len(matches)}")
    filename = file_text
    matchcount = 0
    item_id = ""
    aisle = ""
    bay = ""
    bin = ""
    price = ""
    # create the compiled_array
    for matchNum, match in enumerate(matches, start=1):
        if print_text_capture:
            print(f"Match {matchNum} was found at {match.start()}-{match.end()}: {match.group()}")
        if print_text_capture:
            print(f"MatchNum: {matchNum} \nMatch: {match} \nNames:{match.groupdict()}")
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            # print(f"{groupNum} - {match.group(groupNum)}")
            if match.group(groupNum) == None:
                pass
            else:
                print(f"Group {match.lastgroup} was found at {match.start(groupNum)}-{match.end(groupNum)}: {match.group(groupNum)}")
                matchcount = matchcount + 1
                if match.lastgroup == 'item_num':
                    item_id = match.group(groupNum)
                    print(f"Item {item_id}")                    
                if match.lastgroup == 'aisle_loc':
                    aisle = match.group(groupNum)
                    print(f"Aisle {aisle}")
                if match.lastgroup == 'bay_loc':
                    bay = match.group(groupNum)
                    print(f"Bay: {bay}")
                if match.lastgroup == 'bin_loc':
                    bin = match.group(groupNum)
                    print(f"Bin: {bin}")
                if match.lastgroup == 'item_price':
                    price = match.group(groupNum)
                    print(f"Price: {price}")
                if groupNum == 5:
                    print(f"ID: {item_id} A: {aisle} B: {bay} Bin: {bin} $: {price}") 
                    temp_dict = create_dict_item(item_id, 
                                                aisle, 
                                                bay, 
                                                bin, 
                                                price,
                                                filename)
                    canonical_study.append(temp_dict)
    return canonical_study



def save_list_of_items(data, datasave):
    with open(datasave, 'w') as file:
        json.dump(data, file, indent=4)
