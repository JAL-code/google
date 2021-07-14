from PIL import Image
import os, sys
import re

print(os.getcwd())

with open("./example.png", "rb") as fp:
    im = Image.open(fp)
