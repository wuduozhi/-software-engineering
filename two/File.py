# -*- coding:utf-8 -*-
import sys
import json
import io
import random
import os
import time

class File:

	def creatDir(self,name):
		file_dir = os.getcwd()
		name_dir = name
		file_abs = file_abs = os.path.join(file_dir, name_dir)
		if os.path.exists(file_abs) == False:
			os.mkdir(file_abs)

		return file_abs
	
	#写入试卷
	def write(self,name,practices = []):
		file_dir = self.creatDir(name)
		file_name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())+'.txt'			
		file_abs =  os.path.join(file_dir,file_name)
		with open(file_abs,mode="w+",encoding='utf-8') as f:
			for practice in practices:
				f.writelines(practice+"\n")

	# json 文件读出
	@staticmethod
	def read_json(file_abs):
		with open(file_abs,'r') as load_f:
			data = json.load(load_f)

		return data

	# json 文件写入
	@staticmethod
	def write_json(file_abs,data):
		with open(file_abs,'w+') as dump_f:
			json.dump(data,dump_f)


