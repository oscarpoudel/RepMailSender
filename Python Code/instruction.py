from tkinter import *
from tkinter.font import Font

class Instruction(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("instructions")
        #self.inst_window = self.Toplevel()
        self.scnew = Scrollbar(self)
        self.scnew.pack(side=RIGHT, fill=Y)
        inst = '''
(Highlight over text and Press ctrl+c to copy)

1.Enable allow less secure app at:https://myaccount.google.com/lesssecureapps and check your mail
  for critical activity mail ,open it ,click on check activity and select yes it was me...
2.Enter your correct email and password and click sign in test if test was sucess proceed further..
3.Bulk paste receiver email address
4.Type subject and body in their respective box
5.Click Send and look at logs for status.

This program was created with main goal to send multiple mail  to multiple
high profile medias with issue regarding border dispute between Nepal and India.
Sample receiver mail, subject and body are given below.

receiver mail:
community@cnn.com
hannity@foxnews.com
news@skynews.com
msnbc.digital.editors@nbcuni.com
contact.doc@aljazeera.net
newmedia@euronews.com
editor.english@alarabiya.net

subject:
   Border Encroachment of Nepal by India

Body:
Dear Editorial Team,

I would like to draw your kind attention on the issue that India has been beaching the border
agreement with Nepal and it denying for peaceful negotiation since long before.India has recently
inaugurated the roadway in Lipulekh area of Nepal without bilateral understanding and is claiming
the land as theirs breaching the agreement made in Sugauli Treaty.The land belongs to Nepal not
only as per bilateral treaties (between Nepal & India) but also this fact has been recognised in
other documents including treaty between Nepal and China in the past.

So it is my utmost requestto you to cover this matter as fairly as possible.
           '''
        self.ins_t = Text(self, height=30, width=100, wrap=WORD, font=Font(family="Helvetica"),padx=40,yscrollcommand=self.scnew.set)
        self.ins_t.insert(1.0,inst)
        self.ins_t.tag_add("here", "4.0", "10.0")
        self.ins_t.tag_config("here", background="yellow")
        self.ins_t.tag_add("fist", "2.0", "3.0")
        self.ins_t.tag_config("fist", background="#F5B041")
        self.ins_t.pack()
        self.scnew.config(command=self.ins_t.yview)
        self.geometry('1000x700+50+50')
        self.ins_t.configure(state="disabled")