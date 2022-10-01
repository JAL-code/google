# Demo file for new GUI using Tkinter (Python 3.5+)
# Updated class based seed file per JAL-code
# Layout by user4171906 at stackoverflow 36542747

from tkinter import *
from tkinter import ttk

class MainGui():

    def __init__(self, parent):
        self.parent = parent
        root.title('Base created')
        print("Started Container")
        self.GF1 = GenField(self.parent, _row = 0)
        self.GF2 = GenField(self.parent, _row = 1)
        self.GF2 = GenField(self.parent, _row = 2)
        self.GF2 = GenField(self.parent, _row = 4)

class GenField():

    def __init__(self, root, _row):
        gfframe = ttk.Frame(root)
        gfframe.grid(column=0, row=_row)
        self.gflabel = ttk.Label(gfframe, text=f'{_row} Label')
        self.gflabel.grid(column = 0, row = _row)
        self.gftext = ttk.Entry(gfframe)
        self.gftext.grid(column = 1, row = _row)
        self.gfcommand = ttk.Button(gfframe, text=f'{_row} Label Update', command = lambda: self.uln)
        self.gfcommand.grid(column = 2, row = _row)
        entry = ttk.Entry(root, width = 30)
        print("Added Label")

    # Update label name
    def uln(self):
        print(f"Test update {self.gftext.get()}")
        self.gflabel.labelText = self.gftext.get()


if __name__ == "__main__":
    root = Tk()
    MainGui(root)
    root.mainloop()