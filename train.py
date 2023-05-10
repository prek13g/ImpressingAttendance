from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("courier",35,"bold"),bg="maroon",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"images\header2.webp")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("courier",30,"bold"),bg="maroon",fg="white")
        b1_1.place(x=0, y=380, width=1530,height=60)

        img_bottom=Image.open(r"images\header2.webp")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data") #relative path of the folder containing the photo samples
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image, Image imported from pil
            imageNp=np.array(img,'uint8') #image converted into gray scale
            id=int(os.path.split(image)[1].split('.')[1]) #jaise user1.1.jpg to user1.100 hai 100 images hmari toh this will store 1 to 100 in id

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13 #window close hojaygi
        ids=np.array(ids) #for converting into array, numpy gives 88% better performance other than usual

        #train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create() #we stored this algorithm in this algorithm in this variable
        clf.train(faces,ids)
        clf.write("classifier.xml") #jo data train hua hai, wo classifier.xml me store hogya in the form of binary numbers
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")





if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()