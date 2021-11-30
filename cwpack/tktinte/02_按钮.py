import tkinter as tk

class App:
    def __init__(self, root):
        frame = tk.Frame(root)
        frame.pack()
        self.hi_three = tk.Button(frame,text="say hello",bg="white",fg="red", command=self.say_hi)
        self.hi_three.pack(side=tk.LEFT)

    def say_hi(self):
        print("hello ,welcome to the real world")


root = tk.Tk()
app = App(root)
root.mainloop()
