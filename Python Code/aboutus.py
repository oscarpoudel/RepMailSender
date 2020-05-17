from tkinter import *
from tkinter.font import Font

class AboutUs(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("About us")
        myinfo='''
        Name: Oscar Poudel
        Email: opoudel27@gmail.com
        Occupation: Student and a computer enthusiast


        '''
        self.label=Label(self,text=myinfo,justify="left").pack(side=LEFT)
        self.resizable(False,False)
        self.label.pack()