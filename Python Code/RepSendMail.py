from tkinter import *
from tkinter.font import Font
from instruction import Instruction
from aboutus import AboutUs
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
from tkinter import messagebox
import os
import sys

class Application(object):
    def __init__(self,master):
        self.master = master
        #Frames
        self.top=Frame(master,height=500,width=800,bg = '#FBFCFC',highlightbackground='black',highlightthickness=2)
        self.top.pack(side=TOP)
        self.rightbottom=Frame(master,width=400,height=200,bg ='#FDEBD0',highlightbackground='black',highlightthickness=1)
        self.rightbottom.pack(side=RIGHT,fill=Y)
        self.leftbottom=Frame(master,width=400,height=200,bg='#FBFCFC',highlightbackground='black',highlightthickness=1)
        self.leftbottom.pack(side=LEFT,fill=Y)
        #Topframedesign
        ''' def resource_path(relative_path):
            """ Get absolute path to resource, works for dev and for PyInstaller """
            try:
                # PyInstaller creates a temp folder and stores path in _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        self.icon1 = resource_path("icons8-mail-contact-48.png")
        self.icon2=resource_path("icons8-nepal-48.png")

        self.icon_label1=Label(self.top,image=self.icon1,bg="#FBFCFC").place(x=10,y=7)
        self.icon_label2=Label(self.top,image=self.icon2,bg="#FBFCFC").place(x=740,y=7)'''
        my_font = Font(family="Segoe Print", size=17,weight="bold")
        self.toplabel = Label(self.top, text="Repeated Mail sender By Oscar!!!",bd=0,bg='#FBFCFC', font=my_font, relief=RAISED)
        self.toplabel.place(x=210,y=10)
        self.line1 = Canvas(self.top,bg='#FBFCFC',width=800,height=5,bd=0,highlightthickness=0)
        self.line1.create_line(10, 4, 775, 4)
        self.line1.place(x=10, y=58)
        self.topic=Label(self.top,text="Enter your credentials:",font='Leelawadee 13',bg='#FBFCFC').place(x=30,y=70)
        self.enter_mail=Label(self.top,text="Mail:",font='Verdana 12 ',bg='#FBFCFC').place(x=30,y=100)
        self.mail_entry=Entry(self.top,width=30,bd=1,bg='white',highlightthickness=1, highlightbackground="#5D6D7E")
        self.mail_entry.place(x=120,y=100)

        self.enter_password = Label(self.top, text="Password:",font='Verdana 12',bg='#FBFCFC').place(x=30, y=130)
        self.passwd_entry = Entry(self.top, width=30, bd=1, bg='white',highlightthickness=1, highlightbackground="#5D6D7E")
        self.passwd_entry.place(x=120, y=130)
        lol_font = Font(family="Monotype Corsiva",size=12,weight="bold")
        lol_font2 = Font(family="Comic Sans MS", size=12, weight="bold")
        self.stop_value=0
        self.signin=Button(self.top,text="Sign in Check",font=lol_font,bg="#2671FF",fg='white',command=self.process2).place(x=120,y=160)
        self.line2 = Canvas(self.top,bg='#FBFCFC',width=5,height=120,bd=0,highlightthickness=0)
        self.line2.create_line(1, 1, 1,110)
        self.line2.place(x=400, y=75)
        self.sub_label=Label(self.top,text="Subject:",font='Verdana 12',bg='#FBFCFC').place(x=30,y=210)
        self.sub_entry=Entry(self.top,width=79, bd=1, bg='white',highlightthickness=1, highlightbackground="#5D6D7E")
        self.sub_entry.place(x=120, y=210)
        self.body_label = Label(self.top,text="Body:", font='Verdana 12', bg='#FBFCFC').place(x=30, y=250)
        self.body_text=Text(self.top,width=59,height=10,bg='white',wrap=WORD,highlightthickness=1, highlightbackground="#5D6D7E")
        self.body_text.place(x=120,y=250)
        self.rec=Label(self.top,text='Enter receiver addresses:',font='Leelawadee 13',bg='#FBFCFC').place(x=420,y=70)
        self.line3 = Canvas(self.top, bg='#FBFCFC', width=800, height=5, bd=0, highlightthickness=0)
        self.line3.create_line(10, 4, 775, 4)
        self.line3.place(x=10, y=195)
        self.reciv_mail=Text(self.top,height=5,width=40,bg='white',highlightthickness=1, highlightbackground="#5D6D7E")
        self.reciv_mail.place(x=420,y=100)
        self.loop_label=Label(self.top,text="Enter no of times to mail:",font="Leelawadee 10",bg="#F1948A").place(x=620,y=210)
        self.loop_entry=Text(self.top,width=3,height=1,bg='white',padx=40,pady=40,relief=RIDGE,font="Arial 25 italic",highlightthickness=1, highlightbackground="#5D6D7E")
        self.loop_entry.place(x=620,y=240)
        self.stop_send = Button(self.top, text="STOP", bg='red',font='bold',fg='white', command=self.stop,height=1,width=5,bd=10).place(x=707,y=430)
        #left_bottom_instruction
        self.ins_button=Button(self.leftbottom,text="INSTRUCTIONS",command=self.openwindow,height=5,width=20,bd=1,bg="#E67E22",font=Font(size=12,family="Lato"))
        self.ins_button.place(x=80,y=30)
        self.about_button=Button(self.leftbottom,text="about us",fg='blue',bg='#ABEBC6',command=self.about_us).place(x=80,y=160)
        self.send_button=Button(self.top,text="SEND THE MAIL!!!",fg='white',bd=10,width=60,height=1,font=lol_font2,bg='#2671FF',command=self.process1 ).place(x=70,y=430)
        #right_bottom_logs
        self.log_heading=Label(self.rightbottom,text="LOGS",bg='#FDEBD0',font="Arial 14 bold underline").place(x=150,y=0)
        self.scroll=Scrollbar(self.rightbottom)
        self.scroll.place(x=380,y=20,height=178)
       #self.scroll.pack(sid=LEFT,fill=Y)
        self.log_text=Text(self.rightbottom,height=10,width=51,font='Verenda 10',bg='#F9E79F',yscrollcommand=self.scroll.set,padx=10,pady=10,wrap=WORD)
        self.scroll.config(command=self.log_text.yview)
        self.log_text.place(x=0,y=23)
        #self.log_text.configure(state='disabled')
        #print(self.mail, self.password)


    def sign_in(self):
        self.log_text.insert(1.0,"\nWaiting....for sign in test\n")
        sender_address=self.mail_entry.get()
        sender_pass=self.passwd_entry.get()
        print(sender_pass,sender_address)
        mail_content = '''login check'''
        receiver_address = ['oscar.poudel123@gmail.com']

        try:
            # Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            for y in range(0, 1):
                for x in range(0, len(receiver_address)):
                    message['To'] = receiver_address[x]
                    message['Subject'] = 'login check'  # The subject line
                    # The body and the attachments for the mail
                    message.attach(MIMEText(mail_content, 'plain'))
                    # Create SMTP session for sending the mail
                    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
                    session.starttls()  # enable security
                    session.login(sender_address, sender_pass)  # login with mail_id and password
                    text = message.as_string()
                    session.sendmail(sender_address, receiver_address[x], text)
                    session.quit()
                    self.log_text.insert(1.0,"\nSign in test Successful\n")


        except:
            self.log_text.insert(1.0,"\ntest failed:Click on Instructions/Please check your internet connections\n")

    def send_mail(self):
        self.log_text.insert(1.0,"\nWaiting....for sending mail\n")
        time.sleep(2)
        sender_address = self.mail_entry.get()
        sender_pass = self.passwd_entry.get()
        mail_content = self.body_text.get(1.0,END)
        receiver_bulk = self.reciv_mail.get(1.0,END)
        receiver_address=receiver_bulk.split()
        try:
         loop=int(self.loop_entry.get(1.0,END))
         self.log_text.insert(1.0,"\nThe Entered loop is interger so proceding forward\n")
        except:
         self.log_text.insert(1.0,"\nThe Entered loop value is not integer or the other data field empty...Enter again\n")
         return
        try:
            # Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            for y in range(0, loop):
                if (self.stop_value == 1):
                    self.stop_value = 0
                    self.log_text.insert(1.0, '\nStopped:\n')
                    break
                for x in range(0, len(receiver_address)):
                        message['To'] = receiver_address[x]
                        message['Subject'] = self.sub_entry.get()  # The subject line
                        # The body and the attachments for the mail
                        message.attach(MIMEText(mail_content, 'plain'))
                        # Create SMTP session for sending the mail
                        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
                        session.starttls()  # enable security
                        session.login(sender_address, sender_pass)  # login with mail_id and password
                        text = message.as_string()
                        session.sendmail(sender_address, receiver_address[x], text)
                        session.quit()
                        true_result="\nmail sent:%s [%d]"%(receiver_address[x],y+1)+'\n'
                        self.log_text.insert(1.0,true_result)
                        if(x==len(receiver_address)):
                            x=0
        except:
            self.log_text.insert(1.0,"\nmail not sent: Check all the data you entered and try again\n")

    def process1(self):
        p1=threading.Thread(target=self.send_mail)
        p1.start()

    def process2(self):
        p1=threading.Thread(target=self.sign_in)
        p1.start()
    def stop(self):
        self.log_text.insert(1.0,'\nStopping all Processes\n')
        self.stop_value=1



    def openwindow(self):
            callid=Instruction()
    def about_us(self):
            callid=AboutUs()


def main():
    def on_close():
        close = messagebox.askyesno("exit", "Would you really like to exit??")
        if close == True:
            root.quit()
    root=Tk()
    app=Application(root)
    root.title("Repeated Mail Sender")
    root.protocol("WM_DELETE_WINDOW",on_close)
    root.geometry("800x700+400+50")
    root.resizable(False,False)
    #root.configure(bg='#D2B4DE')
    root.mainloop()

if __name__ == '__main__':
    main()