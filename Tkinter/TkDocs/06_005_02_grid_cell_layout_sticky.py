# By JAL-code
from tkinter import *
from tkinter import ttk

# Custom widget to explain cell layout using sticky.
root = Tk()

data1 = StringVar(value="default layout")
data2 = StringVar(value="default layout")

content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
widgetlbl = ttk.Label(content, text="other widget")
widgetlbl2 = ttk.Label(content, text="other widget")
name = ttk.Entry(content, textvariable=data1)
name2 = ttk.Label(content, textvariable=data2)

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=(N, S, E, W))
widgetlbl.grid(column=0, row=0, sticky=(E, W))
name.grid(column=1, row=0)

name2.grid(column=0, row=1, sticky=(W))
widgetlbl2.grid(column=1, row=1)
root.mainloop()