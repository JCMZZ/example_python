# -*- coding:UTF-8 -*-

import MySQLdb

db = MySQLdb.connect('localhost','root','666666','jiang',charset='utf8')

cursor = db.cursor()

sql_old = "SELECT * FROM user WHERE uid =14;"

try:
    cursor.execute(sql_old)
    result_old = cursor.fetchone()
    print "user-name-old：",result_old[1]
except:
    print "old查询失败"

sql_user = "UPDATE user SET name = 'JCM' WHERE uid = 14;"

try:
    cursor.execute(sql_user)
    result_update = cursor.fetchone()
    db.commit()
    print "user更新：",result_update
except:
    print "更新失败"

sql_new = "SELECT * FROM user WHERE uid =14;"

try:
    cursor.execute(sql_new)
    result_new = cursor.fetchone()
    print "user-name-new：",result_new[1]
except:
    print "new查询失败"