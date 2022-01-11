from tkinter import *
from tkinter import ttk

def back_register():
    root.destroy()
    import teacherwork


def add():
    # address_text = addressentry.get("1.0", "end-1c")
    if (id.get() == '' or name.get() == '' or section.get() == ''):

        return
    value = (id.get(), name.get(), section.get())
    teacher_table.insert('', END, values=value)
    clear_input()


def delete():
    for selected_item in teacher_table.selection():
        item = teacher_table.item(selected_item)['values']
    selected_item = teacher_table.selection()[0]
    teacher_table.delete(selected_item)


def clear_input():
    # identry.delete(0, END)
    nameentry.delete(0, END)
    sectionentry.delete(0, END)

root = Tk()
root.geometry("1200x800")
root.title("School_Management_System")
headingframe = Frame(root)
headingframe.place(x=0, y=0, width=1200, height=60)

# Heading
header = Label(headingframe, bd=20, text="CLASS", fg='white', bg='#3498db', font=("times new roman", 30))
header.pack(side=TOP, fill=X)

app1 = Frame(root, padx=20)
app1.place(x=170, y=80, width=1200, height=300)


#Text for our form
name = Label(app1, text="Class Name", font=("lucida", 12, "bold"))
section = Label(app1, text="Section", font=("lucida", 12, "bold"))

#Pack text for our form
name.grid(row=1, column=2, pady=6, padx=45)
section.grid(row=1, column=5, pady=6, padx=45)


# Tkinter variable for storing entries
namevalue = StringVar()
sectionvalue = StringVar()

#Entries for our form
nameentry = Entry(app1, textvariable=namevalue, width=30)
sectionentry = Entry(app1, textvariable=sectionvalue, width=30)

# Packing the Entries
nameentry.grid(row=1, column=3)
sectionentry.grid(row=1, column=6)

app2 = Frame(root, padx=40)
app2.place(x=250, y=140, width=710, height=50)

Button(app2, text="ADD", command=add, bg="#CBC3E3", pady=3, padx=40).grid(row=5, column=1, padx=35)
Button(app2, text="DELETE", command=delete, bg="#CBC3E3", pady=3, padx=40).grid(row=5, column=2, padx=25)
Button(app2, text="CANCEL", command=clear_input, bg="#CBC3E3", pady=3, padx=40).grid(row=5, column=3, padx=35)

mainframe = Frame(root, bg="lightgrey", bd=2, relief=RIDGE)
mainframe.place(x=65, y=210, width=1070, height=330)

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

'''ID, Class name, Father Name'''

columns = ("ID", "Class name", "Section")

teacher_table = ttk.Treeview(mainframe, style="Custom.Treeview", columns=columns, show='headings',
                             yscrollcommand=yscroll.set,
                             xscrollcommand=xscroll.set)

yscroll.config(command=teacher_table.yview)
xscroll.config(command=teacher_table.xview)

yscroll.pack(side=RIGHT, fill=Y)
xscroll.pack(side=BOTTOM, fill=X)

teacher_table.heading("ID", text="ID")
teacher_table.heading("Class name", text="Class name")
teacher_table.heading("Section", text="Section")

teacher_table.column("ID", width=150)
teacher_table.column("Class name", width=150, anchor=CENTER)
teacher_table.column("Section", width=150, anchor=CENTER)

teacher_table.pack(fill=BOTH, expand=TRUE)


root.mainloop()