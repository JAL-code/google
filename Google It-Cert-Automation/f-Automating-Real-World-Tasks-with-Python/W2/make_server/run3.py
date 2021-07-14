#!/usr/bin/env python3

import os
import requests

path = '/data/feedback/'
file_list = os.listdir(path)
file_list.sort()

def read_file(file):
    with open (path + file) as f:
        list = []
        dict = {}
        list = f.read().splitlines()
        dict['title'] = list[0]
        dict['name'] = list[1]
        dict['date'] = list[2]
        dict['feedback'] = list[3]
    return dict

def main():
    for file in file_list:
        p = read_file(file)
        response = requests.post("http://35.193.74.73/feedback", json=p)
        print(response.status_code)

if __name__ == "__main__":
    main()
