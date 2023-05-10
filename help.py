from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import webbrowser

class Help:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("help desk")

        def open_url(url):
            webbrowser.open_new_tab(url)

        title_lbl=Label(self.root,text="HELP DESK",font=("courier",35,"bold"),bg="white",fg="navy blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"D:\Users\Preksha Dixit\faceRecognition2\images\helpbg.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_lbl=Label(f_lbl,text="Email:prekshadixit21@gmail.com",font=("courier",20,"bold"),bg="white",fg="navy blue")
        dev_lbl.place(x=500,y=300)

        url='prekshadixit21@gmail.com'

        f_lbl.bind("<Button-1>",lambda e:open_url(url))

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()