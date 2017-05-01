#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Black Viking"
__date__   = "01.05.2017"

from Tkinter import *
import re

class Program:
    def __init__(self):
        self.root = Tk()
        self.root.title("Black Viking | Regex Tester")
        self.root.tk_setPalette("black")

        self.bilgiBanner=Label(text="Regular Expression Tester",bg="green",fg="black")
        self.bilgiBanner.pack(side=TOP,fill=X)
        
        self.labelStr = Label(text="Yazı", fg="green")
        self.labelRe  = Label(text="Regex", fg="green")
        self.labelRes = Label(text="Sonuç", fg="green")

        self.entryStr = Entry()
        self.entryRe  = Entry()
        self.entryRe.bind("<Key>",self.test) # herhangi bir tuşa basılırsa, test metodu çalışsın

        self.textRes = Text(fg="green")

##        self.button = Button(text="Test", fg="green", command = lambda: test(entryStr.get(), entryRe.get()))
##        self.button.pack()
        
        self.labelStr.pack()
        self.entryStr.pack()
        self.labelRe.pack()
        self.entryRe.pack()
        self.labelRes.pack()
        self.textRes.pack()

        
        self.root.mainloop()

    def test(self,event=None):
        try:
            reString=self.entryRe.get()
            string=self.entryStr.get()
            reString = re.compile(reString)
            result   = re.findall(reString, string)
            self.textRes.delete('1.0', END)
            for res in result:
                self.textRes.insert(END,res+"\n")
            self.textRes.insert(END,("\n"+(40*"_")))
        except Exception,e:
            #print(e)
            pass
        

Program()
