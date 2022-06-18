#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        

# KeyPress Events
#     Event Format  : Event Description
# <Button>, <ButtonPress> : Any button was pressed.
# <Button-1>, <ButtonPress-1>, <1> : Button 1 was pressed.
# <ButtonRelease-1> : Button 1 was released.
# <Double-Button-1> or <Triple-Button-1> : Button 1 was double- or triple-clicked.
# Movement-Related Mouse Events
# <Enter> : Mouse entered widget area.
# <Leave> : Mouse left widget area.
# <Motion> : Mouse was moved.
# <B1-Motion> : Mouse was moved with Button 1 held down.

def mouse_press(event):
    global prev # save the event so accessible next mouse event.
    prev = event
    print('type:{}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num))
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
    print('x_root: {}'.format(event.x_root))
    print('y_root: {}'.format(event.y_root))

root = Tk()


canvas = Canvas(root, width = 640, height = 480, background = 'white')
canvas.grid()

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=5)
    prev = event
    
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

root.mainloop()
