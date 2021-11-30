from tkinter import *

root = Tk()


def test():
    if e1.get() == "abc":
        print("right")
        return True
    else:
        print("wrong")
        e1.delete(0, END)
        return False


def test2():
    print("you cuo le")
    return True


v = StringVar()
e1 = Entry(root, textvariable=v, validate="focusout", validatecommand=test, invalidcommand=test2)
e2 = Entry(root)

e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)


mainloop()
