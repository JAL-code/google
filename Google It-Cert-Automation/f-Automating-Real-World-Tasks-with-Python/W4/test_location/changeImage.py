#!/usr/bin/env python3
# script

import os
import sys
from PIL import Image

def get_image_loc(type):

    user_loc = os.path.expanduser("~")
    test_path = "{}".format(os.path.split(__file__)[0])
    relative_location =  "~"
    switch = test_path
    print(user_loc)
    print(test_path)
    print(relative_location)
    path = "{}{}{}/".format(switch,"/supplier-data/",type)
    print(path)
    return path

def main():
    loc = get_image_loc('images')
    print(loc)
    for image in os.listdir(loc):
        if '.' not in image[0]:
            file_open = "{}{}".format(loc, image)
            img = Image.open(file_open).convert("RGB").resize((600,400))
            jpegfilename = "{}{}".format(loc, os.path.splitext(image)[0])
            print(jpegfilename)
            img.save(jpegfilename, 'jpeg')
            img.close()

if __name__ == "__main__":
    main()