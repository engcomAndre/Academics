__author__ = 'ANDRE'
from Tkinter import *

class Application():
    def __init__(self,master = NONE):
        Frame.__init__(self,master = NONE):
        self.msg = Label(self,master)
        self.msg.pack()
        self.bye.pack()
        self.pack()

app = Application

