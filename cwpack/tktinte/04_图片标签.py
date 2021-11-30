import tkinter as tk
#找到父路径下的其他文件，即同级的其他文件

import os

os.chdir(os.path.split(os.path.realpath(__file__))[0])
root = tk.Tk()
root.title = "吹牛逼"

photo = tk.PhotoImage(file="cat.gif")

lable_first = tk.Label(root,
                       text="吹牛逼",
                       justify=tk.LEFT,
                       image=photo,
                       compound=tk.CENTER,
                       fg="white"
                       )
lable_first.pack()

root.mainloop()
