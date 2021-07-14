#!/usr/bin/env python3
# script

import os
from PIL import Image

user_path = os.path.expanduser("~")
print(user_path)
old_path = user_path + "/images/"
print(old_path)
new_path = "/opt/icons/"
for image in os.listdir(old_path):
    if '.' not in image[0]:
        img = Image.open(old_path + image).convert("RGB").rotate(-90).resize((128,128))
        jpegfilename = "{}{}".format(new_path, os.path.splitext(image)[0])
        print(jpegfilename)
        img.save(jpegfilename, 'jpeg')
        img.close()