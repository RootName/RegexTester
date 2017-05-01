#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"
__date__   = "01.05.2017"

from Tkinter import *
import re

def test(string, reString):

	reString = re.compile(reString)
	result   = re.findall(reString, string)

	textRes.delete('1.0', END)

	for res in result:
		textRes.insert(END, res+"\n")

	textRes.insert(END, "-"*40+"\n")


def main():
	global textRes, entryStr, entryRe

	root = Tk()
	root.title("Black Viking | Regex Tester")
	root.tk_setPalette("black")

	labelStr = Label(text="String :", fg="green")
	labelRe  = Label(text="Regex  :", fg="green")
	labelRes = Label(text="Result :", fg="green")

	entryStr = Entry()
	entryRe  = Entry()

	textRes = Text(fg="green")

	button = Button(text="Test", fg="green", command = lambda: test(entryStr.get(), entryRe.get()))

	labelStr.pack()
	entryStr.pack()

	labelRe.pack()
	entryRe.pack()

	labelRes.pack()
	textRes.pack()

	button.pack()

	root.mainloop()

if __name__ == "__main__":
	main()
