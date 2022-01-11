import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def back_register():
    root.destroy()
    import staff_registration


def add():
    address_text = addressentry.get("1.0", "end-1c")
    if (admission.get() == '' or student.get() == '' or parent.get() == ''
            or cnic.get() == '' or dob.get() == '' or dateofadmission.get() == '' or gender.get() == ''
            or standard.get() == '' or section.get() == '' or email.get() == ''
            or contact.get() == '' or address_text == ''):
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    value = (admission.get(), student.get(), parent.get(),
             cnic.get(), dob.get(), dateofadmission.get(), gender.get(), standard.get(), section.get(), email.get(),
             contact.get(), address_text)
    teacher_table.insert('', END, values=value)
    clear_input()


def delete():
    for selected_item in teacher_table.selection():
        item = teacher_table.item(selected_item)['values']
    selected_item = teacher_table.selection()[0]
    teacher_table.delete(selected_item)


def clear_input():
    admissionentry.delete(0, END)
    studententry.delete(0, END)
    parententry.delete(0, END)
    cnicentry.delete(0, END)
    dobentry.delete(0, END)
    dateofadmissionentry.delete(0, END)
    genderentry.delete(0, END)
    standardentry.delete(0, END)
    sectionentry.delete(0, END)
    emailentry.delete(0, END)
    contactentry.delete(0, END)
    addressentry.delete('1.0', END)


root = Tk()
root.geometry("1200x800")
root.title("School_management_system")
headingframe = Frame(root)
headingframe.place(x=0, y=0, width=1200, height=60)

conn = sqlite3.connect('tree_crm.db')

c = conn.cursor()

c.execute(""" CREATE TABLE if not exists customers(
   admission text,
   cnic integer,
   gender text,
   email text,
   student_name text,
   dob integer,
   standard integer,
   contact integer,
   parent integer,
   dateofadmission integer,
   appointment integer,
   section text,
   address text )
    """)

conn.commit()

conn.close()

def query_database():
    conn = sqlite3.connect('tree_crm.db')

    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    records = c.fetchall()

# Heading
header = Label(headingframe, bd=20, text="STUDENT REGISTRATION", fg='white', bg='#3498db', font=("times new roman", 30))
header.pack(side=TOP, fill=X)

app1 = Frame(root, padx=20)
app1.place(x=40, y=80, width=1200, height=300)


#Text for our form
admission = Label(app1, text="Admission Number")
cnic = Label(app1, text="CNIC No.")
gender = Label(app1, text="Gender")
email = Label(app1, text="Email Address")
student = Label(app1, text="Student Name")
dob = Label(app1, text="Date of Birth")
standard = Label(app1, text="Class")
contact = Label(app1, text="Contact No.")
parent = Label(app1, text="Parent/Guardian Name")
dateofadmission = Label(app1, text="Date of Admission")
appointment = Label(app1, text="Appointment")
section = Label(app1, text="Section")
address = Label(app1, text="Address")

#Pack text for our form
admission.grid(row=1, column=1, pady=6, padx=15)
cnic.grid(row=2, column=1, pady=6, padx=15)
gender.grid(row=3, column=1, pady=6, padx=15)
email.grid(row=4, column=1, pady=6, padx=15)
student.grid(row=1, column=3, pady=6, padx=15)
dob.grid(row=2, column=3, pady=6, padx=15)
standard.grid(row=3, column=3, pady=6, padx=15)
contact.grid(row=4, column=3, pady=6, padx=15)
parent.grid(row=1, column=5, pady=6, padx=35)
dateofadmission.grid(row=2, column=5, pady=6, padx=35)
section.grid(row=3, column=5, pady=6, padx=15)
address.grid(row=4, column=5, pady=6, padx=15)

# Tkinter variable for storing entries
admissionvalue = IntVar()
cnicvalue = IntVar()
gendervalue = StringVar()
emailvalue = StringVar()
studentvalue = StringVar()
dobvalue = IntVar()
standardvalue = IntVar()
contactvalue = IntVar()
parentvalue = StringVar()
dateofadmissionvalue = IntVar()
sectionvalue = StringVar()
addressvalue = StringVar()


#Entries for our form
admissionentry = Entry(app1, textvariable=admissionvalue, width=30)
cnicentry = Entry(app1, textvariable=cnicvalue, width=30)
genderentry = Entry(app1, textvariable=gendervalue, width=30)
emailentry = Entry(app1, textvariable=emailvalue, width=30)
studententry = Entry(app1, textvariable=studentvalue, width=30)
dobentry = Entry(app1, textvariable=dobvalue, width=30)
standardentry = Entry(app1, textvariable=standardvalue, width=30)
contactentry = Entry(app1, textvariable=contactvalue, width=30)
parententry = Entry(app1, textvariable=parentvalue, width=30)
dateofadmissionentry = Entry(app1, textvariable=dateofadmissionvalue, width=30)
sectionentry = Entry(app1, textvariable=sectionvalue, width=30)
addressentry = Entry(app1, textvariable=addressvalue, width=30)

# Packing the Entries
admissionentry.grid(row=1, column=2)
cnicentry.grid(row=2, column=2)
genderentry.grid(row=3, column=2)
emailentry.grid(row=4, column=2)
studententry.grid(row=1, column=4)
dobentry.grid(row=2, column=4)
standardentry.grid(row=3, column=4)
contactentry.grid(row=4, column=4)
parententry.grid(row=1, column=6)
dateofadmissionentry.grid(row=2, column=6)
sectionentry.grid(row=3, column=6)
addressentry.grid(row=4, column=6)

app2 = Frame(root, padx=10)
app2.place(x=100, y=290, width=710, height=100)

#Button & packing it and assigning it a command
Button(app2, text="ADD", command=add, bg="#E6E6FA", pady=3, padx=40).grid(row=5, column=1, padx=20)
Button(app2, text="DELETE", command=delete, bg="#E6E6FA", pady=3, padx=30).grid(row=5, column=2, padx=10)
Button(app2, text="CANCEL", command=back_register, bg="#E6E6FA", pady=3, padx=30).grid(row=5, column=3,padx=20)

# Search Teacher's
search = Label(app2, text="Search Teacher's")
search.grid(row=5, column=4, pady=6, padx=15)
searchvalue = StringVar()
searchentry = Entry(app2, textvariable=searchvalue, width=30)
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

'''Admission No, CNIC No, Gender,  Email Address,
 Student, Date of Birth, Standard, Contact No, 
 Parent,Date of Admission, Appointment, Section, Address'''

columns = ("Admission No", "Student Name", "Father Name", "CNIC No", "Date of Birth", "Date of Admission", "Gender",
           "Class", "Section", "Email", "Contact", "Address")

teacher_table = ttk.Treeview(mainframe, style="Custom.Treeview", columns=columns, show='headings',
                             yscrollcommand=yscroll.set,
                             xscrollcommand=xscroll.set)

yscroll.config(command=teacher_table.yview)
xscroll.config(command=teacher_table.xview)

yscroll.pack(side=RIGHT, fill=Y)
xscroll.pack(side=BOTTOM, fill=X)

teacher_table.heading("Admission No", text="Admission No")
teacher_table.heading("Student Name", text="Student Name")
teacher_table.heading("Father Name", text="Father Name")
teacher_table.heading("CNIC No", text="CNIC No")
teacher_table.heading("Date of Birth", text="Date of Birth")
teacher_table.heading("Date of Admission", text="Date of Admission")
teacher_table.heading("Gender", text="Gender")
teacher_table.heading("Class", text="Class")
teacher_table.heading("Section", text="Section")
teacher_table.heading("Email", text="Email")
teacher_table.heading("Contact", text="Contact")
teacher_table.heading("Address", text="Address")

teacher_table.column("Admission No", width=100)
teacher_table.column("Student Name", width=125, anchor=CENTER)
teacher_table.column("Father Name", width=120, anchor=CENTER)
teacher_table.column("CNIC No", width=80, anchor=CENTER)
teacher_table.column("Date of Birth", width=100, anchor=CENTER)
teacher_table.column("Date of Admission", width=150, anchor=CENTER)
teacher_table.column("Gender", width=100, anchor=CENTER)
teacher_table.column("Class", width=80, anchor=CENTER)
teacher_table.column("Section", width=80)
teacher_table.column("Email", width=150)
teacher_table.column("Contact", width=100)
teacher_table.column("Address", width=150)

teacher_table.pack(fill=BOTH, expand=TRUE)

query_database()

root.mainloop()