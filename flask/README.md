# flask的简单应用
1、引入Flask类 from flask import Flask
2、创建Flask类的实例，Flask(__name__) __name__根据"应用使用"和“模块使用"而发生变化
3、使用route()装饰器来告诉Flask触发函数的URL
4、函数名称用来生成相关联的URL，函数最后返回需要的信息