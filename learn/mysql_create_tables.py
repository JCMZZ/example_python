# -*- coding:UTF-8 -*-

"""
 提示：
    在创建数据表时应先进行删操作，
    在删除完后将相应的删除代码注释掉，
    再进行数据表的添加操作
"""

import MySQLdb

db = MySQLdb.connect(host='localhost',user='root',passwd='666666',db='jiang',charset='utf8')

cursor = db.cursor()

# 创建前删除数据库 
"""
 提示：
    删除表时应注意，根据表关联进行，
    删除顺序的排列
"""
sql_delete = """DROP TABLE IF EXISTS department;
                DROP TABLE IF EXISTS user;"""

# try:
#     cursor.execute(sql_delete)
#     result_delete  = cursor.fetchone()
#     print "SQL_delete返回值：%s" % result_delete
# except:
#     print "删除完成"

# 创建数据表 user department
sql_user = """CREATE TABLE user(
             uid INT AUTO_INCREMENT PRIMARY KEY,
             name VARCHAR(32) NOT NULL,
             age INT NOT NULL DEFAULT 1,
             gender VARCHAR(8) NOT NULL DEFAULT '未知'
         );"""

try:
    cursor.execute(sql_user)
    result_user  = cursor.fetchone()
    print "SQL_user返回值：%s" % result_user
except:
    print "user创建失败"

sql_department = """CREATE TABLE department(
             did INT AUTO_INCREMENT PRIMARY KEY,
             dname VARCHAR(64) NOT NULL,
             serial_numbers INT NOT NULL,
             admin VARCHAR(32) NOT NULL,
             user_id INT NOT NULL,
             FOREIGN KEY(user_id) REFERENCES user(uid)
         );"""

try:
    cursor.execute(sql_department)
    result_department  = cursor.fetchone()
    print "SQL_department返回值：%s" % result_department
except:
    print "department创建失败"

cursor.close()

db.close()