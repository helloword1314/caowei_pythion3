from tkinter import *

root = Tk()

s1 = Scale(root, from_=0, to=100, tickinterval=25, length=200, resolution=5)
s1.pack()

s2 = Scale(root, from_=0, to=200, tickinterval=10, length=600, orient=HORIZONTAL)
s2.pack()


def show():
    print(s1.get(), s2.get())


Button(root, text="获得位置", command=show).pack()
mainloop()
