#!/usr/bin/python3
# toplevel.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *      
    
root = Tk()

window = Toplevel(root)
window.title('New Window')  # Default size is x = 200, y = 200

window.lower() # move the window down one position
window.lift(root) # move the window up one position

window.state('zoomed')  # Maximize the window to largest allowable size
window.state('withdrawn') # Hide a window
window.state('iconic')  # Minimize the window so it is still accessible in the task bar.
window.state('normal')  # Default state in zoomed state.
print(window.state()) # Get the current state of a window.  It's still zoomed.
window.state('normal') # Return the window initalization state.

window.iconify()  # Shortcut to put the window in the task bar.
window.deiconify()  # Shortcut to put the window in normal state.

window.geometry('640x480+50+100')  # width x height + (50 left + 100 up) origin (x+ ->, y+ V)
print(window.geometry())
window.resizable(False, False)  # control resize in x and y directions
window.maxsize(640, 480)
window.minsize(200, 200)
window.resizable(True, True)

root.destroy()

root.mainloop()
