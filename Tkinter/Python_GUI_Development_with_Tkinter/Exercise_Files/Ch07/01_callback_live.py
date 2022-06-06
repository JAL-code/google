#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Callbacks only available for specific actions.
# Tkinter can bind to events with specific handlers
# This exercise focuses on callbacks.

from tkinter import *
from tkinter import ttk        
    
root = Tk()
# Command callbacks functions: Button, Checkbutton, Radiobutton, Spinbox, Scale, Scrollbar
def callback(number):
    print(f'In the callback {number}')

# Lambda keyword creates an anonymous function that contains the callback method.
ttk.Button(root, text = "Click Me 1", command = lambda: callback(1)).pack()
ttk.Button(root, text = "Click Me 2", command = lambda: callback(2)).pack()
ttk.Button(root, text = "Click Me 3", command = lambda: callback(3)).pack()

root.mainloop()
