import os
import os.path

def get_location_for_code():
    # :releative location
    access_area = '/home/joseph/Desktop'
    # access_area = os.getcwd()
    return access_area

def select_case():
    case = 4
    return case

home_address = get_location_for_code()
case = select_case()

os.walk(home_address).next()[0] # returns 'C:\dir1\dir2\startdir'
os.walk(home_address).next()[1] # returns all the dirs in 'C:\dir1\dir2\startdir'
os.walk(home_address).next()[2]
