from tkinter import *

class App(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.master.title("TE Vocabulary")
        self.master.geometry("800x600")
        self.config(bg="white")
        self.master.config(bg="white")
        self.all_here()

    def all_here(self):

        menubar = Menu(self)

        insertmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="insert", menu=insertmenu)
        insertmenu.add_command(label="new date", command=self.insert_date)

        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="help", menu=helpmenu)
        helpmenu.add_command(label="about", command=self.about_TEV)

        self.master.config(menu=menubar)

    def insert_date(self):
        pass

    def about_TEV(self):
        pass

root = Tk()

app = App(master=root)

root.mainloop()
