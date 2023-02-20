#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
import os
import json 
import get_text

# example building dictionary of lists
class ItemLocation:
  stock={ 'id': [],'aisle': [],'bay' :[], 'bin':[]}
  def __init__(self,name):
    aisle = ""
    bay = ""
    bin = 0
    self.id = name
  def add_location(self, name, aisle, bay, bin):
    ItemLocation.stock['id'].append(self.id)
    ItemLocation.stock['aisle'].append(self.aisle)
    ItemLocation.stock['bay'].append(self.bay)
    ItemLocation.stock['bin'].append(self.bin)

# example building dictionary of one item
class Stock_items:
    def __init__(self):
        self.stock = {}
    def add_package(self, id, aisle, bay, bin):
        self.stock[id.name] = id
        self.stock[id.name] = id
        self.stock[id.name] = id
        self.stock[id.name] = id

# If line 2 works delete the following commented block
""" # check unicode
def check_unicode():
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str
    return to_unicode """

# save the list of products
def save_data(file_name, data):
    # , encoding='utf8 ' replaced by 2nd line
    with io.open (file_name, 'w') as outfile:  
        str_ =json.dumps(data, indent=4, sort_keys=False, separators=(',',': '), ensure_ascii=False)
        outfile.write(str_)

# load the list of products
def load_products(file_name):
    print("Loading the products")
    # , encoding='utf8 ' replaced by 2nd line
    with open(file_name, 'r' , encoding='utf8') as data_file:  
        data_loaded = json.load(data_file)
    return data_loaded

def create_default_item(test):
    default_item = {}
    return default_item

# make sure the saved data is the same as the loaded data
def verify_data(saved, loaded):
    print(saved == loaded)

def file_exists(filename, location):
    f_exists = False
    if not os.path.exists(filename):
        f_exists=False
        print(f"File {filename} does not exist!")
    else:
        print(f"Error, file {filename} already exists!")
        f_exists=True
        # sys.exit(1)
    return f_exists

if __name__ == '__main__':
    # set the file name
    file_name='store_items.json'
    working_dir = os.getcwd()
    relative_location = f"\\supermarket\\"
    # does this file exist the working folder
    default_folder = f"{working_dir}{relative_location}"
    print(f"{default_folder}{file_name}")
    if file_exists(file_name, default_folder):
        print("We can load the data!")
    if file_exists(file_name, default_folder)==False:
        print("We must create a default file!")


# make sure the saved data is the same as the loaded data
def verify_data(saved, loaded):
    print(saved == loaded)

def file_exists(filename, location):
    print("Checking for json file")
    if os.path.exists(f"{location}{filename}.json"):
        print(f"File {location}{filename}.json already exists!")
    else:
        rebuild_default(file_name, default_folder)
        print(f"Created default file.")
        # sys.exit(1)


def rebuild_default(file_name, relative_location): 
    """ Start the program to parse text file into
        types of text components """
    print("Building default file")
    # File Name
    fname_load = "create_default"
    # FileNotFoundError example
    # folder and file location for text to load
    fname = f"{relative_location}{fname_load}.txt"
    fname_base = os.path.basename(fname)
    file_name_split = os.path.splitext(fname_base)
    print(f"Name: {file_name}, Create Extension: {file_name_split[1]}, Create File Name: {file_name_split[0]}")
    # folder where to save output
    datasave = f"{relative_location}{file_name}.json"
    # Load the data.
    loaded_text = get_text.count_words(fname)
    # Initialize the dictionary for storage of data.
    breakdown, list_of_products = get_text.init_processed_data()
    print(breakdown)
    print(list_of_products)
    
    # Process the data for primary verses
    dataset = get_text.regex_iter(loaded_text, breakdown, list_of_products, file_name)
    # for v in dataset:
        # print(v)
    get_text.save_list_of_items(dataset, datasave)
    print(f"Save file: {file_name[0]}") 

def end_program(endprogram):
    pass
    return endprogram

def add_item(endprogram):
    print("Add item")
    return endprogram

def delete_item(endprogram):
    print("Delete item")
    return endprogram

def remove_item(endprogram):
    print("Remove list")
    return endprogram

def print_items(endprogram):
    print("Print items")
    return endprogram

if __name__ == '__main__':
    print("Starting ... ")
    # set the file name
    file_name='products'
    working_dir = os.getcwd()
    relative_location = f"\\supermarket\\"
    # does this file exist the working folder
    default_folder = f"{working_dir}{relative_location}"
    print(f"{default_folder}{file_name}.json")
    file_exists(file_name, default_folder)
    print("Load data")
    saved_data = f"{default_folder}{file_name}.json"
    print(saved_data)
    products = load_products(saved_data)
    print(products)
    endprogram = 's'
    while endprogram != 0:
        print("Add item (a), Delete item (d), Review list (r), Top stock (t), Exit (exit)?")
        endprogram = input("Action? ")
        match endprogram:
            case 'exit':
                end_program(endprogram)
                break
            case 'a':
                add_item(endprogram)
            case 'd':
                delete_item(endprogram)
            case 'r':
                remove_item(endprogram)
            case 't':
                print_items(endprogram)