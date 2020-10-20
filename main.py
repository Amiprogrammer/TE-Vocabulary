from tkinter import *
import mysql.connector

db_connection = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="root",
                    database="te_vocabulary"
                )

class App(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.master.title("TE Vocabulary")
        self.master.geometry("730x560")
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

        toolbars1 = Frame(self)
        toolbars1["bg"] = "white"
        toolbars1.pack(side=TOP, fill=X)

        photo = PhotoImage(file="img/file1.png")

        photo_lbl = Label(toolbars1, image=photo, width=100, height=100)
        photo_lbl["bg"] = "white"
        photo_lbl.photo = photo
        photo_lbl.grid(row=0, column=0)

        index_lbl = Label(toolbars1, text="Tetum English Vocabulary.", bg="white", font=("Calibri",36))
        index_lbl.grid(row=0, column=1)

        toolbars2 = Frame(self)
        toolbars2["bg"] = "white"
        toolbars2.pack(side=TOP, fill=X)

        find_lbl = Label(toolbars2, text="Find your vocabulary with keyword(s) tetun !", anchor=W, justify=LEFT, bg="white", font=("Calibri",18))
        find_lbl.grid(row=0, pady=40)

        toolbars3 = Frame(self, bg="white")
        toolbars3.pack(fill=X, side=TOP)

        self.user_entry = Entry(toolbars3, font=("calibri",16), width=32, bg="grey", justify=CENTER)
        self.user_entry.grid(row=1, column=0)

        go_img = PhotoImage(file="img/file2.png")

        ok = Button(toolbars3, image=go_img, compound=CENTER, width=45, height=35, command=self.get_entry)
        ok.go_img = go_img
        ok.grid(row=1, column=1, padx=20)

        result_img = PhotoImage(file=r"img\file3.png")

        self.results = Label(toolbars3, text="Result Here!", font=("Calibri",36), image=result_img, compound=TOP, bg="white", width=250, height=160)
        self.results.result_img = result_img
        self.results.grid(row=2, columnspan=2, pady=100)

    def insert_date(self):
        pass

    def about_TEV(self):
        pass

    def get_entry(self):
        self.user_entry.focus_set()
        input = self.user_entry.get()

        print(input)


root = Tk()

app = App(master=root)

root.mainloop()
