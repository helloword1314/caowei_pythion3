from tkinter import *

root = Tk()
GIRLS = ["A", "B", "C", "D"]
v = []
for girl in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root, text=girl, variable=v[-1])
    b.pack(anchor=W)

mainloop()
