#! /usr/bin/env python3
# By Joseph Leffek

import os
import requests

STAGE_ONE = True
STAGE_TWO = True
STAGE_THREE = False
VERBOSE = True

access_area = os.getcwd()
if VERBOSE:
    print(access_area)
    user_path = "/data/feedback"

if STAGE_ONE:
    data = os.listdir(user_path)
    data.sort()
    build_reviews = []

for review in data:
    if '.' in review and STAGE_TWO:
        try:
            file = open(f"{user_path}/{review}", "r")
        except OSERROR:
            print(f"File {review} can not be opened.")
        lines = file.readlines()
        if VERBOSE:
            print(f"Lines:\n {lines}")
        count = 0
        for line in lines:
            lines[count] = line.replace("\n", '')
            count += 1        
        temp_dict = dict(title=lines[0], name=lines[1], date=lines[2], feedback=lines[3])
        if VERBOSE:
            print(temp_dict)
        build_reviews.append(temp_dict)

if STAGE_THREE:
        if VERBOSE:
            print(build_reviews)
        request = requests.post('http://34.123.192.178/feedback/', data = build_reviews)
        if not request.ok:
            print(f"Error: {response.status_code}")

