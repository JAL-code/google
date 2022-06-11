#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Tk Event Types
# ButtonPress, ButtonRelease, Enter, Leave, Motion,
# KeyPress Events
#     Event Format  : Event Description
# <Key>, <KeyPress> : User pressed any key.
# <KeyPress-Delete> : User pressed Delete key.
# <KeyRelease-Right>: User released the Right Arrow key.
# a, b, c, 1, 2, 3, etc... and <space>, <less>: User pressed a printable key.
# <Shift_L>, <Control_R>, <F5>, <Up> : User pressed a "special" key.
#  Note keysym encased in angle brackets.
# <Return>: User pressed the enter key.
# <Control-Alt-Next> :  User pressed Ctrl+Alt+Page Down keys.
# KeyRelease
# FocusIn
# FocusOut

from tkinter import *
from tkinter import ttk        
    
root = Tk()

def key_press(event):
    print('type:{}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('char: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}'.format(event.keycode))

def shortcut(action):
    print(action)

root.bind('<KeyPress>', key_press)

root.bind('<Control-c>', lambda e: shortcut('Copy'))
root.bind('<Control-v>', lambda e: shortcut('Paste'))

root.mainloop()
