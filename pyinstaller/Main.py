# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *
from tkinter import scrolledtext
import sys
import json
import io
import random
from Practice import Practice
from Calculation import Calculation
from File import File

def radCall():
	pass

class Main(object):
	"""docstring for Main"""
	def __init__(self, phone = None):
		super(Main, self).__init__()
		self.producer = Practice()  # 生成题目
		self.cal = Calculation()    # 计算结果
		self.school = {"小学":"primary","初中":"middle","高中":"high"}
		self.score = 0      # 记录分数
		self.answer = None  # 记录答案
		self.index = 0      # 第几题
		self.practices = None  # 生成的题目
		self.phone = phone
		self.file = File()     # 保存试卷


	# 题目展示
	def display(self):
		self.window = tk.Tk()
		self.window.title("题目展示")

		# 生成题目模块
		self.head = Frame(self.window)
		self.head.pack()

		ttk.Label(self.head, text='Enter a Count:').grid(column=0, row=0)
		# Adding a Textbox Entry widget
		self.count = tk.StringVar()
		count_entered = ttk.Entry(self.head, width=12, textvariable=self.count)
		count_entered.grid(column=0, row=1) # column 0
		# Adding a Button
		self.action = ttk.Button(self.head, text="生成试卷", command=self.creatPractices)   
		self.action.grid(column=2, row=1) # change column to 2
		
		ttk.Label(self.head, text='Choose a Mold:').grid(column=1, row=0)
		
		# 模式选择
		self.mold = tk.StringVar()
		mold_chosen = ttk.Combobox(self.head, width=12, textvariable=self.mold)
		mold_chosen['values'] = ("小学","初中","高中")
		mold_chosen.grid(column=1, row=1) # Combobox in column 1
		mold_chosen.current(0)

		# 题目展示模块
		self.middle = Frame(self.window,width=200)
		# self.middle.pack_propagate(0)
		self.middle.pack()

		# self.practice = StringVar()
		
		
		# 显示题目
		self.show_label = Label(self.middle,text="这里是题目....",font=("Arial", 15),height = 3)
		self.show_label.pack()		

		# 显示答案
		self.radio = Frame(self.middle)
		self.radio.pack()

		self.input_answer = tk.StringVar()

		self.rad_A = tk.Radiobutton(self.radio, text="A", variable=self.input_answer, value="A", command=radCall)
		self.rad_A.grid(column=0, row=0)

		self.rad_B = tk.Radiobutton(self.radio, text="B", variable=self.input_answer, value="B", command=radCall)
		self.rad_B.grid(column=1, row=0)

		self.rad_C = tk.Radiobutton(self.radio, text="C", variable=self.input_answer, value="C", command=radCall)
		self.rad_C.grid(column=2, row=0)

		self.rad_D = tk.Radiobutton(self.radio, text="D", variable=self.input_answer, value="D", command=radCall)
		self.rad_D.grid(column=3, row=0)

		self.submit = Button(self.window, text="提交", width = 40,command=self.submitCommand,state=DISABLED)
		self.submit.pack()
		# Start GUI
		self.window.mainloop()

	# 生成试卷按钮的处理函数
	def creatPractices(self):
		count = self.count.get()
		mold = self.mold.get()
		if count == "" or int(count) < 0 :
			self.showinfo("生成题目","请输入正确的题目数量")
			return
		self.practices = self.producer.produce(mold=self.school[mold],count = int(count))
		self.showinfo("生成题目","生成题目成功")
		self.action.configure(state=DISABLED)   # 设置生成试卷按钮不可点
		self.submit.configure(state=NORMAL)   # 设置生成提交按钮可点
		# 重新设置
		self.index = 0
		self.score = 0
		# 处理题目显示
		practice = self.practices[0]
		answer = self.cal.expression_to_value(string = self.practices[0])
		self.practices[0] = "1:"+self.practices[0] + " = " + str(answer) 
		self.setChoice(practice = practice,answer = answer)
		
		
	def submitCommand(self):
		input_answer = self.input_answer.get()
		if input_answer == self.answer:
			self.score = self.score + 1
		if self.index == int(self.count.get()):  # 答题结束，显示分数
			self.show_label.configure(text = "score:"+str(self.score)+"/"+self.count.get(),font=("Arial", 18),fg = 'red')
			self.action.configure(state=NORMAL)     # 设置生成试卷按钮可点
			self.submit.configure(state=DISABLED)   # 设置生成提交按钮不可点
			self.file.write(self.phone,self.practices)         # 保存题目
			return
		practice = self.practices[self.index]
		answer = self.cal.expression_to_value(string = self.practices[self.index])
		self.practices[self.index] = str(self.index+1) + ":" + self.practices[self.index] + " = " + str(answer)  # 添加答案
		self.setChoice(practice = practice,answer = answer)

	# 设置选项和题目
	def setChoice(self,practice,answer):
		practice = str(self.index+1) + ": " + practice + "="
		self.index = self.index+1   # index+1
		self.show_label.configure(text = practice,fg = 'black')
		num = random.randint(0,3)
		ans = ['A','B','C','D']
		self.answer = ans[num]   # 设置答案
		answers = [answer*-1,answer+1,answer-1]  # 其他的三个答案
		j = 0
		l = [self.rad_A,self.rad_B,self.rad_C,self.rad_D]
		for i in range(0,4):
			if i == num:
				l[i].configure(text = answer,font=("Arial", 12))
				continue
			l[i].configure(text = answers[j],font=("Arial", 12))
			j = j+1

	# 提示框
	def showinfo(self,title="", message=""):
		showinfo(title,message)


if __name__ == '__main__':
	pass
	# main = Main()
	# main.display()