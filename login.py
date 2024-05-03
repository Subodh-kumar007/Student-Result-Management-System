from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
from tkinter import messagebox
import sqlite3
import os
from forget import Forget_pass
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")  
        #=======backgroung colours=========>
        left_lbl=Label(self.root,bg="#08A3D2",bd=0).place(x=0,y=0,relheight=1,width=600)
        right_lbl=Label(self.root,bg="#031F3C",bd=0).place(x=600,y=0,relheight=1,relwidth=1)    
        #==========Frames=============>
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,height=500,width=800)
        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)
        password=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_password=Entry(login_frame,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_password.place(x=250,y=280,width=350,height=35)

        but_reg=Button(login_frame,text="Register New Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857",cursor="hand2",command=self.register).place(x=250,y=320)
        but_forget=Button(login_frame,text="Forget Password!",font=("times new roman",14),bg="white",bd=0,fg="red",cursor="hand2",command=self.forget).place(x=450,y=320)
        but_login=Button(login_frame,text="Login",font=("times new roman",20),fg="white",bg="#B00857",cursor="hand2",command=self.login).place(x=250,y=380,width=180,height=40)
        #=======Clock label=========>
        self.lbl=Label(self.root,text="\nAnalog Clock",font=("Book Antiqua",25,"bold"),bg="#081923",fg="white",compound=BOTTOM,bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        self.working()

    #========Function===========>
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="srms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python deshboard.py")
                    con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

    def clock_image(self,hr,mint,secn):
        cloks=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(cloks)
        #=======for clock Image======>
        bg=Image.open("images/c.png")
        bg=bg.resize((300,300),Image.Resampling.LANCZOS)
        cloks.paste(bg,(50,50))
        origin=200,200
        
        #formula t rotate the clock
        #angle_in_radians= angle_in_degrees * math.pi/180
        #line_length=100
        #center_x= 250
        #center_y= 250
        #end_x= center_x + line_length * math.sin(angle_in_radians)
        #end_y= center_y - line_length * math.cos(angle_in_radians)
        #=========hour line image===========>
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #=========Min line image===========>
        draw.line((origin,200+80*sin(radians(mint)),200-80*cos(radians(mint))),fill="white",width=3)
        #=========Sec line image===========>
        draw.line((origin,200+110*sin(radians(secn)),200-110*cos(radians(secn))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        cloks.save("images/new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        mint=(m/60)*360
        secn=(s/60)*360
        self.clock_image(hr,mint,secn)
        #self.img=Image.open("images/new.png")
        self.img=ImageTk.PhotoImage(file="images/new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
    
    def register(self):
        self.root.destroy()
        os.system("python register.py")
    
    def forget(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to Reset Your Password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="srms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Enter the Valid Email to Reset Your Password",parent=self.root)
                else:
                    
                    self.senEmail=self.txt_email.get()
                    self.new_win=Toplevel(self.root)
                    self.new_obj=Forget_pass(self.new_win,self.senEmail)
                    self.clear()
                    con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

    def clear(self):
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)

#=======Main==============>
root=Tk()
obj=Login(root)
root.mainloop()
