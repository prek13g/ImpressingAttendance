from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
import os #as we have to take photos from directory accessible from our operating system
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from help import Help

class Face_Recognition_System:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

#header img1
        img=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\header1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
#header img2
        img1=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\header2.webp")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
#header img3
        img2=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\header3.webp")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

#bg img
        bgimg=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\bg.jpg")
        bgimg=bgimg.resize((1530,710),Image.ANTIALIAS)
        self.photobgimg=ImageTk.PhotoImage(bgimg)
        bg_img=Label(self.root,image=self.photobgimg)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("courier",35,"bold"),bg="white",fg="navy blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #time
        def time():
            string = strftime('%H:%M:%S %p') #%p is for meridian
            lbl.config(text=string) #config similar to pack
            lbl.after(1000,time) #1000 ms
        
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='navy blue')
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()

#buttons 
#student button
        img4=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\stdetail.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
        b1.place(x=200, y=100, width=180,height=180)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("courier",13,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=200, y=250, width=180,height=40)

#face detector
        img5=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\face-600x900.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,command=self.face_recognition,cursor="hand2")
        b1.place(x=500, y=100, width=180,height=180)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_recognition,cursor="hand2",font=("courier",13,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=500, y=250, width=180,height=40)

#attendance 
        img6=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\att.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,command=self.attendance,cursor="hand2")
        b1.place(x=800, y=100, width=180,height=180)

        b1_1=Button(bg_img,text="Attendance",command=self.attendance,cursor="hand2",font=("courier",13,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=800, y=250, width=180,height=40)

#help desk
        img7=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\helpdesk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,command=self.help_data,cursor="hand2")
        b1.place(x=1100, y=100, width=180,height=180)

        b1_1=Button(bg_img,text="Help Desk",command=self.help_data,cursor="hand2",font=("courier",13,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=1100, y=250, width=180,height=40)

#train data
        img8=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\traindata.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=200, y=400, width=180,height=180)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("courier",13,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=200, y=540, width=180,height=40)

#photos
        img9=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\phot.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500, y=400, width=180,height=180)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("courier",13,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=500, y=540, width=180,height=40)        

#exit
        img10=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\exit.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimg10,command=self.exit,cursor="hand2")
        b1.place(x=800, y=400, width=180,height=180)

        b1_1=Button(bg_img,text="Exit",command=self.exit,cursor="hand2",font=("courier",13,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=800, y=540, width=180,height=40)

    def open_img(self):
        os.startfile("data")   

    def exit(self):
        self.exit=messagebox.askyesno("Face Recognition","Are you sure you want to exit!!",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return         

#functions buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)   

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

