#! /usr/bin/env python3

from changeImage import get_image_loc
import mimetypes
import os
from PIL import Image
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

def set_url(get_url):
    url_address = "35.193.89.63"
    url_image = 'http://{}/upload/'.format(url_address)
    url_des = 'http://{}/fruits/'.format(url_address)
    if get_url == 'images':
        return url_image
    if get_url == 'descriptions':
        return url_des
    return url_address

def get_temp_location_for_code():
    temp_location = __file__
    return os.path.split(temp_location)[0]

def verify_jpeg(file, source):
    """ is it a jpeg? """
    with Image.open(source) as im:
        if VERBOSE:
            print(file, im.format, f"{im.size}x{im.mode}")
    if im.format == "JPEG":
        return True
    return False

def main():
    """ Upload the jpegs to the website """
    # Allows the user to process files at other folders.
    dup_folder = get_temp_location_for_code()
    user_path = get_image_loc('images')
    if VERBOSE:
        print(user_path)
        print(dup_folder)
    if STAGE_ONE:
        url = set_url('images')
        data = os.listdir(user_path)
        data.sort()
    if VERBOSE:
        print(data)
    for review in data:
        source = "{}{}".format(user_path, review)
        real_pic = verify_jpeg(review, source)
        if VERBOSE:
            print(source)
        if not '.tiff' in review and not '.png' in review and STAGE_TWO:
            print("We can load it!")
            try:
                with open(source, 'rb') as opened:
                    if VERBOSE:
                        print("Opened file: {}{}".format(user_path, opened))
                    if STAGE_THREE and real_pic:
                        print("Posting to {}".format(url))
                        r = requests.post(url, files={'file': opened})
                        if not response.ok:
                            print("Error: {}".format(r.status_code))
            except os.error:
                print("File {} can not be opened.".format(opened))

if __name__ == "__main__":
    """ Run the main program. """
    main()