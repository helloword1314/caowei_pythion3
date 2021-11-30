from tkinter import *

root = Tk()


def test(content, reason, name):
    if content == "abc":
        print("right")
        print(content, reason, name)
        return True
    else:
        print("wrong")
        print(content, reason, name)
        return False


v = StringVar()
testCMD = root.register(test)
e1 = Entry(root, textvariable=v, validate="focusout", validatecommand=(testCMD, '%P', '%V', '%W'))
e2 = Entry(root)

e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)


mainloop()
