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