from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("courier",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"images\face-600x900.png")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        img_bottom=Image.open(r"images\facedetection.jpg")
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)

        b1_1=Button(f_lbl,text="Face recognition",command=self.face_recog,cursor="hand2",font=("courier",15,"bold"),bg="navy blue",fg="white")
        b1_1.place(x=365, y=600, width=200,height=60)

    #attendance
    def mark_attendance(self,i,r,n,d):
        already_in_file=set()
        with open("attendancesheet.csv","r+",newline="\n") as f:
            for line in f:
                already_in_file.add(line.split(",")[0])
            if((i not in already_in_file) and (r not in already_in_file) and (n not in already_in_file) and (d not in already_in_file)):
                with open("attendancesheet.csv","r+",newline="\n") as f:
                    now=datetime.now()
                    d1=strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
            
            # myDataList=f.readlines()
            # name_list=[]
            # for line in myDataList:
            #     entry=line.split((","))
            #     name_list.append(entry[0])
            # if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)): #means agr already ye wale record excel sheet me na ho to hi attendance lge
            #     now=datetime.now()
            #     d1=strftime("%d/%m/%Y")
            #     dtString=now.strftime("%H:%M:%S")
            #     f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


        #face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,minNeigbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeigbour) #img k features

            coords=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300))) #img wahi hai or nhi

                conn=mysql.connector.connect(host="localhost",user="root",password="preksha",database="face_recognizer",auth_plugin="mysql_native_password")
                mycursor=conn.cursor()

                mycursor.execute("select Name from student where Student_id="+str(id))
                n=mycursor.fetchone()
                n="+".join(n)

                mycursor.execute("select Roll from student where Student_id="+str(id))
                r=mycursor.fetchone()
                r="+".join(r)

                mycursor.execute("select Dep from student where Student_id="+str(id))
                d=mycursor.fetchone()
                d="+".join(d)

                mycursor.execute("select Student_id from student where Student_id="+str(id))
                i=mycursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coords=[x,y,w,y]
                
            return coords
            
        def recognize(img,clf,faceCascade):
            coords=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
            
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videocap=cv2.VideoCapture(0)

        while True:
            ret,img=videocap.read()
            ret=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",ret)

            if cv2.waitKey(1)==13:      #jbtk enter na dabaaye, camera will be open
                break
        videocap.release()
        cv2.destroyAllWindows()
                



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()