from tkinter import *
from tkinter import ttk
root = Tk()

# create a button
button = ttk.Button(root, text="Hello", command="buttonpressed")
button.grid() # show the button
# check the current value of the text option
button['text']
# change the value of the text option
button['text'] = 'goodbye'
button.configure(text='goodbye')
# check the current value of the text option
button['text']
# echo: 'goodbye'
# get information on all options for text option
button.configure('text')
# echo: ('text', 'text', 'Text', '', 'goodbye')
# get information about all options for this widget
button.configure()
print(button.configure())
""" {'command': ('command', 'command', 'Command', '', 'buttonpressed'), 
'default': ('default', 'default', 'Default', <string object: 'normal'>, <string object: 'normal'>), 
'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', 'ttk::takefocus', 'ttk::takefocus'), 
'text': ('text', 'text', 'Text', '', 'goodbye'), 'textvariable': ('textvariable', 'textVariable', 
'Variable', '', ''), 'underline': ('underline', 'underline', 'Underline', -1, -1), 
'width': ('width', 'width', 'Width', '', ''), 
'image': ('image', 'image', 'Image', '', ''), 
'compound': ('compound', 'compound', 'Compound', '', ''), 
'padding': ('padding', 'padding', 'Pad', '', ''), 
'state': ('state', 'state', 'State', <string object: 'normal'>, <string object: 'normal'>), 
'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 'style': ('style', 'style', 'Style', '', ''), 'class': ('class', '', '', '', '')} """