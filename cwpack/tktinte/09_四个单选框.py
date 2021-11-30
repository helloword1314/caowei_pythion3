from tkinter import *

root = Tk()
GIRLS = [("A", 1), ("B", 2), ("C", 3), ("D", 4)]
v = IntVar()
v.set(1)
for girl, num in GIRLS:

    b = Radiobutton(root, text=girl, variable=v, value=num, indicatoron=False)
    #b.pack(anchor=W)
    b.pack(fill=X)
mainloop()
