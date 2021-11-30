import tkinter as tk
import os

os.chdir(os.path.split(os.path.realpath(__file__))[0])
def callback():
    var.set("吹牛逼，我不信")
root = tk.Tk()
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
var = tk.StringVar()
var.set("再想想 \n请三思啊")
lable_text = tk.Label(frame1,
                      justify=tk.LEFT,
                      textvariable=var
                      )
lable_text.pack(side=tk.LEFT)
photo = tk.PhotoImage(file="cat.gif")
lable_image = tk.Label(frame1, image=photo)
lable_image.pack(side=tk.RIGHT)
thebutton = tk.Button(frame2, text="哥，我十八了", command=callback)
thebutton.pack()
frame1.pack()
frame2.pack()
root.mainloop()
