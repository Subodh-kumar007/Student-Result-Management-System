from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os
class Register:
     def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #======bg_Img============>
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg_img=Label(self.root,image=self.bg).place(x=250,y=0,relheight=1,relwidth=1)
        #======left_Img============>
        self.left=ImageTk.PhotoImage(file="images/side.png")
        img_left=Label(self.root,image=self.left).place(x=80,y=100,height=500,width=400)
        #=========register Frame======>
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        #=======Variables=======>
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_ques=StringVar()
        self.var_ans=StringVar()
        self.var_pass=StringVar()
        self.var_conpass=StringVar()
        #-------------------Row 1------------------------------------
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_fname).place(x=50,y=130,width=250)
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_lname).place(x=370,y=130,width=250)
        #-------------------Row 2------------------------------------
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_contact).place(x=50,y=200,width=250)
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_email).place(x=370,y=200,width=250)
        #-------------------Row 3------------------------------------
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        cmb_question=ttk.Combobox(frame1,font=("times new roman",12),state="readonly",justify=CENTER,textvariable=self.var_ques)
        cmb_question['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        cmb_question.place(x=50,y=270,width=250)
        cmb_question.current(0)
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_ans).place(x=370,y=270,width=250)
        #-------------------Row 4------------------------------------
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_pass).place(x=50,y=340,width=250)
        cpassword=Label(frame1,text="Conform Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_conpass).place(x=370,y=340,width=250)
        #---------------terms------------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="images/register.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        btn_login=Button(root,text="Sign In",font=("times new roman",20),bd=0,cursor="hand2",command=self.signin).place(x=200,y=460,width=180)

     #=========function============>
     def clear(self):
          self.var_fname.set("")
          self.var_lname.set("")
          self.var_contact.set("")
          self.var_email.set("")
          self.var_ques.set("Select")
          self.var_ans.set("")
          self.var_pass.set("")
          self.var_conpass.set("")
   
     def register_data(self):
          if self.var_fname.get()=="":
                 messagebox.showerror("Error","First Name is Required",parent=self.root)
          elif self.var_contact.get()=="":
               messagebox.showerror("Error","Contact is Required",parent=self.root)
          elif self.var_email.get()=="":
               messagebox.showerror("Error","Email is Required",parent=self.root)
          elif self.var_ques.get()=="Select":
               messagebox.showerror("Error","Select the Question",parent=self.root)
          elif self.var_ans.get()=="":
               messagebox.showerror("Error","Answer is Required",parent=self.root)
          elif self.var_pass.get()=="":
               messagebox.showerror("Error","Password is Required",parent=self.root)
          elif self.var_conpass.get()=="":
               messagebox.showerror("Error","Conform Password is Required",parent=self.root)
          elif self.var_pass.get()!=self.var_conpass.get():
               messagebox.showerror("Error","Password & Conform Password should be Same",parent=self.root)
          elif self.var_chk.get()==0:
               messagebox.showerror("Error","Please Agree Our Terms & Condition",parent=self.root)
          else:
               try:
                    con=sqlite3.connect(database="srms.db")
                    cur=con.cursor()
                    cur.execute("select * from employee where email=?",(self.var_email.get(),))
                    row=cur.fetchone()
                    if row!=None:
                         messagebox.showerror("Error","User Already Exist, Please Try With Another Email",parent=self.root)
                    else:
                         cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                                     (self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_ques.get(),
                                      self.var_ans.get(),self.var_pass.get()
                                      ))
                         con.commit()
                         con.close()
                         messagebox.showinfo("Success","Register Successfull",parent=self.root)
                         self.clear()
                         self.signin()
               except Exception as es:
                    messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

     def signin(self):
          self.root.destroy()
          os.system("python login.py")            
             
#=======Main==============>
root=Tk()
obj=Register(root)
root.mainloop()