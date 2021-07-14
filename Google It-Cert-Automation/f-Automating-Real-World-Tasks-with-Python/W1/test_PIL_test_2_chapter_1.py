import os
from PIL import Image
from os.path import join, getsize

def get_location_for_code():
    # :releative location
    access_area = '/home/joseph/Desktop/STC'
    # access_area = os.getcwd()
    return access_area

def select_case():
    case = 4
    return case

home_address = get_location_for_code()
address = f"./example.png"
# print(address)
# im = Image.open(address)
case = select_case()

for root, dirs, files in os.walk(home_address):
    # print(root, "consumes", end=" ")
    # print((join(root, name) for file in files), end=" ")
    # print("bytes in", len(files), "non-directory files")
    for file in files:
        if file.endswith(".png"):
            print(os.path.join(root,file))
        if file.endswith(".gif"):
            print(os.path.join(root,file))
        if file.endswith(".jpg"):
            print(os.path.join(root,file))
        if file.endswith(".bmp"):
            print(os.path.join(root,file))

