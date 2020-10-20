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
        self.config(bg="grey")
        self.master.config(bg="grey")
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
        toolbars1["bg"] = "grey"
        toolbars1.pack(side=TOP, fill=X)

        photo = PhotoImage(file="img/file1.png")

        photo_lbl = Label(toolbars1, image=photo, width=100, height=100)
        photo_lbl["bg"] = "grey"
        photo_lbl.photo = photo
        photo_lbl.grid(row=0, column=0)

        index_lbl = Label(toolbars1, text="TE Vocabulary.", bg="grey", font=("Calibri",36))
        index_lbl.grid(row=0, column=1)

        toolbars2 = Frame(self)
        toolbars2["bg"] = "grey"
        toolbars2.pack(side=TOP, fill=X)

        find_lbl = Label(toolbars2, text="Find your vocabulary with keyword(s) tetun !", anchor=W, justify=LEFT, bg="grey", font=("Calibri Italic",16))
        find_lbl.grid(row=0, pady=40)

        toolbars3 = Frame(self, bg="grey")
        toolbars3.pack(fill=X, side=TOP)

        self.user_entry = Entry(toolbars3, justify=CENTER, font=("Calibri",16), width=28)
        self.user_entry.grid(row=0, column=0)

        right_arrow = PhotoImage(file="img/file2.png")

        confirm_button = Button(toolbars3, image=right_arrow, width=48, height=25, command=self.get_entry)
        confirm_button.right_arrow = right_arrow
        confirm_button.grid(row=0, column=1, padx=10)

        toolbars4 = Frame(self, bg="grey")
        toolbars4.pack(fill=X, side=TOP, pady=20)

        tetun_index = Label(toolbars4, text="Tetun", font=("Calibri",24), bg="grey")
        tetun_index.grid(row=0, column=0)

        english_index = Label(toolbars4, text="English", font=("Calibri",24), bg="grey")
        english_index.grid(row=0, column=1, padx=60)

        self.tetun = Label(toolbars4, text="", font=("Calibri",24), bg="grey")
        self.tetun.grid(row=1, column=0)

        self.english = Label(toolbars4, text="", font=("Calibri",24), bg="grey")
        self.english.grid(row=1, column=1, padx=60)

    def insert_date(self):
        insert_window = Toplevel()
        insert_window.title("TE Vocabulary")
        insert_window.geometry("480x350")
        insert_window.config(bg="grey")

        photo = PhotoImage(file="img/file1.png")

        te_img = Label(insert_window, image=photo, text="Insert a new date!", compound=TOP, font=("Calibri",24), bg="grey")
        te_img.photo = photo
        te_img.pack()

        form_insert = Frame(insert_window, bg="grey")
        form_insert.pack()

        tetun_lbl = Label(form_insert, text="Tetun", font=("Calibri",16), bg="grey")
        tetun_lbl.grid(row=0, column=0)

        english_lbl = Label(form_insert, text="English", font=("Calibri",16), bg="grey")
        english_lbl.grid(row=0, column=1)

        self.new_tetun_entry = Entry(form_insert, font=("Calibri",16), justify=CENTER)
        self.new_tetun_entry.grid(row=1, column=0, padx=8)

        self.new_english_entry = Entry(form_insert, font=("Calibri",16), justify=CENTER)
        self.new_english_entry.grid(row=1, column=1, padx=8)

        Button(form_insert, text="OK", font=("Cooper Black",12), bg="blue", fg="white", command=self.get_in_date).grid(row=2, columnspan=2, pady=20)

    def get_in_date(self):
        self.new_tetun_entry.focus_set()
        self.new_english_entry.focus_set()

        new_tetun = self.new_tetun_entry.get()
        new_english = self.new_english_entry.get()

        if( len(new_tetun) == 0 or len(new_english) == 0 ):
            messagebox.showwarning("TE Vocabulary",
                                "please insert a value in prompt!")
            self.new_tetun_entry.delete(0, END)
            self.new_english_entry.delete(0, END)
        else:
            sql = "INSERT INTO words (tetun,english) VALUES (%s,%s)"
            val = (new_tetun.lower(),new_english.lower())
            mycursor.execute(sql,val)

            db_connection.commit()

            if( mycursor.rowcount > 0 ):
                messagebox.showinfo("TE Vocabulary",
                            "Success!\n1 record(s) inserted.")
            else:
                messagebox.showwarning("TE Vocabulary",
                            "Faill!\n1 record(s) not inserted.")

    def about_TEV(self):
        about_window = Toplevel()
        about_window.title("About TE Vocabulary")
        about_window.geometry("400x350")
        about_window.config(bg="grey")

        photo = PhotoImage(file="img/file1.png")

        self.te_lbl = Label(about_window, image=photo, text="TE Vocabulary", compound=TOP, font=("Calibri",24),bg="grey")
        self.te_lbl.photo = photo
        self.te_lbl.pack()

        var = StringVar()
        var.set("This program built with Python V3.8.2 programming languague and Tkinter V8.5 Module with associate MySQL database server to develop this program\n\n\n(C) 2020. <> by Juliao Martins")

        message = Message(about_window, textvariable=var, font=("Calibri Bold",8), width=180, justify=CENTER, bg="grey", fg="white")
        message.pack(pady=10)

        Button(about_window, text="Dismiss", bg="red", fg="black", command=about_window.destroy).pack()

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

                self.tetun.config(text="", fg="black")
                self.english.config(text="", fg="black")

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
