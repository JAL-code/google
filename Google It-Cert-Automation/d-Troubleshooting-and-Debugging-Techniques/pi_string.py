#!/usr/bin/env python3

from access import get_location_for_code
# create a module called access.py that gives the location
# for the file_reader to get this macro to run.
# Call the function: get_location_for_code()

file_path = get_location_for_code()

file_name = 'W1-Q2-NO.txt'
with open(f"{file_path}{file_name}") as file_object:
    # load the file into a list
    lines = file_object.readlines()
    print(lines)
