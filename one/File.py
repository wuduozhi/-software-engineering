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
	
	def write(self,name,practices = []):
		file_dir = self.creatDir(name)
		file_name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())+'.txt'			
		file_abs =  os.path.join(file_dir,file_name)
		with open(file_abs,mode="w+",encoding='utf-8') as f:
			for practice in practices:
				f.writelines(practice+"\n")



if __name__ == '__main__':
	file = File()
	file.creatDir("吴多智")
