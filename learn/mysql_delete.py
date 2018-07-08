# -*- coding:UTF-8 -*-

import MySQLdb

db = MySQLdb.connect('localhost','root','666666','jiang',charset='utf8')

cursor = db.cursor()

sql_old = "SELECT * FROM department"

try:
    cursor.execute(sql_old)
    result_old = cursor.fetchall()
    for index in range(len(result_old)):
        print "====第 %d 条数据===" % index
        for item in result_old[index]:
            print "old:",item
except:
    print "old查询失败"

sql_delete = "DELETE FROM department WHERE did = 1"

try:
    cursor.execute(sql_delete)
    result_delete = cursor.rowcount
    db.commit()
    print "操作影响的行数: %d 行" % result_delete
except:
    print "user删除失败"

sql_new = "SELECT * FROM department"

try:
    cursor.execute(sql_new)
    result_new = cursor.fetchall()
    for index in range(len(result_new)):
        print "====第 %d 条数据====" % index
        for item in result_new[index]:
            print "new:",item
except:
    print "new查询失败"

cursor.close()

db.close()