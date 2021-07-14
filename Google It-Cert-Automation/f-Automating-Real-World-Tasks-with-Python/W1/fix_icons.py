import os
from os import mkdir, walk
from PIL import Image
from os.path import join, split

def get_location_for_code():
    # :releative location
    access_area = '/home/joseph/Desktop/STC'
    last_folder = 'STC'
    return access_area, last_folder

def get_temp_location_for_code():
    temp_location = __file__
    return os.path.split(temp_location)[0]

def select_case(ext):
    case = ['.png','.gif','.jpg','.bmp']
    if ext in case:
        return True
    return False

def search_directory(home_address, rel_folder):
    verb1, show_temp, make_copy = debug()
    """Get the graphic files and duplicate them to the
    same directory as the script"""
    # Source folders to be copied to this new folder 
    # at same directory for this script.
    dup_folder = get_temp_location_for_code()
    if verb1:
        print(f"Temp location: {dup_folder}")
    # Count the files, graphic files and directories.
    file_check = 0
    graphic_check = 0
    directory_check = 0
    # walk through the directory
    for root, dirs, files in os.walk(home_address):
        directory_check += 1
        if verb1:
            print(f"D:{directory_check}, F:{file_check}")
        for file in files:
            # get the file and convert it to file and file ext.
            found_file = os.path.splitext(file)
            # the file directory and remove home_address
            diff_folder = os.path.join(root,file).replace(home_address,"")
            add_folder = os.path.split(diff_folder)[0]
            # create new test folder 
            copy_location = f"{dup_folder}/{rel_folder}{add_folder}"
            if show_temp:
                print(f"Copy To: {copy_location}")
            try:
                 os.mkdir(copy_location)
                 if verb1:
                     print("Folder created")
            except Exception:
                if verb1:
                    print("Folder already made.")
            file_check += 1
            if select_case(found_file[1]):
                if verb1:
                    print(f"{found_file}: Check:\n {select_case(found_file[1])}")
                im = Image.open(os.path.join(root,file))
                os.path.join(root,file)
                new_im = im.resize((640,480))
                new_im = im.rotate(90)
                new_im.save(os.path.join(copy_location,f"{found_file[0]}_temp{found_file[1]}"))
                graphic_check += 1
                # if verb1:
                print(os.path.join(root,file))
    print(f"D:{directory_check}, F:{file_check}, G:{graphic_check}")
    

def copy_dir_if_graphic_file_found():
    pass

def debug():
    verbose_state_1 = False
    show_temp_location = False
    copy_file = False
    return verbose_state_1, show_temp_location, copy_file    

home_address, rel_folder = get_location_for_code()
search_directory(home_address, rel_folder)




