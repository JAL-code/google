import os
from PIL import Image


def get_location_for_code():
    # :releative location
    # access_area = 'files_and_exceptions/'
    access_area = os.getcwd()
    return access_area

def select_case():
    case = 3
    return case


home_address = get_location_for_code()
address = f"./example.png"
print(address)
im = Image.open(address)
case = select_case()
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
