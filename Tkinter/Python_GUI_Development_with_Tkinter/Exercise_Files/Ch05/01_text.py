#!/usr/bin/python3
# text.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *      
# from PIL import ImageTk, Image
# import os
    
root = Tk()

text = Text(root, width = 40, height = 10)
text.pack()
text.config(wrap = 'word')  # word, none or char

# "base modifier modifier modifer"
# line.char  - lines start with 1 ( position in the text box) and char start with 0
# end - position from last character
# +/- # chars or lines
# linestart, lineend, wordstart, wordend

print(text.get('1.0', 'end'))
print(text.get('1.0', '1.end'))
text.insert('1.0 + 2 lines', 'Inserted message')
text.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore.')
text.delete('1.0')
text.delete('1.0', '1.0 lineend')
text.delete('1.0', '3.0 lineend + 1 chars')
text.replace('1.0', '1.0 lineend', 'This is the first line.')

text.config(state = 'disabled')  # lock text
text.delete('1.0', 'end')
text.config(state = 'normal')

text.tag_add('my_tag', '1.0', '1.0 wordend')
text.tag_configure('my_tag', background = 'yellow')  # font, foreground, justify, overstrike, underline, wrep, etc.
text.tag_remove('my_tag', '1.1', '1.3')
print(text.tag_ranges('my_tag'))
print(text.tag_names())
text.replace('my_tag.first', 'my_tag.last', 'That was')
text.tag_delete('my_tag')

# insert (cursor) and current (mouse)

text.mark_names()
text.insert('insert', '_')
# set gravity
text.mark_set('my_mark', 'end')
text.mark_gravity('my_mark', 'right')
text.mark_unset('my_mark')

#Setting it up for photo
img = PhotoImage(file = "C://Users//Joseph//Documents//GitHub//google//Tkinter//Python_GUI_Development_with_Tkinter//Exercise_Files//Ch05//python_logo.gif").subsample(5, 5)

# image = PhotoImage(file = 'python_logo.gif').subsample(5, 5) # Change path as needed

text.image_create('insert', image = img)
text.image_create('insert', image = img)
# Adding other Tk components
button = Button(text, text = 'Click Me')
text.window_create('insert', window = button)

root.mainloop()
