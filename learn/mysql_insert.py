# -*- coding:UTF-8 -*-

import MySQLdb

db = MySQLdb.connect('localhost','root','666666','jiang',charset='utf8')

cursor = db.cursor()

sql_user = """INSERT INTO user VALUE(
            null,'蒋春明',1,'男'
        );"""

try:
    cursor.execute(sql_user)
    result_user = cursor.fetchone()
    db.commit()
    print "SQL_user返回值：%s" % result_user
except:
    print "user添加失败"

sql_department = """INSERT INTO department VALUE(
            null,'平台开发部',01112,'admin',14
        );"""

try:
    cursor.execute(sql_department)
    result_department = cursor.fetchone()
    db.commit()
    print "SQL_department返回值：%s" % result_department
except:
    print "department添加失败"

cursor.close()

db.close()