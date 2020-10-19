from tkinter import *

class App(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.master.title("TE Vocabulary")
        self.master.geometry("800x600")
        self.config(bg="white")
        self.master.config(bg="white")

root = Tk()

app = App(master=root)

root.mainloop()
