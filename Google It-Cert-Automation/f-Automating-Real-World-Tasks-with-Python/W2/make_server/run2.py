#! /usr/bin/env python3
# By Joseph Leffek

import os
import requests

STAGE_ONE = True
STAGE_TWO = True
STAGE_THREE = False
VERBOSE = True

access_area = os.getcwd()
url_address = "99.99.999.99"
web_address = 'http://{}/feedback/'.format(url_address)

def get_temp_location_for_code():
    temp_location = __file__
    return os.path.split(temp_location)[0]

if VERBOSE:
    print(web_address)
    print(access_area)
    dup_folder = get_temp_location_for_code()
    print(dup_folder)
    user_path = "{}/data/feedback".format(dup_folder)

if STAGE_ONE:
    data = os.listdir(user_path)
    data.sort()

for review in data:
    if '.' in review and STAGE_TWO:
        source = "{}/{}".format(user_path, review)
        try:
            file = open(f"{user_path}/{review}", "r")
        except OSError:
            print("File {} cannot be opened.".format(review))
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
            response = requests.post(web_address, json=build_reviews)
            if not response.ok:
                print("Error: {response.status_code}".format())