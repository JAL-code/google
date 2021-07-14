#! /usr/bin/env python3
# By xxxx

import json
import os
import requests

STAGE_ONE = True
STAGE_TWO = True
STAGE_THREE = False
VERBOSE = False

build_reviews = []

access_area = os.getcwd()
if VERBOSE:
    print(access_area)
user_path = os.path.expanduser("/home/joseph/google/Google It-Cert-Automation/f-Automating-Real-World-Tasks-with-Python/W2/make_server/data/feedback")

if STAGE_ONE:
    data = os.listdir(user_path)
    print(data)
    data.sort()

for review in data:
    if '.' in review and STAGE_TWO:
        source = "{}/{}".format(user_path, review)
        try:
            file = open(source, "r")
        except OSERROR:
            print("File {} can not be opened.".format(review))
        lines = file.readlines()
        if VERBOSE:
            print("Lines:\n {}".format(lines))
        count = 0
        for line in lines:
            lines[count] = line.replace("\n", '')
            count += 1
        temp_dict = dict(title=lines[0], name=lines[1], date=lines[2], feedback=lines[3])
        if VERBOSE:
            print(temp_dict)
        build_reviews.append(temp_dict)

if VERBOSE:
    print(build_reviews)

if STAGE_THREE:
    response = requests.post('http://34.122.59.223/feedback/', json=build_reviews)
    print(response.ok)
    if response.ok:
        print("Feedback uploaded!")
    if not response.ok:
        print("Error: {}".format(response.status_code))
