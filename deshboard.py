from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
import sqlite3
from datetime import *
import time
from math import *
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1450x750+0+0")
        self.root.config(bg="white")
        #====icons=====>
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        #====Title====>
        title=Label(self.root,text="Student Result Managment System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #====Menu====>
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exits).place(x=1120,y=5,width=200,height=40)

        #=====content window====>
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #====updata_details=====>
        self.lbl_course=Label(self.root,text="Total courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,height=100,width=300)
        self.lbl_student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,height=100,width=300)
        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,height=100,width=300)

        #=======Clock label=========>
        self.lbl=Label(self.root,text="\nAnalog Clock",font=("Book Antiqua",25,"bold"),bg="#081923",fg="white",compound=BOTTOM,bd=0)
        self.lbl.place(x=20,y=180,height=450,width=350)
        self.working()
        #====Footer====>
        footer=Label(self.root,text="SRMS-Student Result Managment System\nContact Us for any Technical Issue: 981xxxx450",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update()

#========Functions==============>
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)
    
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to Logout ?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
    
    def exits(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit ?",parent=self.root)
        if op==True:
            self.root.destroy()

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
        
    def update(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Course\n[{str(len(cr))}]")

            cur.execute("select * from student")
            st=cur.fetchall()
            self.lbl_student.config(text=f"Total Student\n[{str(len(st))}]")
            
            cur.execute("select * from results")
            rs=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(rs))}]")
            
            self.lbl_course.after(200,self.update)
            con.close()                     
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#=======Main==============>
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()