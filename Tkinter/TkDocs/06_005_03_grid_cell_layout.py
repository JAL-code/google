# By JAL-code
from tkinter import *
from tkinter import ttk

# Custom widget to explain cell layout.
root = Tk()

data1 = StringVar()
data2 = StringVar()

content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=300, height=200)
widgetlbl = ttk.Label(content, text="other widget")
widgetlbl2 = ttk.Label(content, text="other widget")
name = ttk.Entry(content, textvariable=data1)
name2 = ttk.Entry(content, textvariable=data2)

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=2, rowspan=2)
widgetlbl.grid(column=0, row=0)
name.grid(column=1, row=0)

name2.grid(column=0, row=1)
widgetlbl2.grid(column=1, row=1)
root.mainloop()