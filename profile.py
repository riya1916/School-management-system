from tkinter import *
from PIL import ImageTk

def register():
    print("add")


def login():
    print("delete")


def exit():
    print("cancel")


root = Tk()

root.geometry("1200x800")
root.title("School_Management_System")
headingframe = Frame(root)
headingframe.place(x=0, y=0, width=1200, height=50)

# Heading
header = Label(headingframe, bd=20, text="SCHOOL MANAGEMENT SYSTEM  v1.0", fg='white', bg='#3498db', font=("times new roman", 30))
header.pack(side=TOP, fill=X)

f1 = Frame(root, padx=80)
f1.place(x=80, y=160, width=1200, height=300)


my_pic = ImageTk.PhotoImage(file="student.png")
my_pic2 = ImageTk.PhotoImage(file="lock.png")
my_pic3 = ImageTk.PhotoImage(file="cross.png")

my_label = Label(f1, image=my_pic)
my_label2 = Label(f1, image=my_pic2)
my_label3 = Label(f1, image=my_pic3)

my_label.pack(side=LEFT, padx=20)
my_label2.pack(side=LEFT, padx=20)
my_label3.pack(side=LEFT, padx=20)

f2 = Frame(root, padx=80)
f2.place(x=80, y=470, width=1100, height=100)

Button(f2, text="REGISTRATION", bg="#d4ebf2", command=register, pady=3, padx=60).grid(row=1, column=1, padx=30)
Button(f2, text="LOGIN", bg="#d4ebf2", command=login, pady=3, padx=70).grid(row=1, column=2, padx=40)
Button(f2, text="EXIT", bg="#FF6347", command=exit, pady=3, padx=60).grid(row=1, column=3, padx=60)


root.mainloop()