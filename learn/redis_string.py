# -*- coding:UTF-8 -*-

# 引入redis模块

import redis

# 引入定时器

import threading

# 连接redis数据库

r = redis.Redis('localhost', 6379)

# 存入一个名称为 name 的普通键 set值为 jiang

r.set('name', 'jiang')

print 'name: %s' % r.get('name')

# 存入一个定时键(seconds) user setex 值为 JCM

r.set('user', 'JCM', ex=5)

print 'inside_user: %s' % r.get('user')

def seconds():
    print 'outsid_user: %s' % r.get('user')

seconds_timer = threading.Timer(5, seconds)

seconds_timer.start()

# 存入一个定时键(milliseconds) passwd setpx 值为 ’123456‘

r.set('passwd', '123456', px=5000)

print 'inside_passwd: %s' % r.get('passwd')

def milliseconds():
    print 'outside_passwd: %s' % r.get('passwd')

milliseconds_timer = threading.Timer(5, milliseconds)

milliseconds_timer.start()

# 存入一个唯一键(only) weight nx=True 值为 ’72kg‘

r.delete('weight')

r.set('weight', '72kg', nx=True)

print 'first_weight: %s' % r.get('weight')

r.set('weight', '74kg', nx=True)

print 'second_weight: %s' % r.get('weight')

print 'weight是否为唯一键:', r.get('weight') == '72kg'

# 存入一个预存键(exists) age xx=True 值为 23

r.set('age', 23, xx=True)

print 'before_age: %s' % r.get('age')

r.set('age', 23)

print 'exists_age: %s' % r.get('age')

r.set('age', 22, xx=True)

print 'after_age: %s' % r.get('age')

# 批量存储 mset

r.mset(name1 = 'jiang', name2 = 'chun', name3 = 'ming')

r.mset({'weight1': '71kg', 'weight2': '72kg', 'weight3': '73kg'})

# 批量获取 mget

print '批量获取 name:', r.mget('name1', 'name2', 'name3')

print '批量获取 weight:', r.mget(['weight1', 'weight2', 'weight3'])

# 设置新值打印原值

r.set('gender', 1)

print '打印原值: %s' % r.getset('gender', 0)

print '打印新值: %s' % r.get('gender')

# 根据字节获取子序列(子串)

r.set('message', 'Hello World !')

print '打印子序列: %s' % r.getrange('message', 6, 10)

# 修改字符串内容，从指定字符串索引开始向后替换，如果新值太长时，则向后添加

r.set('text', 'I see You')

print 'primary_text: %s' % r.get('text')

r.setrange('text', 1, '-')

print 'inside_replace_text: %s' % r.get('text')

r.setrange('text', r.strlen('text'), ' again')

print 'outside_replate_text: %s' % r.get('text')

# 对二进制表示位进行操作

r.set('str', '345')

for item in r.get('str'):
    print '值: %s' % item
    print 'ASCII码中对应的值: %s' % ord(item)
    print '对应值转换的二进制: %s' % bin(ord(item))

r.setbit('str', 6, 0) 

print 'str: %s' % r.get('str')

# 获取对应值的二进制中某位置的值(0或1)

r.set('head', 'one')

for item in r.get('head'):
    print '值: %s' % item
    print 'ASCII码中对应的值: %s' % ord(item)
    print '对应值转换的二进制: %s' % bin(ord(item))

print 'head 6 位置上的值: %s' % r.getbit('head', 6)

# 获取对应二进制中 1 的个数

r.set('ear', 'two')

for item in r.get('ear'):
    print '值: %s' % item
    print 'ASCII码中对应的值: %s' % ord(item)
    print '对应值转换的二进制: %s' % bin(ord(item))

print 'ear二进制 1 的个数: %d' % r.bitcount('ear', 0, 2)

# 返回对应值的字节长度(一个汉字3个字节)

r.set('bird', '小鸟')

print 'bird的字节长度: %d' % r.strlen('bird')

# 自增对应的值，当值不存在时，则创建，否则则自增 incr 自增整数

r.incr('kite')

print 'incr_first: %s' % r.get('kite')

r.incr('kite', 4)

print 'incr_second: %s' % r.get('kite')

# 自增 incrfloat 自增浮点数

r.incrbyfloat('caryon')

print 'incrbyfloat_first: %s' % r.get('caryon')

r.incrbyfloat('caryon', 0.4)

print 'incrbyfloat_second: %s' % r.get('caryon')

# 自减 decr 自减整数

r.decr('height')

print 'decr_first: %s' % r.get('height')

r.decr('height', 5)

print 'decr_second: %s' % r.get('height')

# 在对应的值后面追加内容 append

r.set('food', 'food')

print 'food的值: %s' % r.get('food')

r.append('food', 's')

print '向food值后追加’s‘: %s' % r.get('food')