from tkinter import *
from tkinter import messagebox
import mysql.connector

db_connection = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="root",
                    database="te_vocabulary"
                )

mycursor = db_connection.cursor()

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

        find_lbl = Label(toolbars2, text="Find your vocabulary with keyword(s) tetun !", anchor=W, justify=LEFT, bg="white", font=("Calibri Italic",16))
        find_lbl.grid(row=0, pady=40)

        toolbars3 = Frame(self, bg="white")
        toolbars3.pack(fill=X, side=TOP)

        self.user_entry = Entry(toolbars3, justify=CENTER, bg="grey", font=("Calibri",16), width=28)
        self.user_entry.grid(row=0, column=0)

        right_arrow = PhotoImage(file="img/file2.png")

        confirm_button = Button(toolbars3, image=right_arrow, width=48, height=25, command=self.get_entry)
        confirm_button.right_arrow = right_arrow
        confirm_button.grid(row=0, column=1, padx=10)

        toolbars4 = Frame(self, bg="white")
        toolbars4.pack(fill=X, side=TOP, pady=20)

        tetun_index = Label(toolbars4, text="Tetun", font=("Calibri",24), bg="white")
        tetun_index.grid(row=0, column=0)

        english_index = Label(toolbars4, text="English", font=("Calibri",24), bg="white")
        english_index.grid(row=0, column=1, padx=60)

        self.tetun = Label(toolbars4, text="", font=("Calibri",24), bg="white")
        self.tetun.grid(row=1, column=0)

        self.english = Label(toolbars4, text="", font=("Calibri",24), bg="white")
        self.english.grid(row=1, column=1, padx=60)

    def insert_date(self):
        pass

    def about_TEV(self):
        about = Toplevel()
        about.title("About TE Vocabulary")
        about.geometry("400x350")

        photo = PhotoImage(file="img/file1.png")

        te_img = Label(about, image=photo)
        te_img.photo = photo
        te_img.pack()

        self.te_lbl = Label(about, text="TE Vocabulary", font=("Calibri",24))
        self.te_lbl.pack(pady=5)

        var = StringVar()
        var.set("This program built with Python V3.8.2 programming languague and Tkinter V8.5 Module with associate MySQL database server to develop this program\n\n\n(C) 2020. <> by Juliao Martins")

        message = Message(about, textvariable=var, font=("Calibri Bold",8), width=180, justify=CENTER)
        message.pack(pady=10)

        Button(about, text="Dismiss", bg="red", fg="black", command=about.destroy).pack()

        self.te_lbl.bind("<Enter>",self.change_color)
        self.te_lbl.bind("<Leave>",self.default_color)

    def change_color(self,event):
        self.te_lbl.config(fg="lightgreen")

    def default_color(self,event):
        self.te_lbl.config(fg="black")

    def get_entry(self):
        try:
            self.user_entry.focus_set()
            input = self.user_entry.get()

            if( len(input) == 0 ):
                messagebox.showwarning("TE Vocabulary",
                                "Please Insert Something!")
            elif( len(input) > 0 ):
                sql = "SELECT tetun,english FROM words WHERE tetun = %s"
                val = (input.lower(),)

                mycursor.execute(sql,val)
                result = mycursor.fetchall()

                if( mycursor.rowcount > 0):
                    self.tetun.config(text=result[0][0], fg="black")
                    self.english.config(text=result[0][1], fg="black")

                    self.user_entry.delete(0, END)
                else:
                    self.tetun.config(text="la iha!", fg="red")
                    self.english.config(text="not exists!", fg="red")

                    self.user_entry.delete(0, END)
        except Exception as err:
            messagebox.showerror("TE Vocabulary",f"ERROR: {err}")


root = Tk()

app = App(master=root)

root.mainloop()
