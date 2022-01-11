from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def add():
    pass
def cancel():
    pass

root = Tk()

root.geometry("1200x800")
root.title("School_Management_System")
headingframe = Frame(root)
headingframe.place(x=0, y=0, width=1200, height=50)

# Heading
header = Label(headingframe, bd=20, text="SCHOOL INFORMATION", fg='white', bg='#3498db', font=("times new roman", 30))
header.pack(side=TOP, fill=X)

f1 = Frame(root, padx=70)
f1.place(x=0, y=85, width=600, height=500)

school = Label(f1, text="Name Of School", font=("lucida", 11, "bold"))
principal = Label(f1, text="Name Of Principal", font=("lucida", 11, "bold"))
classavailable = Label(f1, text="Class Available", font=("lucida", 11, "bold"))
area = Label(f1, text="Total Land Area", font=("lucida", 11, "bold"))
id = Label(f1, text="School ID No", font=("lucida", 11, "bold"))
registration = Label(f1, text="Registration No", font=("lucida", 11, "bold"))
postalcode = Label(f1, text="Postal Code", font=("lucida", 11, "bold"))
establishment = Label(f1, text="Date Of Establishment", font=("lucida", 11, "bold"))


#Pack text for our form
school.grid(row=1, column=1, pady=6, padx=15)
principal.grid(row=2, column=1, pady=6, padx=15)
classavailable.grid(row=3, column=1, pady=6, padx=15)
area.grid(row=4, column=1, pady=6, padx=15)
id.grid(row=5, column=1, pady=6, padx=15)
registration.grid(row=6, column=1, pady=6, padx=15)
postalcode.grid(row=7, column=1, pady=6, padx=15)
establishment.grid(row=8, column=1, pady=6, padx=15)

schoolvalue = StringVar()
principalvalue = StringVar()
classavailablevalue = StringVar()
areavalue = StringVar()
idvalue = StringVar()
registrationvalue = IntVar()
postalcodevalue = StringVar()
establishmentvalue = StringVar()

schoolentry = Entry(f1, textvariable=schoolvalue, width=30)
principalentry = Entry(f1, textvariable=principalvalue, width=30)
classavailableentry = Entry(f1, textvariable=classavailablevalue, width=30)
areaentry = Entry(f1, textvariable=areavalue, width=30)
identry = Entry(f1, textvariable=idvalue, width=30)
registrationentry = Entry(f1, textvariable=registrationvalue, width=30)
postalcodeentry = Entry(f1, textvariable=postalcodevalue, width=30)
establishmententry = Entry(f1, textvariable=establishmentvalue, width=30)

schoolentry.grid(row=1, column=2)
principalentry.grid(row=2, column=2)
classavailableentry.grid(row=3, column=2)
areaentry.grid(row=4, column=2)
identry.grid(row=5, column=2)
registrationentry.grid(row=6, column=2)
postalcodeentry.grid(row=7, column=2)
establishmententry.grid(row=8, column=2)

# ..........................

f2 = Frame(root)
f2.place(x=605, y=85, width=600, height=400)

council = Label(f2, text="Municipal Council", font=("lucida", 11, "bold"))
address = Label(f2, text="Address", font=("lucida", 11, "bold"))
post = Label(f2, text="Tehsil", font=("lucida", 11, "bold"))
district = Label(f2, text="District", font=("lucida", 11, "bold"))
province = Label(f2, text="Province", font=("lucida", 11, "bold"))
country = Label(f2, text="Country", font=("lucida", 11, "bold"))

council.grid(row=1, column=1, pady=6, padx=15)
address.grid(row=2, column=1, pady=6, padx=15)
post.grid(row=5, column=1, pady=6, padx=15)
district.grid(row=6, column=1, pady=6, padx=15)
province.grid(row=7, column=1, pady=6, padx=15)
country.grid(row=8, column=1, pady=6, padx=15)

councilvalue = StringVar()
addressvalue = StringVar()
postvalue = StringVar()
districtvalue = IntVar()
provincevalue = StringVar()
countryvalue = StringVar()


#Entries for our form
councilentry = Entry(f2, textvariable=councilvalue, width=30)
addressentry = Entry(f2, textvariable=addressvalue, width=30)
postentry = Entry(f2, textvariable=postvalue, width=30)
districtentry = Entry(f2, textvariable=districtvalue, width=30)
provinceentry = Entry(f2, textvariable=provincevalue, width=30)
countryentry = Entry(f2, textvariable=countryvalue, width=30)

# Packing the Entries

councilentry.grid(row=1, column=2)
addressentry.grid(row=2, column=2)
postentry.grid(row=5, column=2)
districtentry.grid(row=6, column=2)
provinceentry.grid(row=7, column=2)
countryentry.grid(row=8, column=2)

f3 = Frame(root, padx=250)
f3.place(x=40, y=400, width=1100, height=100)

#Button & packing it and assigning it a command
Button(f3, text="REGISTRATION", bg="#d4ebf2", command=add, pady=3, padx=30, font=("lucida", 12, "bold")).grid(row=1,
                                                                                                column=1, padx=30)
Button(f3, text="EXIT", bg="#FF6347", command=cancel, pady=3, padx=50, font=("lucida", 12, "bold")).grid(row=1,
                                                                                                    column=2, padx=60)




root.mainloop()