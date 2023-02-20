# This file is updated for use with Windows OS
# #* is original content (see p)

import os

# #* os.listdir("website")
# #*dir = "website"
dir = os.getcwd()
os.listdir(dir)

for name in os.listdir(dir):
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))