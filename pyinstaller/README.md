# 结对编程

## 环境说明

* python 3.6+
* Window
* 项目中文编码为 utf-8，即使用终端运行时，需要设置终端的编码为utf-8,不然会乱码

## 运行

* 在`Login.py` 目录下执行 `python Login.py`即可,这个需要配python3.6的环境
* 可以之间运行 Login.exe  文件，不过可能会被安全管家之类的安全软件识别为病毒，需要信任或关闭安全软件



## 文件说明

* Login.py      登录、注册的窗体及逻辑
* Main.py       做题窗体
* Practice.py   负责随机生成题目
* Calculation.py  中缀表达式变后缀表达式，然后计算答案
* User.py       负责身份验证
* user.json     已经注册的用户
* File.py       文件读写，及用户的存储、读取
* Message.py    负责短信的发送，即验证码的发送


## 参考资料

[中缀表达式变后缀表达式、后缀表达式（逆波兰）求值](https://www.bbsmax.com/A/QV5ZeyqVJy/)