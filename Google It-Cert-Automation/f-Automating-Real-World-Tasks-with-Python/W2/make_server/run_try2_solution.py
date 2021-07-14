#! /usr/bin/env python3
# By JAL

import os
import requests

# The following are stages to debug the code
# Check the folder for text files
STAGE_ONE = True
# Process the files
STAGE_TWO = True
# Post the reveiws to the team site
STAGE_THREE = True
# Print the output of selected variables
VERBOSE = True

access_area = os.getcwd()
url_address = "35.193.89.63"
web_address = 'http://{}/feedback/'.format(url_address)

def get_temp_location_for_code():
    temp_location = __file__
    return os.path.split(temp_location)[0]

# Allows the user to process files at other folders.
dup_folder = get_temp_location_for_code()
user_path = "/data/feedback"

if VERBOSE:
    print(web_address)
    print(access_area)
    print(dup_folder)

if STAGE_ONE:
    data = os.listdir(user_path)
    data.sort()

for review in data:
    if '.' in review and STAGE_TWO:
        source = "{}/{}".format(user_path, review)
        try:
            file = open("{}/{}".format(user_path, review), "r")
        except os.error:
            print("File {} can not be opened.".format(review))
        lines = file.readlines()
        if VERBOSE:
            print("Lines:\n {}".format(lines))
        count = 0
        for line in lines:
            lines[count] = line.replace("\n", '')
            count += 1
        temp_dict = dict(title=lines[0],
                         name=lines[1],
                         date=lines[2],
                         feedback=lines[3])
        if VERBOSE:
            print(temp_dict)
        if STAGE_THREE:
            print("Posting to {}".format(web_address))
            response = requests.post(web_address, json=temp_dict)
            if not response.ok:
                print("Error: {response.status_code}".format())