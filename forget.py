from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
class Forget_pass:
    def __init__(self,root,email):
        self.root=root
        self.email=email
        self.root.title("Forget Password")
        self.root.geometry("350x400+500+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.grab_set()
        t=Label(self.root,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
        #=============Forget password===============>

        self.var_ques=StringVar()
        self.var_ans=StringVar()
        self.var_Npass=StringVar()

        question=Label(root,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=70)
        cmb_question=ttk.Combobox(root,font=("times new roman",12),state="readonly",justify=CENTER,textvariable=self.var_ques)
        cmb_question['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        cmb_question.place(x=50,y=100,width=250)
        cmb_question.current(0)

        answer=Label(root,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=150)
        txt_answer=Entry(root,font=("times new roman",15),bg="lightgray",textvariable=self.var_ans).place(x=50,y=180,width=250)
        new_pass=Label(root,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=230)
        txt_new_pass=Entry(root,font=("times new roman",15),bg="lightgray",textvariable=self.var_Npass).place(x=50,y=260,width=250)

        but_change_password=Button(root,text="Reset Password",font=("times new roman",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.forgetpassword).place(x=80,y=320)

#============Function=========>
    def clear(self):
        self.var_ques.set("Select")
        self.var_ques.set("")
        self.var_Npass.set("")

    def forgetpassword(self):
        if self.var_ans.get()=="Select" or self.var_ans.get()=="" or self.var_Npass.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="srms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",(self.email,self.var_ques.get(),self.var_ans.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select the Correct Security Question / Enter Answer",parent=self.root)
                else:
                    cur.execute("update employee set password=? where email=?",(self.var_Npass.get(),self.email))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your Password has been reset, Please Login with New password",parent=self.root)
                    self.clear()
                    self.root.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

#=======Main==============>
if __name__=="__main__":
    root=Tk()
    e=""
    obj=Forget_pass(root,e)
    root.mainloop()
