#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

def callback():
    print('In the callback')

ttk.Button(root, text = "Click Me!", command = callback).pack()

root.mainloop()
