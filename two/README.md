# 结对编程

## 环境说明

* python 3.6+
* Window
* 项目中文编码为 utf-8，即使用终端运行时，需要设置终端的编码为utf-8,不然会乱码

## 运行

* 在`Login.py` 目录下执行 `python Login.py`即可
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


## pyinstaller 打包文件

Python虽好，但是平时我们写的代码都是.py脚本文件，必须要在Python环境下 才可以运行。如果一台电脑没有安装Python是无法运行我们的程序的。当然你也可以选择随身携带安装包。 不过终究是有些麻烦。那么有没有什么办法，能把我们编写的Python代码转换成exe文件呢？这样不管到哪， 只要能打开exe就可以运行我们的程序。当然，办法是有的。网上一搜就有py2exe、pyinstaller等包可以实现 我们想要的这个功能。这里我们选择pyinstaller。

安装PyInstaller
### Installation

The easies way to install PyInstaller is using pip:

`pip install pyinstaller`

or upgrade to a newer version:

`pip install --upgrade pyinstaller`

For other installation options please refer to the manual and the pip user guide.

To install the current development version use:

`pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz`


[安装参考](https://blog.csdn.net/woshisangsang/article/details/73230433)

### 常用参数介绍 

* –icon=图标路径
* -F 打包成一个exe文件
* -w 使用窗口，无控制台
* -c 使用控制台，无窗口
* -D 创建一个目录，里面包含exe以及其他一些依赖性文件
* pyinstaller -h 来查看参数

## 参考资料

[中缀表达式变后缀表达式、后缀表达式（逆波兰）求值](https://www.bbsmax.com/A/QV5ZeyqVJy/)