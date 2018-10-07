# -*- coding: UTF-8 -*-
import requests
import urllib.parse
import json


# 单例模式   发送短信
# 20167   wdz123456

class Message(object):
	instance = None
	url = "http://api.tms.im/sendsms"
	templateId = '20167'
	passwd = 'wdz123456'

	

	@staticmethod
	def get_instance(): # 单例模式
		if Message.instance is None:
			Message.instance = object.__new__(Message)
		return Message.instance


	# 根据 code 验证码  phone 手机号码 发送验证短信
	def send_code(self,code,phone):
		body = '{"%'+'code%":"'+code+'"}'
		body = urllib.parse.quote(body)
		data = {
			"phone":phone,
			"pass":self.passwd,
			"templateId":self.templateId,
			"body":body
		}
		headers = {"Content-Type": "application/x-www-form-urlencoded"} 
		# print(json.dumps(data))
	
		respose = requests.post(self.url, data=data,headers=headers)
		string = respose.text
		l = string.rfind("}")
		string = string[:l+1]
		result = json.loads(string)
		return result
		# print(json.loads(string))



if __name__ == '__main__':
	# message = Message.get_instance().send_code(code="123456",phone="13098921645")
	print("Message")
