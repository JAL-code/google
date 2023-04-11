
# incorporating Tk
from tkinter import * # load the Tk library
from tkinter import ttk  # load the submodule for newer themed widgets.
# To prefix anything inside submodule

# calculate the feet to meters. Procedure added here since referenced in other parts of program.
def calculate(*args):
    try:
        value = float(feet.get()) # takes value from entry widget.
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)  # place value in label widget.
        # for rounding to a clean value divide by 10000.0
    except ValueError:
        pass

# clear the values
def clearvalues():
    pass

# set up the main application window.
root = Tk()
root.title("Feet to Meters")

# Create content frame since the main window does not match newer style
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create Entry Widget
feet = StringVar()
# Specify parent to place it as a child of the content frame.
# Parent, first parameter.
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# Place widget in grid and assign compass locations.
feet_entry.grid(column=2, row=1, sticky=(W, E))

# Add meter output to label widget.
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Add padding to all mainframe childeren
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# Focus on feet entry widget.
feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop() # tell Tk to enter its event loop.