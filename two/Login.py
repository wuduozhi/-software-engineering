# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from User import User
from Message import Message
import hashlib
import re
import sys
import json
import io
import random

class Login(object):
	"""docstring for Login"""
	def __init__(self):
		super(Login, self).__init__()
		self.code = None

	def loginCommand(self):
		phone = self.phone.get()
		passwd = self.passwd.get()
		if phone.strip() == "" or passwd.strip() == "":
			self.warning("LOGIN WARNING",'请输入电话号码与密码')
		else:
			md5 = hashlib.md5()  # 密码MD5加密存储
			md5.update(passwd.encode(encoding='utf-8'))
			if User.validate(phone=phone,passwd = md5.hexdigest()) == True:
				self.warning("LOGIN MESSAGE",'登录成功','green')

	# 登录界面
	def loginGUI(self):
		self.LOGIN = tk.Tk()
		self.LOGIN.title("Main GUI")
		app = Frame(self.LOGIN)
		app.grid(column=0, row=0)
		label_phone = Label(app,text="phone :")
		label_phone.grid(column=0, row=0)
		label_passwd = Label(app,text="passwd :")
		label_passwd.grid(column=0, row=1)

		self.phone = StringVar()
		entry_phone = Entry(app,textvariable = self.phone)
		entry_phone.grid(column=1, row=0)
		self.passwd = StringVar()
		entry_passwd = Entry(app,textvariable = self.passwd)
		entry_passwd.grid(column=1, row=1)

		btn = Frame(self.LOGIN)
		btn.grid(column=0, row=1)

		btn_register = Button(btn,command=self.registerGUI)
		btn_register.grid(column=0, row=2)
		btn_register.configure(text="register")
		btn_submit = Button(btn,command=self.loginCommand)
		btn_submit.grid(column=1, row=2)
		#小部件的任何选项都可以通过configure()方法操作
		btn_submit.configure(text = "submit")
		self.LOGIN.mainloop()


	def registerGUI(self):
		self.REGISTER = tk.Tk()
		self.REGISTER.title("REGISTER GUI")

		label = Frame(self.REGISTER)
		label.grid(column=0, row=0)

		# 标签
		label_phone = Label(label,text="phone :")
		label_phone.grid(column=0, row=0)
		label_code = Label(label,text="code :")
		label_code.grid(column=0, row=1)
		label_passwd = Label(label,text="passwd :")
		label_passwd.grid(column=0, row=2)
		label_passwd_again = Label(label,text="passwd again :")
		label_passwd_again.grid(column=0, row=3)


		# 输入框
		self.register_phone = StringVar()
		entry_phone = Entry(label,textvariable = self.register_phone)
		entry_phone.grid(column=1, row=0)
		self.code_input = StringVar()
		entry_code = Entry(label,textvariable = self.code_input)
		entry_code.grid(column=1, row=1)
		self.register_passwd = StringVar()
		entry_passwd = Entry(label,textvariable = self.register_passwd)
		entry_passwd.grid(column=1, row=2)
		self.register_passwd_again = StringVar()
		entry_passwd_again = Entry(label,textvariable = self.register_passwd_again)
		entry_passwd_again.grid(column=1, row=3)

		# 按钮
		btn = Frame(self.REGISTER)
		btn.grid(column=0, row=1)

		btn_code = Button(btn,command=self.sendCode)
		btn_code.grid(column=0, row=0)
		btn_code.configure(text="code")
		btn_register = Button(btn,command=self.registerCommand)
		btn_register.grid(column=1, row=0)
		#小部件的任何选项都可以通过configure()方法操作
		btn_register.configure(text = "register")

		self.REGISTER.mainloop()

	def codeWarning(self,message,color="red"):
		warning = tk.Tk()
		warning.title("Code Warning")
		label_warning = Label(warning,text=message)
		label_warning.configure(foreground=color)
		label_warning.pack()
		# label_warning.configure(text='A Red Label')
		warning.mainloop()

	def sendCode(self):
		warningTitle = "CODE WARNING"
		if self.code != None:
			self.warning(warningTitle,"您已经发送过验证码","red")
			return

		phone = self.register_phone.get()
		# 验证手机号是否正确
		is_phone = re.match(r"^1[35678]\d{9}$", phone)
		if is_phone :
			code = self.getCode(6)
			result = Message.get_instance().send_code(code=code,phone=phone)
			if result['statusCode'] == 200:
				self.warning(warningTitle,result['message'],"green")
			else:
				self.warning(warningTitle,result['message'],"red")
		else:
			self.warning(warningTitle,"请输入正确的电话号码","red")

	# 生成验证码
	def getCode(self,length = None):
		li = []
		for i in range(length): #循环6次,生成6个字符
			r = random.randrange(0, 5) #随机生成0-4之间的数字
			if r == 1 or r == 4:  #如果随机数字是1或者4时,生成0-9的数字
				num = random.randrange(0, 9)
				li.append(str(num))
			else:  #如果不是1或者4时,生成65-90之间的数字
				temp = random.randrange(65, 91)
				char = chr(temp)  #将数字转化为ascii列表中对应的字母
				li.append(char)
		
		r_code = ''.join(li)  #6个字符拼接为字符串
		self.code = r_code   # 保存code
		return r_code
	
	def warning(self,title,message,color="red"):
		warning = tk.Tk()
		warning.title(title)
		label_warning = Label(warning,text=message)
		label_warning.configure(foreground=color)
		label_warning.pack()
		# label_warning.configure(text='A Red Label')
		warning.mainloop()


	def registerCommand(self):
		warningTitle = "REGISTER WARNING"
		phone = self.register_phone.get()
		passwd = self.register_passwd.get()
		passwd_again = self.register_passwd_again.get()
		code_input = self.code_input.get()
		if passwd == '' or passwd_again=='' or passwd != passwd_again :
			self.warning(warningTitle,"两次密码输入不正确")
		elif self.code != code_input :
			self.warning(warningTitle,"请输入正确的手机验证码")
		else:
			md5 = hashlib.md5()  # 密码MD5加密存储
			md5.update(passwd.encode(encoding='utf-8'))
			User.add(phone=phone,passwd=md5.hexdigest())
			self.warning(warningTitle,"注册成功",'green')





if __name__ == '__main__':
	login = Login()
	login.loginGUI()
	# login.registerGUI()