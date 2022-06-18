#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root)
entry.pack()

# Examples of binding to a virtual event.
# Copy function: CTRL + C
entry.bind('<<Copy>>', lambda e: print('Copy'))
# Paste function: CTRL + P
entry.bind('<<Paste>>', lambda e: print('Paste'))

# Create your own event with event_add.
entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

print(entry.event_info('<<OddNumber>>'))

#Trigger the event
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')
entry.event_generate('<<Copy>>')

# Remove an event
entry.event_delete('<<OddNumber>>')

root.mainloop()
