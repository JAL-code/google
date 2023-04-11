# from collections import defaultdict

# # Define a defaultdict with a list as the default factory
# recipe_dict = defaultdict(list)

# # Add items to the dictionary
# recipe_dict['scrambled eggs'].append({'quantity': 3, 'measure': 'item', 'ingredient': 'egg'})
# recipe_dict['scrambled eggs'].append({'quantity': 1, 'measure': 'cup', 'ingredient': 'cheese'})
# recipe_dict['scrambled eggs'].append({'quantity': 1/2, 'measure': 'cup', 'ingredient': 'pepper'})

# recipe_dict['toast'].append({'quantity': 1, 'measure': 'item', 'ingredient': 'raisin toast'})
# recipe_dict['toast'].append({'quantity': 1/4, 'measure': 'tsp', 'ingredient': 'Cinnamon sugar'})

# # Print the resulting dictionary
# print(recipe_dict)

# import csv module
import csv
import os
from collections import defaultdict


def parent_directory_solo():
    # Create a relative path to the parent 
    # of the current working directory 
    relative_parent_cwd = os.getcwd()
    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent_cwd)

# setup program
print_dictionary = True
build_json = False
print_option = False

# csv file name
home_dir = parent_directory_solo()
relative_dir = "Tkinter\\DSP\\ChatAI\\"
filename = "sample_recipes.csv"
load_dir = f"{home_dir}\{relative_dir}{filename}"

recipes = defaultdict(list)

if print_option:
    # reading csv file
    with open(load_dir, 'r') as csvfile:
        # csv reader object
        csvreader = csv.DictReader(csvfile)

        # extract the data rows
        for row in csvreader:
            recipe = row['RECIPE']
            quantity = float(row['QUANTITY'])
            measure = row['MEASURE']
            ingredient = row['INGREDIENT']
            recipes[recipe].append({'quantity': quantity, 'measure': measure, 'ingredient': ingredient})

        # get total number of rows
        print("Total no. of rows: %d"%(csvreader.line_num))
else:
    # read in the CSV file and populate the defaultdict
    with open(load_dir, 'r') as csvfile:
        for line in csvfile:
            recipe, quantity, measure, ingredient = line.strip().split(',')
            recipes[recipe].append({'quantity': quantity, 'measure': measure, 'ingredient': ingredient})

recipes_dict = dict(recipes)

if print_dictionary:
    print(f"Original {type(recipes)}, Dict {type(recipes_dict)}")
    print(recipes_dict)

# build json file