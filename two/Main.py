# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import sys
import json
import io
import random




if __name__ == '__main__':
	# Create instance
	window = tk.Tk()
	# Add a title
	window.title("Main GUI")
	
	# window.geometry("300x200")

	app = Frame(window)
	app.grid(column=0, row=0)


	label_phone = Label(app,text="phone :")
	label_phone.grid(column=0, row=0)

	label_code = Label(app,text="code :")
	label_code.grid(column=0, row=1)


	phone = StringVar()
	entry_phone = Entry(app,textvariable = phone)
	entry_phone.grid(column=1, row=0)

	code = StringVar()
	entry_code = Entry(app,textvariable = code)
	entry_code.grid(column=1, row=1)


	# Button click Event Function
	def click_me():
		t = tk.Tk()
		t.title("Main GUI")
		t.mainloop()
		# phone.set("hhhh")
		# label.configure(text=phone.get())
		print(string)

	btn = Button(window,command=click_me)
	btn.grid(column=0, row=1)
	#小部件的任何选项都可以通过configure()方法操作
	btn.configure(text = "submit")


	# Start GUI
	window.mainloop()