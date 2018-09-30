# -*- coding: UTF-8 -*-
import sys
import json
import io
import os
import random
from File import File


class User(object):
	file_abs = file_abs = os.path.join(os.getcwd(),"user.json")
		

	# 用户检测
	@staticmethod
	def validate(phone,passwd):
		users = File.read_json(User.file_abs)
		for user in users:
			if user['phone'] == phone and user['passwd'] == passwd:
				return True
		
		return False

	# 增加用户
	@staticmethod
	def add(phone,passwd):
		user = {
			'phone':phone,
			'passwd':passwd
		}
		users = File.read_json(User.file_abs)
		users.append(user)
		File.write_json(User.file_abs,users)

if __name__ == '__main__':
	print(User.validate("13098921645","wdz123"))
	User.add('123','345')