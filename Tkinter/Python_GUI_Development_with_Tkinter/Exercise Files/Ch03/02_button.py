#!/usr/bin/python3
# button.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        

def callback():
    print('Clicked!')

root = Tk()

button = ttk.Button(root, text = "Click Me")
button.pack()

# Allow button to work
button.config(command = callback)
# Simulate button push.
button.invoke()

# Disable button
button.state(['disabled'])
# Check state
print(button.instate(['disabled'])) # True
# Able button
button.state(['!disabled'])
print(button.instate(['!disabled']))  # True

logo = PhotoImage(file = 'C:\\Users\\Joseph\\Documents\\python\\Ex_Files_Python_GUI_Dev_Tkinter\\Exercise Files\\Ch03\\python_logo.gif') # change path to image as necessary
button.config(image = logo, compound = LEFT)
small_logo = logo.subsample(5, 5)
button.config(image = small_logo)

root.mainloop()
