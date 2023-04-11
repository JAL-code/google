# incorporating Tk
from tkinter import * # load the Tk library
from tkinter import ttk  # load the submodule for newer themed widgets.

root = Tk()
content = ttk.Frame(root)
button = ttk.Button(content)
# pass the parent as a parameter to the widget class.

print(str(content))
print(str(button))
# when the object is inserted into the widget hierarchy
# it won't be garbage collected even if you don't keep your own reference to it.
root.mainloop()