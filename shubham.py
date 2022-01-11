from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def back_register():
    root.destroy()
    import staffregister


def insert_item():
    address_text = address_entry.get("1.0", "end-1c")
    if (employee_num.get() == '' or teacher_name.get() == '' or father_name.get() == ''
            or cnic_num.get() == '' or dob_text.get() == '' or doa_text.get() == '' or gender.get() == ''
            or contact_num.get() == '' or email_text.get() == '' or present_grade.get() == ''
            or qualification.get() == '' or address_text == ''):
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    value = (employee_num.get(), teacher_name.get(), father_name.get(),
             cnic_num.get(), dob_text.get(), doa_text.get(), gender.get(), contact_num.get(),
             email_text.get(), present_grade.get(), qualification.get(), address_text)
    teacher_table.insert('', END, values=value)
    clear_input()


def delete_item():
    for selected_item in teacher_table.selection():
        item = teacher_table.item(selected_item)['values']
    selected_item = teacher_table.selection()[0]
    teacher_table.delete(selected_item)


def clear_input():
    employee_entry.delete(0, END)
    teacher_entry.delete(0, END)
    father_entry.delete(0, END)
    cnic_entry.delete(0, END)
    dob_entry.delete(0, END)
    doa_entry.delete(0, END)
    contact_entry.delete(0, END)
    email_entry.delete(0, END)
    grade_entry.delete(0, END)
    qualification_entry.delete(0, END)
    address_entry.delete('1.0', END)


root = Tk()

root.title("Teacher Registration Form")
root.geometry('1120x700')

headingframe = Frame(root)
headingframe.place(x=0, y=0, width=1200, height=60)

header = Label(headingframe, bd=20, text="TEACHER REGISTRATION", fg='white', bg='#3498db', font=("times new roman", 30))
header.pack(side=TOP, fill=X)

app1 = Frame(root)
app1.place(x=0, y=80, width=710, height=200)

# Employee Number
employee_num = IntVar(value='')
employee_label = Label(app1, text='Employee Number', font=('bold', 13), pady=20, padx=20)
employee_label.grid(row=0, column=0, sticky=W)
employee_entry = Entry(app1, textvariable=employee_num, width=30)
employee_entry.grid(row=0, column=1)
# CNIC No
cnic_num = StringVar()
cnic_label = Label(app1, text='CNIC No', font=('bold', 13), padx=20)
cnic_label.grid(row=1, column=0, sticky=W)
cnic_entry = Entry(app1, textvariable=cnic_num, width=30)
cnic_entry.grid(row=1, column=1)
# Gender
gender = StringVar()
gender_label = Label(app1, text='Gender', font=('bold', 13), pady=20, padx=20)
gender_label.grid(row=2, column=0, sticky=W)
gender_entry = ttk.Combobox(app1, state='readonly', textvariable=gender, width=27)
gender_entry['values'] = ('MALE', 'FEMALE', 'OTHERS')
gender_entry.grid(row=2, column=1)
gender_entry.current(0)
# Present Grade
present_grade = StringVar()
grade_label = Label(app1, text='Present Grade', font=('bold', 13), padx=20)
grade_label.grid(row=3, column=0, sticky=W)
grade_entry = Entry(app1, textvariable=present_grade, width=30)
grade_entry.grid(row=3, column=1)

# ----------------------------------

# Teacher's Name
teacher_name = StringVar()
teacher_label = Label(app1, text="Teacher's Name", font=('bold', 13), padx=20)
teacher_label.grid(row=0, column=3, sticky=W)
teacher_entry = Entry(app1, textvariable=teacher_name, width=30)
teacher_entry.grid(row=0, column=4)
# Date of Birth
dob_text = StringVar()
dob_label = Label(app1, text='Date of Birth', font=('bold', 13), padx=20)
dob_label.grid(row=1, column=3, sticky=W)
dob_entry = Entry(app1, textvariable=dob_text, width=27)
dob_entry.grid(row=1, column=4)
# Contact Number
contact_num = StringVar()
contact_label = Label(app1, text='Contact Number', font=('bold', 13), padx=20)
contact_label.grid(row=2, column=3, sticky=W)
contact_entry = Entry(app1, textvariable=contact_num, width=30)
contact_entry.grid(row=2, column=4)
# Qualification
qualification = StringVar()
qualification_label = Label(app1, text='Qualification', font=('bold', 13), padx=20)
qualification_label.grid(row=3, column=3, sticky=W)
qualification_entry = Entry(app1, textvariable=qualification, width=30)
qualification_entry.grid(row=3, column=4)

# ----------------------------------

app2 = Frame(root)
app2.place(x=710, y=80, width=500, height=300)

# Father Name
father_name = StringVar()
father_label = Label(app2, text='Father Name', font=('bold', 13), pady=20, padx=20)
father_label.grid(row=0, column=1, sticky=W)
father_entry = Entry(app2, textvariable=father_name, width=30)
father_entry.grid(row=0, column=2)
# Date of Appointment
doa_text = StringVar()
doa_label = Label(app2, text='Date of Appointment', font=('bold', 13), padx=20)
doa_label.grid(row=1, column=1, sticky=W)
doa_entry = Entry(app2, textvariable=doa_text, width=27)
doa_entry.grid(row=1, column=2)
# Email Address
email_text = StringVar()
email_label = Label(app2, text='Email Address', font=('bold', 13), pady=20, padx=20)
email_label.grid(row=2, column=1, sticky=W)
email_entry = Entry(app2, textvariable=email_text, width=30)
email_entry.grid(row=2, column=2)
# Address
# address_text = StringVar()
address_label = Label(app2, text='Address', font=('bold', 13), padx=20)
address_label.grid(row=3, column=1, sticky=NW)
address_entry = Text(app2, height=6, width=30 )
# address = address_entry.get("1.0", "end-1c")
# address_entry = Entry(app, textvariable=address_text, width=30, pady=20)
address_entry.grid(row=3, column=2)

app3 = Frame(root)
app3.place(x=100, y=290, width=710, height=100)

# Buttons
addBtn = Button(app3, text='ADD', font=('bold', 13), width=10, command=insert_item)
addBtn.grid(row=0, column=1, padx=10)

deleteBtn = Button(app3, text='DELETE', font=('bold', 13), width=10, command=delete_item)
deleteBtn.grid(row=0, column=2, padx=10)

cancelBtn = Button(app3, text='CANCEL', font=('bold', 13), width=10, command=back_register)
cancelBtn.grid(row=0, column=3, padx=10)

# Search Teacher's
search_text = StringVar()
search_label = Label(app3, text="Search Teacher's", font=('bold', 13), padx=20)
search_label.grid(row=0, column=6, sticky=W)
search_entry = Entry(app3, textvariable=search_text, width=30)
search_entry.grid(row=0, column=7)

# Tabular Data

mainframe = Frame(root, bg="lightgrey", bd=2, relief=RIDGE)
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


# For Sample Data
# contents = []
# for i in range(50):
#     contents.append((i, "Marry hgfg", "Haary Hatela", 76545678, "14/08/2009", "28/09/2021",
#                      "MALE", 87654345678, "xyz@yahoo.co.in", "hgfdfgh", "MBA",
#                      "jhgfdsdfiokijuhygtfdsfgjkjh"))
#
# for content in contents:
#     teacher_table.insert('', END, values=content)

teacher_table.pack(fill=BOTH, expand=TRUE)

root.mainloop()