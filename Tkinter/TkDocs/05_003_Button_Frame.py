from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

def submitForm():
    print("Form submitted")

root = Tk()
root.title("Frames")
frame = ttk.Frame(root).grid()
# label = ttk.Label(frame, text='Full name')

#Setting it up
img = ImageTk.PhotoImage(Image.open("C:\\Users\\Joseph\\Documents\\python\\Official_Tkinter\\myimage.gif"))

# Update label text
button = ttk.Button(frame, text='Submit', command=submitForm)
button.grid()

action = ttk.Button(root, text="Action", default="active", command=submitForm)
root.bind('<Return>', lambda e: action.invoke())

# foreground and background - color names or hex RGB codes.

# wraplength - Multi-line Labels
root.mainloop()

# The widget state is a bitmap of independent state flags. Widget state flags include:
# active
# The mouse cursor is over the widget and pressing a mouse button will cause some action to occur. (aka “prelight” (Gnome), “hot” (Windows), “hover”).
# disabled
# Widget is disabled under program control (aka “unavailable”, “inactive”).
button.state(['disabled'])          # set the disabled flag
button.state(['!disabled'])         # clear the disabled flag
button.instate(['disabled'])        # true if disabled, else false
button.instate(['!disabled'])       # true if not disabled, else false
button.instate(['!disabled'], submitForm)  # execute 'cmd' if not disabled

# focus
# Widget has keyboard focus.
# pressed
# Widget is being pressed (aka “armed” in Motif).
# selected
# “On”, “true”, or “current” for things like checkbuttons and radiobuttons.
# background
# Windows and the Mac have a notion of an “active” or foreground window. The background state is set for widgets in a background window, and cleared for those in the foreground window.
# readonly
# Widget should not allow user modification.
# alternate
# A widget-specific alternate display format. For example, used for checkbuttons and radiobuttons in the “tristate” or “mixed” state, and for buttons with -default active.
# invalid
# The widget's value is invalid. (Potential uses: scale widget value out of bounds, entry widget value failed validation.)
# hover
# The mouse cursor is within the widget. This is similar to the active state; it is used in some themes for widgets that provide distinct visual feedback for the active widget in addition to the active element within the widget.
# A state specification or stateSpec is a list of state names, optionally prefixed with an exclamation point (!) indicating that the bit is off.