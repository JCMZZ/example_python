# -*- coding:UTF-8 -*-

import redis

import threading

r = redis.Redis('localhost', 6379, db=0)

# 获取redis中的所有键 keys *

print 'redis中的所有key: %s' % r.keys('*')

# 删除redis中指定的键 delete

r.delete('desks')

print 'redis中的所有key DELETE: %s' % r.keys('*')

# 检查redis中是否存在指定键 exists

print 'redis中是否存有键desks %s' % r.exists('desks')

print 'redis中是否存有键number1 %s' % r.exists('number1') 

# 未指定键设置超时时间 expire

r.expire('number8', 5)

print 'redis中是否存有键number8 %s' % r.exists('number8') 

def number_timer():
    print 'redis中是否存有键number8 %s' % r.exists('number8') 

timer = threading.Timer(5, number_timer)

timer.start()

# 指定键进行重命名 rename

# r.rename('numberinter', 'number1')

# print 'redis中所有的key: %s' % r.keys('*')

# 将redis中指定的键，移动到指定的库下 move

# r.move('number1', 1)

# print 'redis中所有的key: %s' % r.keys('*')

# r = redis.Redis('localhost', 6379, db=1)

# print 'redis中所有的key: %s' % r.keys('*')

# 随机获取一个redis的键 randomkey

print '随机获取的键: %s' % r.randomkey()

# 获取指定键的类型 type

print 'number9的类型: %s' % r.type('number9')