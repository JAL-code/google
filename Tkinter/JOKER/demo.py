# Demo file for new GUI using Tkinter (Python 3.5+)
# Updated class based seed file per JAL-code

from tkinter import *
from tkinter import ttk

class MainGui:

    def __init__(self, root):
        root.grid()
        print("Started Container")

        frame = ttk.Frame(root)

if __name__ == "__main__":
    root = Tk()
    MainGui(root)
    root.mainloop()
