from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def back_register():
    root.destroy()
    import staff_registration


def add():
    address_text = addressentry.get("1.0", "end-1c")
    if (employee.get() == '' or teacher.get() == '' or father.get() == ''
            or cnic.get() == '' or dob.get() == '' or appointment.get() == '' or gender.get() == ''
            or contact.get() == '' or email.get() == '' or grade.get() == ''
            or qualification.get() == '' or address_text == ''):
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    value = (employee.get(), teacher.get(), father.get(),
             cnic.get(), dob.get(), appointment.get(), gender.get(), contact.get(),
             email.get(), grade.get(), qualification.get(), address_text)
    teacher_table.insert('', END, values=value)
    clear_input()


def delete():
    for selected_item in teacher_table.selection():
        item = teacher_table.item(selected_item)['values']
    selected_item = teacher_table.selection()[0]
    teacher_table.delete(selected_item)


def clear_input():
    employeeentry.delete(0, END)
    teacherentry.delete(0, END)
    fatherentry.delete(0, END)
    cnicentry.delete(0, END)
    dobentry.delete(0, END)
    appointmententry.delete(0, END)
    contactentry.delete(0, END)
    emailentry.delete(0, END)
    gradeentry.delete(0, END)
    qualificationentry.delete(0, END)
    addressentry.delete('1.0', END)


root = Tk()
root.geometry("1200x800")
root.title("School_management_system")
headingframe = Frame(root)
headingframe.place(x=0, y=0, width=1200, height=60)

# Heading
header = Label(headingframe, bd=20, text="TEACHER REGISTRATION", fg='white', bg='#3498db', font=("times new roman", 30))
header.pack(side=TOP, fill=X)

app1 = Frame(root)
app1.place(x=40, y=80, width=1200, height=300)


#Text for our form
employee = Label(app1, text="Employee Number")
cnic = Label(app1, text="CNIC No.")
gender = Label(app1, text="Gender")
grade = Label(app1, text="Present Grade")
teacher = Label(app1, text="Teacher's Name")
dob = Label(app1, text="Date of Birth")
contact = Label(app1, text="Contact No.")
qualification = Label(app1, text="Qualification")
father = Label(app1, text="Father Name")
appointment = Label(app1, text="Date of Appointment")
email = Label(app1, text="Email Address")
address = Label(app1, text="Address")


#Pack text for our form
employee.grid(row=1, column=1, pady=6, padx=15)
cnic.grid(row=2, column=1, pady=6, padx=15)
gender.grid(row=3, column=1, pady=6, padx=15)
grade.grid(row=4, column=1, pady=6, padx=15)
teacher.grid(row=1, column=3, pady=6, padx=15)
dob.grid(row=2, column=3, pady=6, padx=15)
contact.grid(row=3, column=3, pady=6, padx=15)
qualification.grid(row=4, column=3, pady=6, padx=15)
father.grid(row=1, column=5, pady=6, padx=15)
appointment.grid(row=2, column=5, pady=6, padx=15)
email.grid(row=3, column=5, pady=6, padx=15)
address.grid(row=4, column=5, pady=6, padx=15)


# Tkinter variable for storing entries
employeevalue = IntVar()
cnicvalue = IntVar()
gendervalue = StringVar()
gradevalue = StringVar()
teachervalue = StringVar()
dobvalue = IntVar()
contactvalue = IntVar()
qualificationvalue = IntVar()
fathervalue = StringVar()
appointmentvalue = StringVar()
emailvalue = StringVar()
addressvalue = StringVar()



#Entries for our form
employeeentry = Entry(app1, textvariable=employeevalue, width=30)
cnicentry = Entry(app1, textvariable=cnicvalue, width=30)
genderentry = Entry(app1, textvariable=gendervalue, width=30)
gradeentry = Entry(app1, textvariable=gradevalue, width=30)
teacherentry = Entry(app1, textvariable=teachervalue, width=30)
dobentry = Entry(app1, textvariable=dobvalue, width=30)
contactentry = Entry(app1, textvariable=contactvalue, width=30)
qualificationentry = Entry(app1, textvariable=qualificationvalue, width=30)
fatherentry = Entry(app1, textvariable=fathervalue, width=30)
appointmententry = Entry(app1, textvariable=appointmentvalue, width=30)
emailentry = Entry(app1, textvariable=emailvalue, width=30)
addressentry = Text(app1, height=3, width=23, pady=5)


# Packing the Entries
employeeentry.grid(row=1, column=2)
cnicentry.grid(row=2, column=2)
genderentry.grid(row=3, column=2)
gradeentry.grid(row=4, column=2)
teacherentry.grid(row=1, column=4)
dobentry.grid(row=2, column=4)
contactentry.grid(row=3, column=4)
qualificationentry.grid(row=4, column=4)
fatherentry.grid(row=1, column=6)
appointmententry.grid(row=2, column=6)
emailentry.grid(row=3, column=6)
addressentry.grid(row=4, column=6)


app2 = Frame(root, padx=10)
app2.place(x=100, y=290, width=710, height=100)

#Button & packing it and assigning it a command
Button(app2, text="ADD", command=add, bg="#CBC3E3", pady=3, padx=40).grid(row=5, column=1, padx=20)
Button(app2, text="DELETE", command=delete, bg="#CBC3E3", pady=3, padx=30).grid(row=5, column=2, padx=10)
Button(app2, text="CANCEL", command=back_register, bg="#CBC3E3", pady=3, padx=30).grid(row=5, column=3,padx=20)

# Search Teacher's
search = Label(app2, text="Search Teacher's")
search.grid(row=5, column=4)
searchvalue = StringVar()
searchentry = Entry(app2, textvariable=searchvalue)
searchentry.grid(row=5, column=5)

mainframe = Frame(root, bg="grey", bd=2, relief=RIDGE)
mainframe.place(x=20, y=350, width=1070, height=330)

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
 Date Of Birth, Date of Appointment, Gender, Contact No, Email Address, 
 Present Grade, Qualification, Address'''

columns = ("Employee No", "Teacher's name", "Father Name", "CNIC No",
           "Date Of Birth", "Date of Appointment", "Gender", "Contact No",
           "Email Address", "Present Grade", "Qualification", "Address")

teacher_table = ttk.Treeview(mainframe, style="Custom.Treeview", columns=columns, show='headings',
                             yscrollcommand=yscroll.set,
                             xscrollcommand=xscroll.set)

yscroll.config(command=teacher_table.yview)
xscroll.config(command=teacher_table.xview)

yscroll.pack(side=RIGHT, fill=Y)
xscroll.pack(side=BOTTOM, fill=X)

teacher_table.heading("Employee No", text="Employee No")
teacher_table.heading("Teacher's name", text="Teacher's name")
teacher_table.heading("Father Name", text="Father Name")
teacher_table.heading("CNIC No", text="CNIC No")
teacher_table.heading("Date Of Birth", text="Date Of Birth")
teacher_table.heading("Date of Appointment", text="Date of Appointment")
teacher_table.heading("Gender", text="Gender")
teacher_table.heading("Contact No", text="Contact No")
teacher_table.heading("Email Address", text="Email Address")
teacher_table.heading("Present Grade", text="Present Grade")
teacher_table.heading("Qualification", text="Qualification")
teacher_table.heading("Address", text="Address")

teacher_table.column("Employee No", width=150)
teacher_table.column("Teacher's name", width=150, anchor=CENTER)
teacher_table.column("Father Name", width=150, anchor=CENTER)
teacher_table.column("CNIC No", width=100, anchor=CENTER)
teacher_table.column("Date Of Birth", width=100, anchor=CENTER)
teacher_table.column("Date of Appointment", width=150, anchor=CENTER)
teacher_table.column("Gender", width=100, anchor=CENTER)
teacher_table.column("Contact No", width=100, anchor=CENTER)
teacher_table.column("Email Address", width=200)
teacher_table.column("Present Grade", width=100)
teacher_table.column("Qualification", width=100)
teacher_table.column("Address", width=200)

teacher_table.pack(fill=BOTH, expand=TRUE)

root.mainloop()