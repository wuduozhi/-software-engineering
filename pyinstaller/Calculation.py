# -*- coding: UTF-8 -*-
import math
import re

# 中缀表达式变后缀表达式、后缀表达式（逆波兰）求值

class Calculation:
	def __init__(self,string = None):
		self.string = string
		self.expression = []
		self.ops_rule = {'+': 1,'-': 1,'*': 2,'/': 2}

	# 将中缀表达式转换为后缀表达式
	def middle_to_after(self,string=None):
		exp = []
		ops = []
		if string == None:
			string = self.string

		middle = string.split(" ")
		for item in middle:
			if item in ['+', '-', '*', '/']:
				while len(ops) >= 0:
					if len(ops) == 0:
						ops.append(item)
						break
					op = ops.pop()
					if op == '(' or self.ops_rule[item] > self.ops_rule[op]:
						ops.append(op)
						ops.append(item)
						break
					else:
						exp.append(op)
			elif item == "(":
				ops.append(item)
			elif item == ")":
				while len(ops) >= 0:
					op = ops.pop()
					if op == '(':
						break
					exp.append(op)
			else:
				exp.append(item)

		while len(ops) > 0:
			exp.append(ops.pop())

		self.expression = exp

	# 后缀表达式求和
	def expression_to_value(self,exp=None,string=None):
		self.middle_to_after(string)
		stack = []
		for item in self.expression:
			if item in ['+', '-', '*', '/']:
				n2 = stack.pop()
				n1 = stack.pop()
				tmp = self.cal(n1,n2,item)
				stack.append(tmp)
			else:
				num = self.special(item)  # 特殊处理根号  三角函数值
				stack.append(num)

		return stack[0]


	def cal(self,n1, n2, op):
	    if op == '+':
	        return n1 + n2
	    if op == '-':
	        return n1 - n2
	    if op == '*':
	        return n1 * n2
	    if op == '/':
	        return n1 / n2

	# 处理根号  sin特殊指
	def special(self,n):
		if n.find("^") != -1:
			strs = n.split("^")
			if strs[1] == "0.5":
				return pow(int(strs[0]),1/2)
			return pow(int(strs[0]),int(strs[1]))

		if n.find("sin") != -1:
			num = re.sub("\D", "", n)
			return math.sin(int(num))

		if n.find("cos") != -1:
			num = re.sub("\D", "", n)
			return math.cos(int(num))

		if n.find("tan") != -1:
			num = re.sub("\D", "", n)
			return math.tan(int(num))


		return int(n)



if __name__ == '__main__':
	cal = Calculation('9 + ( 3 * ( 4 + 2 * 8 ) ) * 3 + 10 / 2')
	# cal.middle_to_after()
	print(cal.expression_to_value())
	print(pow(63,1/2))