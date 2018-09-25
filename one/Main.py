# -*- coding:utf-8 -*-
import sys
import json
import io
import random
from Practice import Practice
from User import User
from File import File
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


if __name__ == '__main__':
	user = User()
	practice = Practice()
	file = File()
	school = {"primary":"小学","middle":"初中","high":"高中"}
	while 1:
		string = input("name and passwd: ")
		arr = re.split(r" +",string)  # 根据空格截取name passwd
		name = arr[0]
		passwd = arr[1]
		# name = input("name and passwd: ")
		# passwd = input("passwd: ")
		mold = user.validate(name,passwd)
		if mold != False:
			print("当前选择为{mold}出题".format(mold=school[mold]))
			break
		else:
			print("请输入正确的用户名和密码")
			continue
	
	while 1:
		log = "准备生成{mold}数学题目,请输入生成题目数量:".format(mold=school[mold])
		count = input(log)
		if count == "quit":
			break

		if count == "切换为小学":
			mold = "primary"
			continue
		elif count == "切换为初中":
			mold = "middle"
			continue
		elif count == "切换为高中":
			mold = "high"
			continue

		if "切换" in count:
			print("请输入小学、初中和高中三个选项中的一个")
			continue

		if int(count)<10 or int(count)>30:
			print("Count must be 10-30")
			continue
		
		practices = practice.produce(mold,int(count))
		file.write(name,practices)
