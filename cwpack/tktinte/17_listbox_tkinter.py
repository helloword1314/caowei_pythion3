from tkinter import *

root = Tk()

theLB = Listbox(root, setgrid=True)
theLB.pack()
for item in ["篮球", "足球", "羽毛球", "麻球", "冰球", "火球", "地球", "水球"]:
    theLB.insert(END, item)
theButton = Button(root, text="删除", command=lambda x=theLB: x.delete(ACTIVE))
theButton.pack()
mainloop()
