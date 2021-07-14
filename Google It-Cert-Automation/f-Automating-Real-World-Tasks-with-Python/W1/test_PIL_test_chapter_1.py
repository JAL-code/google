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
    print("Roots:\n")
    print(root)
    print("Dirs:\n")
    print(dirs)
    print("files:\n")
    print(files)
    if case == 1:
        new_im = im.resize((640,480))
        new_address = f"./example_resized.png"
        new_im.save(new_address)
    if case == 2:
        new_im = im.rotate(90)
        new_address = f"./example_rotated.png"
        new_im.save(new_address)
    if case == 3:
        im.rotate(180).resize((640,480)).save("flipped_and_resized.png")

