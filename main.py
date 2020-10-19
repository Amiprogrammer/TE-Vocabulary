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

        toolbars = Frame(self)
        toolbars["bg"] = "white"
        toolbars.pack(side=TOP, fill=X)

        photo = PhotoImage(file="img/file1.png")

        photo_lbl = Label(toolbars, image=photo, width=100, height=100)
        photo_lbl["bg"] = "white"
        photo_lbl.photo = photo
        photo_lbl.grid(row=0, column=0)

        index_lbl = Label(toolbars, text="Tetum English Vocabulary.", bg="white", font=("Calibri",36))
        index_lbl.grid(row=0, column=1)

        find_lbl = Label(toolbars, text="Find your vocabulary with tetun keyword(s)!", anchor=W, justify=LEFT, bg="white", font=("Calibri",18))
        find_lbl.grid(row=1, columnspan=2, pady=40)

        self.user_entry = Entry(toolbars, font=("calibri",16))
        self.user_entry.grid(row=2, column=0)

    def insert_date(self):
        pass

    def about_TEV(self):
        pass

root = Tk()

app = App(master=root)

root.mainloop()
