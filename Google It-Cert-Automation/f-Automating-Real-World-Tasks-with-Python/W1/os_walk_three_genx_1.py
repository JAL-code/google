import os
import os.path

def get_location_for_code():
    # :releative location
    access_area = '/home/joseph/Desktop/STC'
    # access_area = os.getcwd()
    return access_area

def select_case():
    case = 4
    return case
print(f"Home Path: {os.getcwd()}")
home_address = get_location_for_code()
print(home_address)

for path, directories, files in os.walk(home_address):
    if file in files:
        print('found %s' % os.path.join(path, file))
