# -*- coding:utf-8 -*-
import sys
import json
import io
import random

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

	def pratice_primary(self,count,type="primary"):
		op_list = self.operation[type]
		length = len(op_list)
		for i in range(0,count):
			operand = random.randint(1,5) # 操作数
			item = ""                     # 题目
			for j in range(0,operand):
				num = random.randint(1,100)
				op = random.randint(0,length-1)
				string = str(num) +' ' + op_list[op] + ' '
				item = item + string

			num = random.randint(1,100)		
			item = item + str(num) + ' ='
			print(item)

	def practice_high(self,count,type="high"):
		op_list = self.operation["primary"]
		ext_list = self.operation["high"]
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
			item = item + str(num) + ' ='
			print(item)

	def practice_middle(self,count,type="middle"):
		op_list = self.operation["primary"]
		ext_list = self.operation["middle"]
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
			item = item + str(num) + ' ='
			print(item)

	def produce(self,mold,count):
		if mold == "primary" :
			self.pratice_primary(count)
		elif mold == "middle":
			self.practice_middle(count)
		else:
			self.practice_high(count)




if __name__ == '__main__':
	p = Practice()
	# p.pratice_primary(count=5,type="primary")
	# p.practice_middle(count=5)
	p.practice_high(count=5)