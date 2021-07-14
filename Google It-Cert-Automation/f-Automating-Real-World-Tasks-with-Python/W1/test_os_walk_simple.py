import os

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


for path, dirnames, filenames in os.walk(home_address):
    print(f"{repr(path)} {repr(dirnames)} {repr(filenames)}")
