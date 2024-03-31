from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkcalendar import DateEntry
from pymongo import MongoClient
import pymongo

# from tkinter import PhotoImage

root = Tk()
root.geometry("1540x800+0+0")


def Insert():
    mrdno = textmrdno.get()
    patient = textpatient.get()
    consultant = textconsultant.get()
    created = textlcreated.get()
    Ward=textlward.get()
    Signed=textlSigned.get()

    myclient=pymongo.MongoClient("")
    mydb=myclient['hospitalinfo']
    mycollection=mydb['pinfo']
    
    MessageBox.showinfo("Status", "Successfull inserted")

   


def Delete():
    mrdno = textmrdno.get()

    # name.delete(0,'end')
    # docter.delete(0,'end')
    consultant = textconsultant.get()

    con = mysql.connect(host="localhost", user="root", password="admin", database="hospitaldata")
    cursor = con.cursor()
    cursor.execute("delete from pinfo where no='" + mrdno + "'")
    cursor.execute("commit")
    MessageBox.showinfo("Status", "Successfully deleted")
    con.close()


def Update():
    mrdno = textmrdno.get()
    patient = textpatient.get()
    consultant = textconsultant.get()
    created = textlcreated.get()
    Ward = textlward.get()
    Signed = textlSigned.get()

    con = mysql.connect(host="localhost", user="root", password="*****", database="hospitaldata")
    cursor = con.cursor()
    cursor.execute(
        " update pinfo set patient='" + patient + "',mrdno='" + mrdno+ "' ,consultant='" + consultant + "' ,where no='" + mrdno + "'")
    cursor.execute("commit")
    MessageBox.showinfo("Status", "Successfully Updated")
    con.close()


def fetch():
    mrdno = textmrdno.get()
    patient = textpatient.get()
    consultant = textconsultant.get()
    created = textlcreated.get()
    Ward = textlward.get()
    Signed = textlSigned.get()


    con = mysql.connect(host="localhost", user="root", password="****", database="hospitaldata")
    cursor = con.cursor()
    cursor.execute(
        "select * from pinfo where mrdno='" + mrdno + "' ")
    rows = cursor.fetchall()

    # for r in rows:
    #     text_widget.insert(0,r[1])
    #     text_widget.insert(1,r[2])
    #     text_widget.insert(2,r[3])
    #    # display.insert(0,r[])

    cursor.execute("commit")
    con.close()
    return rows


def Display():
    data = fetch()
    disp_data.delete(1.0, "end")  # delete previous things making space for new one
    for row in data:
        disp_data.insert("end", f"{row}\n")


def Print():
    mrdno = textmrdno.get()



    con = mysql.connect(host="localhost", user="root", password="*****", database="hospitaldata")
    cursor = con.cursor()
    cursor.execute(
        "select * from pinfo where mrdno='" +mrdno+ "' ")
    cursor.execute("commit")
    MessageBox.showinfo("Status", "Successfully Updated")
    con.close()



def Display_prescription():
    mrdno = textmrdno.get()
    patient = textpatient.get()
    consultant = textconsultant.get()
    created = textlcreated.get()
    Ward = textlward.get()
    Signed = textlSigned.get()


    con = mysql.connect(host="localhost", user="root", password="***", database="hospitaldata")
    cursor = con.cursor()
    cursor.execute(
        "select * from pinfo where no='" + mrdno + "'")
    rows = cursor.fetchall()
    # Close the cursor and connection
    cursor.close()
    con.close()

    # Clear previous content from Text widget
    disp_data.delete(1.0, "end")

    # Display the fetched data in the Text widget
    for row in rows:
        disp_data.insert("end", f"{row}\n")


# ------------------------------- tkinter design---------------------------------------------------------------
lbltitle = Label(root, relief=RIDGE, text="PRESCRIPTION ISSUE", fg="Black", font=("times new roman", 50, "italic"))
lbltitle.pack(side=TOP, fill="x")

Dataframe = Frame(root, relief=RIDGE)
Dataframe.place(x=0, y=110, width=1530, height=360)

dfLeft = LabelFrame(Dataframe, bd=5, relief=RIDGE, padx=6, font=("times new roman", 12, "bold"),
                    text="Patient-information")
dfLeft.place(x=10, y=5, width=800, height=250)

lmrdno = Label(dfLeft, font=("times new roman", 12, "bold"), text="MRD No:", padx=2, pady=4)
lmrdno.grid(row=1, column=0, sticky=W)
textmrdno = Entry(dfLeft, textvariable=lmrdno, font=("times new roman", 12, "bold"), width=35)
textmrdno.grid(row=1, column=1)

lpatient = Label(dfLeft, font=("times new roman", 12, "bold"), text="Patient:", padx=2, pady=4)
lpatient.grid(row=2, column=0, sticky=W)
textpatient = Entry(dfLeft, textvariable=lpatient, font=("times new roman", 12, "bold"), width=35)
textpatient.grid(row=2, column=1)


lconsultant = Label(dfLeft, font=("times new roman", 12, "bold"), text="Consultant :", padx=2, pady=4)
lconsultant.grid(row=3, column=0, sticky=W)
textconsultant = Entry(dfLeft, textvariable=lconsultant, font=("times new roman", 12, "bold"), width=35)
textconsultant.grid(row=3, column=1)


lcreated = Label(dfLeft, font=("times new roman", 12, "bold"), text="Created:", padx=2, pady=4)
lcreated.grid(row=4, column=0, sticky=W)
textlcreated = Entry(dfLeft, textvariable=lcreated, font=("times new roman", 12, "bold"), width=35)
textlcreated.grid(row=4, column=1)

lward = Label(dfLeft, font=("times new roman", 12, "bold"), text="Ward:", padx=2, pady=4)
lward.grid(row=5, column=0, sticky=W)
textlward = Entry(dfLeft, textvariable=lward, font=("times new roman", 12, "bold"), width=35)
textlward.grid(row=5, column=1)

lSigned = Label(dfLeft, font=("times new roman", 12, "bold"), text="Signed:", padx=2, pady=4)
lSigned.grid(row=6, column=0, sticky=W)
textlSigned = Entry(dfLeft, textvariable=lSigned, font=("times new roman", 12, "bold"), width=35)
textlSigned.grid(row=6, column=1)

# -----------------------------------------------right side -------------------------------------------------------------------------

dfRight = LabelFrame(Dataframe, bd=5, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
dfRight.place(x=830, y=5, width=680, height=250)




pdatepres = Label(dfRight, font=("times new roman", 12, "bold"), text="Prescription :", padx=2, pady=4)
pdatepres.grid(row=1, column=0, sticky=W)
textpdatepres = DateEntry(dfRight, textvariable=pdatepres, font=("times new roman", 12, "bold"), width=33)
textpdatepres.grid(row=1, column=1)
Printbtn = Button(Dataframe, text="Print prescription", command=Print, font=("times new roman", 12, "bold"), bd=3,
                  width=15, height=2, bg='aliceblue').place(x=530, y=280)

prescription = Label(dfRight, font=("times new roman", 12, "bold"), text="Sex:", padx=2, pady=4)
prescription.grid(row=2, column=0, sticky=W)
textprescription = Entry(dfRight, textvariable=prescription, font=("times new roman", 12, "bold"), width=35 )
textprescription.grid(row=2, column=1)


pIssuedby = Label(dfRight, font=("times new roman", 12, "bold"), text="Issued By :", padx=2, pady=4)
pIssuedby.grid(row=5, column=0, sticky=W)
textpIssuedby = Entry(dfRight, textvariable=pIssuedby, font=("times new roman", 12, "bold"), width=35)
textpIssuedby.grid(row=5, column=1)





#-----------------------------------------------right side ends here--------------------------------------------------------------------------
btnInsert = Button(Dataframe, text="Insert", command=Insert, font=("times new roman", 12, "bold"), bd=3, width=10,
                   height=2).place(x=100, y=280)
btnDelete = Button(Dataframe, text="Delete", command=Delete, font=("times new roman", 12, "bold"), bd=3, width=10,
                   height=2).place(x=240, y=280)
btnUpdate = Button(Dataframe, text="Update", command=Update, font=("times new roman", 12, "bold"), bd=3, width=10,
                   height=2).place(x=390, y=280)
btnSelect = Button(Dataframe, text="Select", command=Display, font=("times new roman", 12, "bold"), bd=3, width=10,
                   height=2).place(x=730, y=280)

# -------------------------------------datafrom bottom for display only--------------------------------------------------------------------------------------------------------
# display data from database

df = LabelFrame(root, bd=5, relief=RIDGE, padx=6, font=("times new roman", 12, "bold"), text="Details")
df.place(x=10, y=480, width=900, height=280)

disp_data = Text(df, wrap="none", height=15, width=100)
disp_data.grid(row=0, column=0, padx=5, pady=5)

# Create a Scrollbar for the Text widget
scrollbar = Scrollbar(df, command=disp_data.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

# Configure the Text widget to use the Scrollbar
disp_data.config(yscrollcommand=scrollbar.set)

# --------------------------------------- design end ---------------------------
root.configure(bg="yellowgreen")
root.mainloop()
