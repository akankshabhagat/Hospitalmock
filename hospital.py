from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector



class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital System")
        self.root.geometry("1540x800+0+0")
        
        #------------------------variables for all buttons----------------

        self.Nametablet=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Notablets=StringVar()
        self.Lot=StringVar()
        self.issueDate=StringVar()
        self.ExpDate=StringVar()
        self.Dailydose=StringVar()
        self.SideEffects=StringVar()
        self.Furtherinfo=StringVar()
        self.Bloodpressure=StringVar()
        self.Storage=StringVar()
        self.Medicine=StringVar()
        self.Patientid=StringVar()
        self.chssNumber=StringVar()
        self.Patientname=StringVar()
        self.DateofBirth=StringVar()
        self.PatientAddress=StringVar()
     





        











        #-------------------------------------------end of variable for buttons----------------
        
        lbltitle=Label(self.root,bd=10,relief=RIDGE,text="HOSPITAL SYSTEM",fg="Black",bg="aliceblue",font=("times new roman",50,"italic"))
        lbltitle.pack(side=TOP,fill="x")
        # ------------------data frame---------------------------------------------------------
        Dataframe=Frame(self.root,bd=5,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        dataframeLeft=LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=60,
        font=("times new roman",12,"bold"),text="Patient information")
        dataframeLeft.place(x=0,y=5,width=1000,height=350)

        dataframeRight=LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10,
        font=("times new roman",12,"bold"),text="Prescription")
        dataframeRight.place(x=1010,y=5,width=460,height=350)
        


#-------------------------------Button frame----------------------
        Buttonframe=Frame(self.root,bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

#-------------------------------Detail fram-e---------------------
        detailsframe=Frame(self.root,bd=10,relief=RIDGE)
        detailsframe.place(x=0,y=600,width=1530,height=190)

# ------------------------- Dataframe left-----------------------------------
        lblNametablet=Label(dataframeLeft,text="Names of tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNametablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(dataframeLeft,textvariable=self.Nametablet,state="readonly",font=("times new roman",12,"bold"),width=33)
        comNametablet["values"]=("Nice","corona virus","acetaminophen","adderall","amlodipoine","antivac")
        comNametablet.grid(row=0,column=1)

        lblref=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Reference No:",padx=2,pady=4)
        lblref.grid(row=1,column=0,sticky=W)
        textref=Entry(dataframeLeft,textvariable=self.ref,font=("times new roman",12,"bold"),width=35)
        textref.grid(row=1,column=1)

        lblDose=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        textref=Entry(dataframeLeft,textvariable=self.Dose,font=("times new roman",12,"bold"),width=35)
        textref.grid(row=2,column=1)

        lblNotablets=Label(dataframeLeft,font=("times new roman",12,"bold"),text="No of tablets:",padx=2,pady=6)
        lblNotablets.grid(row=3,column=0,sticky=W)
        textNotablets=Entry(dataframeLeft,textvariable=self.Notablets,font=("times new roman",12,"bold"),width=35)
        textNotablets.grid(row=3,column=1)

        lblLot=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        textLot=Entry(dataframeLeft,textvariable=self.Lot,font=("times new roman",12,"bold"),width=35)
        textLot.grid(row=4,column=1)


        lblissueDate=Label(dataframeLeft,font=("times new roman",12,"bold"),text="issuedate:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        textissueDate=Entry(dataframeLeft,textvariable=self.issueDate,font=("times new roman",12,"bold"),width=35)
        textissueDate.grid(row=5,column=1)


        lblExpDate=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Expire date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        textExpDate=Entry(dataframeLeft,textvariable=self.ExpDate,font=("times new roman",12,"bold"),width=35)
        textExpDate.grid(row=6,column=1)


        lblDailydose=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Dailydose:",padx=2,pady=4)
        lblDailydose.grid(row=7,column=0,sticky=W)
        textDailydose=Entry(dataframeLeft,textvariable=self.Dailydose,font=("times new roman",12,"bold"),width=35)
        textDailydose.grid(row=7,column=1)


        lblSideEffects=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffects.grid(row=8,column=0,sticky=W)
        textSideEffects=Entry(dataframeLeft,textvariable=self.SideEffects,font=("times new roman",12,"bold"),width=35)
        textSideEffects.grid(row=8,column=1)

        lblFurtherinfo=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Further info:",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        textFurtherinfo=Entry(dataframeLeft,textvariable=self.Furtherinfo,font=("times new roman",12,"bold"),width=35)
        textFurtherinfo.grid(row=0,column=3)


        
        lblBloodpressure=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Blood pressure:",padx=2,pady=6)
        lblBloodpressure.grid(row=1,column=2,sticky=W)
        textBloodpressure=Entry(dataframeLeft,textvariable=self.Bloodpressure,font=("times new roman",12,"bold"),width=35)
        textBloodpressure.grid(row=1,column=3)


        
        lblStorage=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Storage advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        textStorage=Entry(dataframeLeft,textvariable=self.Storage,font=("times new roman",12,"bold"),width=35)
        textStorage.grid(row=2,column=3)


        lblMedicine=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        textMedicine=Entry(dataframeLeft,textvariable=self.Medicine,font=("times new roman",12,"bold"),width=35)
        textMedicine.grid(row=3,column=3)


        lblPatientid=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Patient id:",padx=2,pady=6)
        lblPatientid.grid(row=4,column=2,sticky=W)
        textPatientid=Entry(dataframeLeft,textvariable=self.Patientid,font=("times new roman",12,"bold"),width=35)
        textPatientid.grid(row=4,column=3)


        lblchssNumber=Label(dataframeLeft,font=("times new roman",12,"bold"),text="CHss number:",padx=2,pady=6)
        lblchssNumber.grid(row=5,column=2,sticky=W)
        textchssNumber=Entry(dataframeLeft,textvariable=self.chssNumber,font=("times new roman",12,"bold"),width=35)
        textchssNumber.grid(row=5,column=3)



        lblPatientname=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        textPatientname=Entry(dataframeLeft,textvariable=self.Patientname,font=("times new roman",12,"bold"),width=35)
        textPatientname.grid(row=6,column=3)


        lblDateofBirth=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        textDateofBirth=Entry(dataframeLeft,textvariable=self.DateofBirth,font=("times new roman",12,"bold"),width=35)
        textDateofBirth.grid(row=7,column=3)


        lblPatientAddress=Label(dataframeLeft,font=("times new roman",12,"bold"),text="Patient address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        textPatientAddress=Entry(dataframeLeft,textvariable=self.PatientAddress,font=("times new roman",12,"bold"),width=35)
        textPatientAddress.grid(row=8,column=3)


#----------------------------------------------------------------Dataframeright--------------------------------------------------------
        self.txtPrescription=Text(dataframeRight,font=("times new roman",12,"bold"),width=50,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

#---------------------------------------Buttons-----------------------------------------------------------------------------------------------------

        btnPrescription=Button(Buttonframe,text="Prescription",fg='white',bg="black",font=("times new roman",12,"bold"),width=23,height=2,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        
        btnPrescriptionData=Button(Buttonframe,text="Presriptedinfo",command=iPrescriptionData(self),fg='white',bg="black",font=("times new roman",12,"bold"),width=23,height=2,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)


        
        btnUpdate=Button(Buttonframe,text="Update",fg='white',bg="green",font=("times new roman",12,"bold"),width=23,height=2,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)


        btnDelete=Button(Buttonframe,text="Delete",fg='black',bg="red",font=("times new roman",12,"bold"),width=23,height=2,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)
        
        
        btnClear=Button(Buttonframe,text="Clear",fg='black',bg="red",font=("times new roman",12,"bold"),width=23,height=2,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        
        btnExit=Button(Buttonframe,text="Exit",fg='black',bg="red",font=("times new roman",12,"bold"),width=23,height=2,padx=2,pady=6)
        btnExit.grid(row=0,column=5)
#----------------------------------------------Tableee----------------------
# scrollbar------------------------------------------------------

        scroll_X=ttk.Scrollbar(detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(detailsframe,colum=("Nametablet","ref"
,"Dose"
,"Notablets"
,"Lot"
,"issueDate"
,"ExpDate"
,"Dailydose"
,"Storage"
,"chssNumber"
,"Patientname"
,"DateofBirth"
,"PatientAddress"
),xscrollcommand=scroll_X.set,yscrollcommand=scroll_y.set)
        scroll_X.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_X=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        

        self.hospital_table.heading("Nametablet",text="Name of table")
        self.hospital_table.heading("ref",text="Reference no")
        self.hospital_table.heading("Dose",text="Dose")
        self.hospital_table.heading("Notablets",text="No of tablets")
        self.hospital_table.heading("Lot",text="Lot")
        self.hospital_table.heading("issueDate",text="Issue-Date")
        self.hospital_table.heading("ExpDate",text="Exp-Date")
        self.hospital_table.heading("Dailydose",text="Dailydose")
        self.hospital_table.heading("Storage",text="Storage")
        self.hospital_table.heading("chssNumber",text="chss-Number")
        self.hospital_table.heading("Patientname",text="Patient-name")
        self.hospital_table.heading("DateofBirth",text="DOB")
        self.hospital_table.heading("PatientAddress",text="Address")


        self.hospital_table["show"]="headings"
        
        

        self.hospital_table.column("Nametablet",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("Dose",width=100)
        self.hospital_table.column("Notablets",width=100)
        self.hospital_table.column("Lot",width=100)
        self.hospital_table.column("issueDate",width=100)
        self.hospital_table.column("ExpDate",width=100)
        self.hospital_table.column("Dailydose",width=100)
        self.hospital_table.column("Storage",width=100)
        self.hospital_table.column("chssNumber",width=100)
        self.hospital_table.column("Patientname",width=100)
        self.hospital_table.column("DateofBirth",width=100)
        self.hospital_table.column("PatientAddress",width=100)
      


        self.hospital_table.pack(fill=BOTH,expand=1)
        


    


      

def iPrescriptionData(self):
        if self.Nametablet.get()=="" or self.ref.get()=="":
                conn=mysql.connector.connect(host='localhost',user='root',passwd='selenophile911',database='mydata', auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Hospital(Nametablet,ref,Notablets,Dose,Lot,issueDate,ExpDate,Dailydose,Storage,chssNumber,Patientname,DateofBirth,PatientAddress) values(%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.Nametablet.get(),
                    self.ref.get(),
                    self.Notablets.get(),
                    self.Dose.get(),
                    self.Lot.get(),
                    self.issueDate.get(),
                    self.ExpDate.get(),
                    self.Dailydose.get(),
                    self.Storage.get(),
                    self.Patientname.get(),
                    self.chssNumber.get(),
                    self.DateofBirth.get(),
                    self.PatientAddress.get()
                    )
                    )
               
        else:
             messagebox.showerror("Error ","all fields are not filled")
        
        
          

                
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Success ","record is inserted")            


root=Tk()
ob=Hospital(root)
root.mainloop()
     





        







        


















        
        








