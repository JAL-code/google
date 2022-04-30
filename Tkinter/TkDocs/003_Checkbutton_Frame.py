from tkinter import *
from tkinter import ttk

def submitForm(state):
    print(f"Measure System Selected: {state}")

root = Tk()
root.title("Frames")
frame = ttk.Frame(root).grid()

measureSystem = StringVar()
check = ttk.Checkbutton(frame, text='Use Metric', 
	    command=submitForm(measureSystem), variable=measureSystem,
	    onvalue='metric', offvalue='imperial')

check.grid()

# text, textvariable, image, and compound configuration options 
# command and invoke - run a method
# state and instate - disabled flag

root.mainloop()

# More examples: 
# C:\Users\Joseph\Documents\python\Official_Tkinter\Outside_Examples
# \m6e_checkbox_and_radio_buttons.py