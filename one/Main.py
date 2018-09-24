# -*- coding:utf-8 -*-
import sys
import json
import io
import random
from Practice import Practice
from User import User

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


if __name__ == '__main__':
	user = User()
	practice = Practice()
	school = {"primary":"小学","middle":"初中","high":"高中"}
	while 1:
		name = input("name: ")
		passwd = input("passwd: ")
		mold = user.validate(name,passwd)
		if mold != False:
			print("当前选择为{mold}出题".format(mold=school[mold]))
		else:
			print("请输入正确的用户名和密码")
			continue
		log = "准备生成{mold}数学题目,请输入生成题目数量:".format(mold=school[mold])
		count = input(log)
		practice.produce(mold,int(count))
