#! /usr/bin/env python3

import os
import requests


access_area = os.getcwd()
print(access_area)
user_path = os.path.expanduser("/home/joseph/google/Google It-Cert-Automation/f-Automating-Real-World-Tasks-with-Python/W2/make_server/data/feedback")

data = os.listdir(user_path)

data.sort()
build_reviews = []
print(data)
for review in data:
    if '.' in review:
        try:
            file = open(f"{user_path}/{review}", "r")
        except OSERROR:
            print(f"File {review} can not be opened.")
        lines = file.readlines()
        print(f"Lines:\n {lines}")
        count = 0
        for line in lines:
            lines[count] = line.replace("\n", '')
            count += 1
        temp_dict = dict(title=lines[0], name=lines[1], date=lines[2], feedback=lines[3])
        print(temp_dict)
        build_reviews.append(temp_dict)

print(build_reviews)
request = requests.post('http://34.123.192.178/feedback', data = build_reviews)

if not request.ok:
    print(f"Error: {response.status_code}")


