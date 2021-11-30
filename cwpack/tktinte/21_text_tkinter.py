from tkinter import *

root = Tk()

te = Text(root, width=200, height=5)
te.pack()

te.insert(INSERT, "I LOVE ")


def show():
    print("I have been clicked")


button = Button(root, text="click me !", command=show)
button.pack()
mainloop()
