#! /usr/bin/env python3

from changeImage import get_image_loc
import mimetypes
import os
from PIL import Image
import requests
from supplier_image_upload import set_url

# The following are stages to debug the code
# Check the folder for text files
STAGE_ONE = True
# Process the files
STAGE_TWO = True
# Post the reveiws to the team site
STAGE_THREE = True
# Print the output of selected variables
VERBOSE = True

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
    """ Upload the descriptions to the website """
    # Allows the user to process files at other folders.
    dup_folder = get_temp_location_for_code()
    user_path = get_image_loc('descriptions')
    if VERBOSE:
        print(dup_folder)
    if STAGE_ONE:
        url = set_url('descriptions')
        data = os.listdir(user_path)
        data.sort()
    if VERBOSE:
        print(data)
    for review in data:
        if '.' in review and STAGE_TWO:
            source = "{}/{}".format(user_path, review)
            print(review.split("."))
            reference = "{}.jpeg".format(review.split(".")[0])
            try:
                file = open("{}/{}".format(user_path, review), "r")
            except os.error:
                print("File {} can not be opened.".format(review))
            lines = file.readlines()
            if VERBOSE:
                print("Lines:\n {}".format(lines))
                print("Review: {}".format(reference))
            count = 0
            for line in lines:
                lines[count] = line.replace("\n", '')
                count += 1
            temp_dict = dict(name=lines[0].replace("\n", ""),
                            weight=int(lines[1].replace(" lbs", "").replace("\n", "")),
                            description=lines[2].replace("\n", ""),
                            image_name=reference)
            if VERBOSE:
                print(temp_dict)
            if STAGE_THREE:
                print("Posting to {}".format(url))
                response = requests.post(url, json=temp_dict)
                if not response.ok:
                    print("Error: {response.status_code}".format())

if __name__ == "__main__":
    main()