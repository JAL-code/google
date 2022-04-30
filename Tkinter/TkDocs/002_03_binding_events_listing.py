from tkinter import *
from tkinter import ttk


root = Tk()
l =ttk.Label(root, text="Starting...")
l.grid()
# Complete keylist at https://tcl.tk/man/tcl8.6/TkCmd/keysyms.htm

# Activate
# Deactivate
# MouseWheel
# KeyPress
l.bind('<a>', lambda e: l.configure(text='Pressed: a'))
# KeyRelease
l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button'))
l.bind('<2>', lambda e: l.configure(text='Clicked middle mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
# ButtonPress
l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
# ButtonRelease
l.bind('<ButtonRelease-1>', lambda e: l.configure(text='Released left mouse button'))
# Motion
l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
# Configure
# Destroy
# FocusIn
# FocusOut
# Enter
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
# Leave
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))

# Virtual Events 
# Widget -  <<ListboxSelect>> higher-level, semantic events (double brackets)
# Common operations - <<Cut>>, <<Copy>>, <<Paste>>.
# Custom - root.event_generate("<<MyOwnEvent>>")
root.mainloop()