# incorporating Tk
from tkinter import * # load the Tk library
from tkinter import ttk  # load the submodule for newer themed widgets.

def print_hierarchy(w, depth=0):
    print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()) + ' viewable=' + str(w.winfo_viewable()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)

root = Tk()
content = ttk.Frame(root, padding="3 3 12 12").grid(column=0, row=0, sticky=W)
button = ttk.Button(content, text="Print Hierarchy to debug.", command=print_hierarchy(root, depth = 0))
button.grid(column=1, row=1, sticky=(S,E))

# Focus on feet entry widget.
button.focus()
root.bind("<Return>", print_hierarchy(root, depth = 0))

root.mainloop()

# winfo_class:
# a class identifying the type of widget, e.g., TButton for a themed button
# winfo_children:
# a list of widgets that are the direct children of a widget in the hierarchy
# winfo_parent:
# parent of the widget in the hierarchy
# winfo_toplevel:
# the toplevel window containing this widget
# winfo_width, winfo_height:
# current width and height of the widget; not accurate until it appears onscreen
# winfo_reqwidth, winfo_reqheight:
# the width and height that the widget requests of the geometry manager (more on this shortly)
# winfo_x, winfo_y:
# the position of the top-left corner of the widget relative to its parent
# winfo_rootx, winfo_rooty:
# the position of the top-left corner of the widget relative to the entire screen
# winfo_vieweable:
# whether the widget is displayed or hidden (all its ancestors in the hierarchy must be viewable for it to be viewable)