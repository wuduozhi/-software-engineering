# 逸派后端

## 基本项

a. [github](https://github.com/wuduozhi) https://github.com/wuduozhi

自己在github上放了一些小项目，有帮一个咖啡厅弄的出纳系统[coffee.wduozhi.xyz/frontend/index.html]、有学Java是弄的五子棋小游戏，还有软件工程这门课上弄的项目。

b. 自己有用Python来爬虫，主要用的是request这么模块。最近有帮工作室爬教务系统的成绩、课表等数据。

c. 自己有在学校工作室参与项目的经历，就是去教务系统爬虫，然后用户绑定（即提供学号、密码），我们将用户的成绩、考试安排、课表结果展示给用户。工作室主要用PHP，都是采用前后端分离的架构，使用Ajax交互。

d. 有了解过Flask,也用过于Flask类似的Sanic，用这个来开个小型Web服务，对外提供爬虫的数据，也就是上面 [b] 说到的爬虫。

e.

f. 有自己的云服务器，Linux+Nginx+PHP+Mysql环境，也搭过Java的服务器环境。Nginx+Uwsgi这个的话，看来一些资料，跟 Nginx+php-fpm的模式类似，都是通过nginx代理，然后转发到cgi处理，然后cgi返回给nginx，nginx在返回。

g. 当使用的协议，如从http转到https,端口、域名三个中的任意一个不同时就产生了跨域，浏览器为了保证安全，有同源策略，会限制从一个源加载的文档或脚本与来自另一个源的资源进行交互，主要是限制使用XMLHttpRequest请求。

可通过CORS的方式实现跨域请求，即在服务器端增加一些http头来避开浏览器的同源策略。一般需要增加的响应头有：

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST, GET, OPTIONS
Access-Control-Allow-Headers: X-PINGOTHER, Content-Type
Access-Control-Max-Age: 86400
```


h. 基本的服务器环境、文件操作等，都能搞定

## 加分项

* 自己在学校的工作室是负责微信公众号的开发，即我们的产品入口都是放在微信公众号的，可以说，微信的那一套规则自己还是熟悉的。

* 自己弄过手机验证码，是用的第三方付费平台的接口，邮件类似。

## 其他

每天保证两到三个小时，时间段可能大部分在晚上



