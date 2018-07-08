# -*- coding:UTF-8 -*-

import MySQLdb

db = MySQLdb.connect('localhost','root','666666','jiang',charset='utf8')

cursor = db.cursor()

sql_user = "SELECT * FROM user"

try:
    cursor.execute(sql_user)
    result_user = cursor.fetchone()
    for item in result_user:
        print "user:",item
except:
    print "user查询失败"

sql_department = "SELECT * FROM department"

try:
    cursor.execute(sql_department)
    result_department = cursor.fetchall()
    for items in result_department :
        for item in items:
            print "department:",item
except:
    print "department查询失败"

cursor.close()

db.close()

