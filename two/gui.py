# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import sys
import json
import io
import random


class Gui(object):
	
	@staticmethod
	def login():
		# Create instance
		window = tk.Tk()
		# Add a title
		window.title("Main GUI")
		
		# window.geometry("300x200")

		app = Frame(window)
		app.grid(column=0, row=0)
		
		label_phone = Label(app,text="phone :")
		label_phone.grid(column=0, row=0)

		label_passwd = Label(app,text="passwd :")
		label_passwd.grid(column=0, row=1)


		phone = StringVar()
		entry_phone = Entry(app,textvariable = phone)
		entry_phone.grid(column=1, row=0)

		passwd = StringVar()
		entry_passwd = Entry(app,textvariable = passwd)
		entry_passwd.grid(column=1, row=1)

		btn_register = Button(app)
		btn_register.grid(column=0, row=2)
		btn_register.configure(text="register")

		btn = Button(app)
		btn.grid(column=1, row=2)
		#小部件的任何选项都可以通过configure()方法操作
		btn.configure(text = "submit")

		window.mainloop()

if __name__ == '__main__':
	phone = StringVar()
	passwd = StringVar()
	Gui.login()