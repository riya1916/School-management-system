from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

def back_register():
    root.destroy()
    import staff_registration


def standard():
   pass


def subject():
    pass


def cancel():
    pass

root = Tk()

root.geometry("1200x800")
root.title("School_Management_System")
headingframe = Frame(root)
headingframe.place(x=0, y=0, width=1200, height=60)

# Heading
header = Label(headingframe, bd=20, text="EMPLOYEE PROFILE", fg='white', bg='#3498db', font=("times new roman", 30))
header.pack(side=TOP, fill=X)

f1 = Frame(root, padx=150)
f1.place(x=60, y=150, width=1100, height=300)

my_pic = ImageTk.PhotoImage(file="class1.png")
# my_pic2 = ImageTk.PhotoImage(file="book2.png")
my_pic3 = ImageTk.PhotoImage(file="cross.png")

my_label = Label(f1, image=my_pic)
# my_label2 = Label(f1, image=my_pic2)
my_label3 = Label(f1, image=my_pic3, bg='white')

my_label.pack(side=LEFT, padx=20)
# my_label2.pack(side=LEFT, padx=20)
my_label3.pack(side=LEFT, padx=20)

f2 = Frame(root, padx=150)
f2.place(x=60, y=460, width=1100, height=100)

Button(f2, text="CLASS", command=standard, bg="#E6E6FA", pady=3, padx=50, font=("lucida", 10, "bold")).grid(row=1, column=1, padx=50)
# Button(f2, text="SUBJECT", bg="#E6E6FA", command=subject, pady=3, padx=35, font=("lucida", 10, "bold")).grid(row=1, column=3, padx=80)
Button(f2, text="EXIT", command=cancel, bg="#FF6347", pady=3, padx=50, font=("lucida", 10, "bold")).grid(row=1, column=5, padx=60)

root.mainloop()