# Demo file for new GUI using Tkinter (Python 3.5+)
# Updated class based seed file per JAL-code
# Layout by user4171906 at stackoverflow 36542747

from ast import Not
from tkinter import *
from tkinter import ttk

class MainGui():

    def __init__(self, parent):
        self.parent = parent
        root.title('Base created')
        print("Started Container")
        self.GF1 = GenField(self.parent, _row = 0, name = "Name")
        self.GF2 = GenField(self.parent, _row = 1, name = "Picture")
        self.GF3 = GenField(self.parent, _row = 2, name = "Used In")
        self.GF4 = GenField(self.parent, _row = 4, name = "Recipes")
        self.save = SaveItem(self.parent, _row = 5)

class GenField():

    def __init__(self, root, _row, name):
                     
        # Create Label Variable
        self.labelText = StringVar()
        self.labelText.set(f'{_row} {name}')

        # Create grid
        gfframe = ttk.Frame(root)
        gfframe.grid(column=0, row=_row)

        # Label, Text for string/number data
        self.gflabel = ttk.Label(gfframe)
        self.gflabel['textvariable'] = self.labelText
        self.gflabel.grid(column=0, row=_row, padx=10, sticky=(W, N, E))
        self.gftext = ttk.Entry(gfframe)
        self.gftext.grid(column=1, row=_row, sticky=(E))
        self.gfcommand = ttk.Button(gfframe, text=f'{_row} Label Update', command=self.uln)
        self.gfcommand.grid(column=4, row=_row, sticky=(E))
        # entry = ttk.Entry(root, width=30)
        print("Added Label")

    # Update label name
    def uln(self):
        if self.gftext.get() != "":
            self.labelText.set(self.gftext.get())
        print(self.gftext.get())

class SaveItem():

    def __init__(self, root, _row):

        # Create grid
        gfframe = ttk.Frame(root)
        gfframe.grid(column=0, row=_row)
        self.gfcommand = ttk.Button(gfframe, text=f'Set File', command=self.setlocation)
        self.gfcommand.grid(column=3, row=_row, sticky=(E))
        self.gfcommand = ttk.Button(gfframe, text=f'Save Data', command=self.savedata)
        self.gfcommand.grid(column=4, row=_row, sticky=(E))
        # entry = ttk.Entry(root, width=30)
        print("Added Label")

    # Update label name
    def savedata(self):
        print('saving data')

    def setlocation(self):
        print('Setting save location')

if __name__ == "__main__":
    root = Tk()
    MainGui(root)
    root.mainloop()
