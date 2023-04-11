from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Frames")
frame = ttk.Frame(root).grid()
# label = ttk.Label(frame, text='Full name')

#Setting it up
img = ImageTk.PhotoImage(Image.open("C:\\Users\\Joseph\\Documents\\python\\Official_Tkinter\\myimage.gif"))

# Update label text
label = ttk.Label(frame, text='Full name', image=img, compound="center")
label.grid()

# set image display options
# label['compound'] = 'none' # Display only text
# label['compound'] = 'text'
# Or textvariable (see update label text)
# label['compound'] = 'image'
# label['compound'] = 'center'
# label['compound'] = 'top'
# label['compound'] = 'left'

# foreground and background - color names or hex RGB codes.

# wraplength - Multi-line Labels
root.mainloop()