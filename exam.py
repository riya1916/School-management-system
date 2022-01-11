from tkinter import *
from tkinter import ttk

def add():
    print("add")

    # print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")



    # with open("records.txt", "a") as f:
    #     f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")
def delete():
    print("delete")

    # print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")



    # with open("records.txt", "a") as f:
    #     f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")
def cancel():
    print("cancel")

    # print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")



    # with open("records.txt", "a") as f:
    #     f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")

root = Tk()

root.geometry("1200x800")
root.title("School_Management_System")
headingframe = Frame(root)
headingframe.place(x=0, y=0, width=1200, height=60)

# Heading
header = Label(headingframe, bd=20, text="EXAM", fg='white', bg='#3498db', font=("times new roman", 30))
header.pack(side=TOP, fill=X)

app1 = Frame(root, padx=20)
app1.place(x=40, y=80, width=1200, height=100)


#Text for our form
term = Label(app1, text="Term's")
date = Label(app1, text="Date")
standard = Label(app1, text="Class")
subject = Label(app1, text="Subject")
section = Label(app1, text="Section")

#Pack text for our form
term.grid(row=1, column=1, pady=6, padx=55)
date.grid(row=2, column=1, pady=6, padx=55)
standard.grid(row=1, column=4, pady=6, padx=55)
subject.grid(row=2, column=4, pady=6, padx=55)
section.grid(row=1, column=7, pady=6, padx=55)

# Tkinter variable for storing entries
termvalue = StringVar()
datevalue = StringVar()
standardvalue = StringVar()
subjectvalue = StringVar()
sectionvalue = StringVar()



#Entries for our form
termentry = Entry(app1, textvariable=termvalue, width=30)
dateentry = Entry(app1, textvariable=datevalue, width=30)
standardentry = Entry(app1, textvariable=standardvalue, width=30)
subjectentry = Entry(app1, textvariable=subjectvalue, width=30)
sectionentry = Entry(app1, textvariable=sectionvalue, width=30)


# Packing the Entries
termentry.grid(row=1, column=2)
dateentry.grid(row=2, column=2)
standardentry.grid(row=1, column=5)
subjectentry.grid(row=2, column=5)
sectionentry.grid(row=1, column=8)



app2 = Frame(root, padx=10)
app2.place(x=100, y=180, width=1000, height=100)

#Button & packing it and assigning it a command
Button(app2, text="ADD", command=add, bg="#CBC3E3", pady=3, padx=40).grid(row=3, column=1, padx=20)
Button(app2, text="DELETE", command=delete, bg="#CBC3E3", pady=3, padx=30).grid(row=3, column=3, padx=10)
Button(app2, text="CANCEL", command=cancel, bg="#CBC3E3", pady=3, padx=30).grid(row=3, column=2, padx=20)

# Search Teacher's
search = Label(app2, text="Search Teacher's")
search.grid(row=3, column=4, pady=6, padx=45)
searchvalue = StringVar()
searchentry = Entry(app2, textvariable=searchvalue, width=30)
searchentry.grid(row=3, column=5)


mainframe = Frame(root, bg="grey", bd=2, relief=RIDGE)
mainframe.place(x=60, y=250, width=1070, height=400)

style = ttk.Style()
style.element_create("Custom.Treeheading.border", "from", "default")
style.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.image", {'side': 'right'}),  # , 'sticky': ''
            ("Custom.Treeheading.text", {'sticky': 'we'})
        ]})
    ]}),
])
style.configure("Custom.Treeview.Heading", background="lightgrey", foreground="black", relief="groove")
style.map("Custom.Treeview.Heading", relief=[('active', 'flat'), ('pressed', 'sunken')])

yscroll = Scrollbar(mainframe, orient=VERTICAL)
xscroll = Scrollbar(mainframe, orient=HORIZONTAL)

'''Employee No, Teacher's name, Father Name, CNIC No,
 Date Of Birth'''

columns = ("Term", "Class", "Section", "Date", "Subject")

teacher_table = ttk.Treeview(mainframe, style="Custom.Treeview", columns=columns, show='headings',
                             yscrollcommand=yscroll.set,
                             xscrollcommand=xscroll.set)

yscroll.config(command=teacher_table.yview)
xscroll.config(command=teacher_table.xview)

yscroll.pack(side=RIGHT, fill=Y)
xscroll.pack(side=BOTTOM, fill=X)

teacher_table.heading("Term", text="Term")
teacher_table.heading("Class", text="Class")
teacher_table.heading("Section", text="Section")
teacher_table.heading("Date", text="Date")
teacher_table.heading("Subject", text="Subject")


teacher_table.column("Term", width=150)
teacher_table.column("Class", width=150, anchor=CENTER)
teacher_table.column("Section", width=150, anchor=CENTER)
teacher_table.column("Date", width=100, anchor=CENTER)
teacher_table.column("Subject", width=100, anchor=CENTER)


teacher_table.pack(fill=BOTH, expand=TRUE)


root.mainloop()