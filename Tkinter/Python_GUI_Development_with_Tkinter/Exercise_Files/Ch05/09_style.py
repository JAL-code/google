#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk   

# Widget States - active, disabled, focus, pressed, selected, background, readonly, alternate, invalid, hover
    
root = Tk()

button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')      
button1.pack()
button2.pack()

# style object
style = ttk.Style()

print(style.theme_names())
print(style.theme_use())
style.theme_use('classic')
style.theme_use('vista')

# Widget Style Names
# "T" + widget name: TButton, TFrame, TCombobox
# Except for:   Treeview, TPanedwindow, 
#               Horizontal.TScale or Vertical.Tscale, 
#               Horizontal.TScrollbar or Vertical.TScrollbar
#               Horizontal.TProgressbar or Vertical.TProgressbar

print(button1.winfo_class())
style.configure('TButton', foreground = 'blue')
style.configure('Alarm.TButton', foreground = 'orange',
                font = ('Arial', 24, 'bold'))
button2.configure(style = 'Alarm.TButton')
style.map('Alarm.TButton', foreground = [('pressed', 'pink'),
                                         ('disabled', 'grey')])
button2.state(['disabled'])

print(style.layout('TButton'))
print(style.element_options('Button.label'))
print(style.lookup('TButton', 'foreground'))

root.mainloop()
