from tkinter import *
from tkinter import ttk

def back_register():
    root.destroy()
    import employee_work


def add():
    # address_text = addressentry.get("1.0", "end-1c")
    if (subject.get() == '' or search.get() == ''):

        return
    value = (subject.get(), search.get())
    teacher_table.insert('', END, values=value)
    clear_input()


def delete():
    for selected_item in teacher_table.selection():
        item = teacher_table.item(selected_item)['values']
    selected_item = teacher_table.selection()[0]
    teacher_table.delete(selected_item)


def clear_input():
    subjectentry.delete(0, END)
    searchentry.delete(0, END)


root = Tk()
root.geometry("1200x800")
root.title("School_Management_System")
headingframe = Frame(root)
headingframe.place(x=0, y=0, width=1200, height=60)

# Heading
header = Label(headingframe, bd=20, text="SUBJECT", fg='white', bg='#3498db', font=("times new roman", 30))
header.pack(side=TOP, fill=X)

f1 = Frame(root, padx=20)
f1.place(x=80, y=180, width=600, height=500)

subject = Label(f1, text="Subject Name", font=("lucida", 12, "bold"))
subject.grid(row=2, column=2, pady=6, padx=35)
subjectvalue = StringVar()
subjectentry = Entry(f1, textvariable=subjectvalue, width=30)
subjectentry.grid(row=2, column=3)

f12 = Frame(root, padx=60)
f12.place(x=80, y=240, width=600, height=100)

Button(f12, text="ADD", command=add, bg="#CBC3E3", padx=35, pady=4, font=("lucida", 12, "bold")).grid(row=1, column=3,
                                                                                                      padx=20)
Button(f12, text="DELETE", command=delete, bg="#CBC3E3", padx=35, pady=4, font=("lucida", 12, "bold")).grid(row=1,
                                                                                        column=5, padx=20)
# Button(f12, text="CANCEL", command=clear_input(), bg="#CBC3E3", padx=25, pady=6).grid(row=5, column=3)

f2 = Frame(root, padx=10)
f2.place(x=605, y=80, width=590, height=500)

search = Label(f2, text="Search", font=("lucida", 12, "bold"))
search.grid(row=2, column=3, padx=35, pady=6)
searchvalue = StringVar()
searchentry = Entry(f2, textvariable=searchvalue, width=30)
searchentry.grid(row=2, column=5, pady=10)

mainframe = Frame(root, bg="lightgrey", bd=2, relief=RIDGE)
mainframe.place(x=630, y=135, width=480, height=300)

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

'''Employee No, Teacher's name'''

columns = ("ID", "Subject name")

teacher_table = ttk.Treeview(mainframe, style="Custom.Treeview", columns=columns, show='headings',
                             yscrollcommand=yscroll.set,
                             xscrollcommand=xscroll.set)

yscroll.config(command=teacher_table.yview)
xscroll.config(command=teacher_table.xview)

yscroll.pack(side=RIGHT, fill=Y)
xscroll.pack(side=BOTTOM, fill=X)

teacher_table.heading("ID", text="ID")
teacher_table.heading("Subject name", text="Subject name")

teacher_table.column("Subject name", width=150, anchor=CENTER)
teacher_table.column("ID", width=150)


teacher_table.pack(fill=BOTH, expand=TRUE)


root.mainloop()