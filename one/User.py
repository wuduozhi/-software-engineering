# -*- coding:utf-8 -*-
import sys
import json
import io
import random


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


class User:
	def __init__(slef):
		slef.users = {}
		slef.users['primary'] = [
			['张三1','123'],
			['张三2','123'],
			['张三3','123'],
		]
		slef.users['middle'] = [
			['李四1','123'],
			['李四2','123'],
			['李四3','123'],
		]
		slef.users['high'] = [
			['王五1','123'],
			['王五2','123'],
			['王五3','123'],
		]

	def validate(slef,name,passwd):   # 验证用户,成功返回用户类型
		# val_list = slef.users[mold]
		for mold in slef.users:
			val_list = slef.users[mold]
			for user in val_list:
				if name == user[0] and passwd == user[1] :
					return mold

		return False



if __name__ == '__main__':
	try:
		# mold = sys.argv[1]
		name = sys.argv[1]
		passwd = sys.argv[2]
	except Exception as e:
		print(e)
		print("Usage:python User.py name passwd")
		exit()

	user = User()
	# val = user.validate("primary","张三3s","123")
	val = user.validate(name,passwd)
	print(val)