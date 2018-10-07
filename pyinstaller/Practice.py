# -*- coding:utf-8 -*-
import sys
import json
import io
import random
from Calculation import Calculation

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

class Practice:
	def __init__(self):
		# self.op_primary = ["+","-","*","/"]
		# self.op_middle = ["+","-","*","/","^0.5","^2"]
		# self.op_high = ["+","-","*","/","^0.5","^2","cos","sin","tan"]
		self.operation = {}
		self.operation['primary'] = ["+","-","*","/"]
		self.operation['middle'] = ["^0.5","","^2"]
		self.operation['high'] = ["cos","sin","tan"]
		# self.practices = []

	def pratice_primary(self,count,type="primary"):
		op_list = self.operation[type]
		length = len(op_list)
		practices = []
		for i in range(0,count):
			operand = random.randint(1,5) # 操作数
			# item = str(i) +": "                     # 题目
			item = ""
			for j in range(0,operand):
				num = random.randint(1,100)
				op = random.randint(0,length-1)
				string = str(num) +' ' + op_list[op] + ' '
				item = item + string

			num = random.randint(1,100)		
			# item = item + str(num) + ' ='
			item = item + str(num)
			item = self.addBrackets(item)
			practices.append(item)
			# print(item)
		return practices

	def practice_high(self,count,type="high"):
		op_list = self.operation["primary"]
		ext_list = self.operation["high"]
		practices = []
		length = len(op_list)
		for i in range(0,count):
			operand = random.randint(1,5) # 操作数
			item = ""                     # 题目
			have = 0                      # 是否已经用特殊符号
			for j in range(0,operand):
				flag = random.randint(0,6)   # 可以调节生成特殊符号的概率
				if flag < 3 :
					num = ext_list[flag] + str(random.randint(1,100)) 
					have = 1
				else:
					num = str(random.randint(1,100))

				if num == "tan90":   # tan90度的bug
					x = x-1
					continue
				op = random.randint(0,length-1)
				string = str(num) +' ' + op_list[op] + ' '
				item = item + string

			num = random.randint(1,100)		
			item = item + str(num)
			item = self.addBrackets(item)
			practices.append(item)
			# print(item)
		return practices

	def practice_middle(self,count,type="middle"):
		op_list = self.operation["primary"]
		ext_list = self.operation["middle"]
		practices = [] #保存结果
		length = len(op_list)
		for i in range(0,count):
			operand = random.randint(1,5) # 操作数
			item = ""                     # 题目
			have = 0                      # 是否已经用特殊符号
			for j in range(0,operand):
				flag = random.randint(0,6)   # 可以调节生成特殊符号的概率
				if flag < 3 :
					num = str(random.randint(1,100)) + ext_list[flag]
					have = 1
				else:
					num = str(random.randint(1,100))
				op = random.randint(0,length-1)
				string = str(num) +' ' + op_list[op] + ' '
				item = item + string

			num = random.randint(1,100)		
			# item = item + str(num) + ' ='
			item = item + str(num)
			item = self.addBrackets(item)
			practices.append(item)
			# print(item)
		return practices

	def produce(self,mold,count):
		if mold == "primary" :
			return self.pratice_primary(count)
		elif mold == "middle":
			return self.practice_middle(count)
		else:
			return self.practice_high(count)

	def addBrackets(self,item):   # 添加括号
		num = random.randint(0,2)
		string = item
		for x in range(0,num):
			length = len(string)
			for j in range(0,length):
				flag = random.randint(0,1)
				if flag==1 and string[j] in self.operation['primary']:
					# string = string[:j+1] + "(" + string[j+1:]
					for y in range (j+1,len(string)):   # 找到下一个基本运算符
						if string[y] in self.operation['primary']:
							break

					n = random.randint(y+1,len(string))
					for z in range(n,len(string)):
						if string[z] in self.operation['primary']:   # 一起加括号
							l = len(string)
							string = string[:j+1] + " (" + string[j+1:]
							z = len(string) - l + z   # 重新计算长度
							string = string[:z] + ") " + string[z:]
							break

					break

		return string




if __name__ == '__main__':
	p = Practice()
	cal = Calculation()
	items = p.practice_middle(count=5)
	# items = p.pratice_primary(count=5,type="primary")
	for item in items:
		# print(type(item))
		print(item + " = " + str(cal.expression_to_value(string=item)))
	# p.practice_middle(count=5)
	# p.practice_high(count=5)