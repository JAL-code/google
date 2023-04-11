from tkinter import *
from tkinter import ttk

# Frames help to organize your user interface, 
# often both visually and at the coding level. 
# Frames often act as master widgets for a geometry manager like grid, 
# which manages the slave widgets contained within the frame.

size = True
padding = 2 # (1,2,3)
borders =  True
relief = 'flat'
setstyle = True
# relief options: flat (default), raised, sunken, solid, ridge, or groove.

root = Tk()
root.title("Frames")
frame = ttk.Frame(root)
if size:
    frame['width'] = '5i'
    frame['height'] = '10i'
    pass  # 350 pixels - 350 
    # 350 centimeters = 350c
    # 350 inches = 350i
    # 350 points (1/72 inch) - 350p
if padding == 1:
    frame['padding'] = 5           # 5 pixels on all sides
if padding == 2:
    frame['padding'] = (5,10)      # 5 on left and right, 10 on top and bottom
if padding == 3:
    frame['padding'] = (5,7,10,12) # left: 5, top: 7, right: 10, bottom: 12

if borders:
    frame['borderwidth'] = 2
    frame['relief'] = relief

if setstyle:
    s = ttk.Style()
    s.configure('Danger.TFrame', background='red', borderwidth=5, relief='ridge')
    ttk.Frame(root, width=200, height=200, style='Danger.TFrame').grid()

root.mainloop()