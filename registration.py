from tkinter import *
from tkcalendar import *
from PIL import ImageTk
from tkinter import ttk
def add():
    pass
def cancel():
    pass

root = Tk()
root.geometry("1200x800")
root.title("School_Management_System")
root.iconbitmap('C:/Users/Dell/PycharmProjects/School_management_system/student2.png')

mainframe = Frame(root)
mainframe.place(x=0, y=0, width=1200, height=800)

f1 = Frame(root, padx=20)
f1.place(x=0, y=180, width=600, height=500)


my_pic = ImageTk.PhotoImage(file="Registration.png")
my_label = Label(f1, image=my_pic)
my_label.pack(side=LEFT, padx=20)

header = Label(f1, text="REGISTRATION", fg='white', bg='#3498db', font=("lucida", 30, "bold"))
header.pack(anchor=S, side=LEFT)


f2 = Frame(root, padx=20)
f2.place(x=680, y=100, width=1200, height=500)


name = Label(f2, text="Name", font=("lucida", 11, "bold"))
username = Label(f2, text="User Name", font=("lucida", 11, "bold"))
gmail = Label(f2, text="Gmail", font=("lucida", 11, "bold"))
contact = Label(f2, text="Phone No", font=("lucida", 11, "bold"))
gender = Label(f2, text="Gender", font=("lucida", 11, "bold"))
dob = Label(f2, text="Date of Birth", font=("lucida", 11, "bold"))
password = Label(f2, text="Password", font=("lucida", 11, "bold"))
address = Label(f2, text="Address", font=("lucida", 11, "bold"))
usertype = Label(f2, text="Usertype", font=("lucida", 11, "bold"))


name.grid(row=1, column=1, padx=15, pady=10)
username.grid(row=2, column=1, padx=15, pady=10)
gmail.grid(row=3, column=1, padx=15, pady=10)
contact.grid(row=4, column=1, padx=15, pady=10)
gender.grid(row=5, column=1, padx=15, pady=10)
dob.grid(row=6, column=1, padx=15, pady=10)
password.grid(row=7, column=1, padx=15, pady=10)
address.grid(row=8, column=1, padx=15, pady=10)
usertype.grid(row=9, column=1, padx=15, pady=10)



namevalue = StringVar()
usernamevalue = StringVar()
gmailvalue = StringVar()
contactvalue = IntVar()
gendervalue = StringVar()
dobvalue = IntVar()
passwordvalue = IntVar()
addressvalue = IntVar()

# usertypevalue = StringVar()
clicked = StringVar()
clicked.set("MALE")

#Entries for our form
nameentry = Entry(f2, textvariable=namevalue, width=30)
usernameentry = Entry(f2, textvariable=usernamevalue, width=30)
gmailentry = Entry(f2, textvariable=gmailvalue, width=30)
contactentry = Entry(f2, textvariable=contactvalue, width=30)
genderentry = Entry(f2, textvariable=gendervalue, width=30)
dobentry = Entry(f2, textvariable=dobvalue, width=30)
passwordentry = Entry(f2, textvariable=passwordvalue, width=30)
addressentry = Entry(f2, textvariable=addressvalue, width=30)

# usertypeentry = Entry(f2, textvariable=usertypevalue, width=30)
usertype = OptionMenu(f2, clicked, "MALE", "FEMALE")


# Packing the Entries
nameentry.grid(row=1, column=2)
usernameentry.grid(row=2, column=2)
gmailentry.grid(row=3, column=2)
contactentry.grid(row=4, column=2)
genderentry.grid(row=5, column=2)
dobentry.grid(row=6, column=2)
passwordentry.grid(row=7, column=2)
addressentry.grid(row=8, column=2)

usertype.grid(row=9, column=2)

f3 = Frame(root, padx=20)
f3.place(x=670, y=520, width=1200, height=100)

Button(f3, text="REGISTER", command=add, bg="#d4ebf2", pady=4, padx=30, font=("lucida", 11, "bold")).grid(row=14, column=1, padx=20)
Button(f3, text="CANCEL", bg="#FF6347", command=cancel, pady=4, padx=30, font=("lucida", 11, "bold")).grid(row=14, column=2, padx=20)


root.mainloop()