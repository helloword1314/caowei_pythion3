from tkinter import *

root = Tk()
group = LabelFrame(root, text="最好的脚本语言是：", padx=5, pady=5)
group.pack(padx=10, pady=10)
GIRLS = [("A", 1), ("B", 2), ("C", 3), ("D", 4)]
v = IntVar()
v.set(1)
for girl, num in GIRLS:

    b = Radiobutton(group, text=girl, variable=v, value=num, indicatoron=False)
    #b.pack(anchor=W)
    b.pack(fill=X)
mainloop()
