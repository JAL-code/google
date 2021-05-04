#!/usr/bin/env python3
# Code by JAL-code
# Process the lastest update and output potential terminal input.
# User to Copy/Paste to terminal.

import os
import re
import sys

'''Enter "./process_current_update.py current_update.txt" at terminal.'''

txt_file_location = sys.argv[1]
modified = []
add = []
deleted = []

# Find the line indicating change must be updated to the repo.
def find_start(lines, pattern):
    ch_recorded = False
    line_Count = 0

    for line in lines:
        result = re.search(pattern, line)
        if result is None:
            line_Count += 1
            continue
        else:
            ch_recorded = True
            break
    return line_Count, ch_recorded

# Look for modified files
def check_modified(lines):
    print("Running modified.")
    pattern = r"Changes not staged for commit:"
    limit_pattern = r"modified:   "
    line_Count, ch_mod = find_start(lines, pattern)
    print(f"{line_Count}: {ch_mod}")    

    for line in lines[line_Count+1:]:
        if re.search("^[A-Z]", line):
            break
        else:
            if re.search(r"^\t", line):
                modified.append(re.sub(limit_pattern, '', re.sub(r"\t",'', line)))
    return ch_mod

# Look for rm files
def check_deleted(lines):
    print("Running deleted.")
    pattern = r"Changes not staged for commit:"
    limit_pattern = r"deleted:    "
    line_Count, ch_mod = find_start(lines, pattern)
    print(f"{line_Count}: {ch_mod}")

    for line in lines[line_Count+1:]:
        if re.search("^[A-Z]", line):
            break
        else:
            if re.search(r"^\t", line):
                deleted.append(re.sub(limit_pattern, '', re.sub(r"\t",'', line)))
    return ch_mod

# Look for new files
def check_first_add(lines):
    ch_Untrack = False
    print("Running untracked")
    pattern = r"Untracked files:"
    line_Count, ch_Untrack = find_start(lines, pattern)

    for line in lines[line_Count+1:]:
        if re.search("^[A-Z]", line):
            break
        else:
            if re.search(r"^\t", line):
                add.append(re.sub(r"\t", '', line))
    return ch_Untrack

# Create the git command
def create_command(action, list_item):
    output = f"git {action} "
    output2 = "\" \"".join(list_item)  #keep all text for path
    return f"{output} \"{output2}\""

# Open the file and process which files need to be updated to the repo.
def main(txt_file_location):
    print("Running Main")
    # Open the current_update.txt file
    try:
        file = open(txt_file_location)
    except OSERROR:
        return None
    lines = file.readlines()
    lines.remove('\n')
    #print(lines)
    count = 0
    for line in lines:
        #print(line)
        line_r = re.sub(r"\n", "", line)
        lines[count] = line_r
        count += 1
        #print(line)
    # print(lines)
    file.close()
    # The checks to be made.
    checks = [
        (check_modified, "Modified Files found"),
        (check_first_add, "Found files to be added"),
        (check_deleted, "Found items to delete")
    ]
    

    # Run the checks
    everything_ok = True
    for check, msg in checks:
        if check(lines):
            print(msg)
            everything_ok = False

    print("\nProcessed checks")
    print("\nModified")
    print(modified)
    print("\nAdd")
    print(add)
    print("\nDeleted")
    print(deleted)

    # Print out the results
    if not everything_ok:
        print("Work to be done!")
        if modified:
            print(f"These were modified: {modified}")
            print(create_command('add', modified))
        if add:
            print(f"These are new files: {add}")
            print(create_command('add', add))
        if deleted:
            print(f"These are new files: {deleted}")
            print(create_command('rm', deleted))
    else:
        print("No GitHub updates to be pushed")

main(txt_file_location)
