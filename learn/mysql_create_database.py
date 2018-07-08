# -*- coding:UTF-8 -*-

# 引入MySQLdb模块
import MySQLdb

# 连接数据库
db = MySQLdb.connect(host='localhost',user='root',passwd='666666',charset='utf8')

# 创建游标
cursor = db.cursor()

# SQL语句
sql = """DROP DATABASE IF EXISTS jiang;
         CREATE DATABASE jiang CHARACTER SET utf8"""

# 执行SQL语句
cursor.execute(sql)

# 获取一条数据
result = cursor.fetchone()

# 打印返回值
print "SQL返回值：%s" % result

# 关闭游标
cursor.close()

# 数据库断开连接
db.close()