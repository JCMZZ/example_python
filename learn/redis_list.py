# -*- coding:UTF-8 -*-

import redis

r = redis.Redis('localhost', 6379)

# 在对应的list中添加元素，每个元素都添加到列表的最左边 lpush

r.lpush('stationery', 'pencil', 'pencil cas', 'lead')

print 'stationery的所有元素: %s' % r.lrange('stationery', 0, -1)

# 通lpush，每个元素都添加到列表的最右边 rpush

r.rpush('person', 'head', 'body', 'foot')

print 'person的所有元素: %s' % r.lrange('person', 0, -1)

# 只有列表已经存在时，将元素添加到列表的最左边 lpushx

r.lpushx('stationery', 'pencils')

print 'stationery的所有元素L: %s' % r.lrange('stationery', 0, -1)

# 同lpushx，将元素添加到列表的最右边 rpushx

r.rpushx('person', 'ears')

print 'person的所有元素R: %s' % r.lrange('person', 0, -1)

# 获取列表元素的个数 llen

r.lpush('name', 'n', 'a', 'm', 'e')

print 'name的元素个数: %d' % r.llen('name') 

# 在对应的列表的某一个值前(before)或后(after),插入一个元素 linsert

r.rpush('numbers', '1', '2')

print 'numbers的所有元素: %s' % r.lrange('numbers', 0, -1)

r.linsert('numbers', 'BEFORE', '1', '0')

print 'numbers的所有元素BEFORE: %s' % r.lrange('numbers', 0, -1)

r.linsert('numbers', 'AFTER', '2', '3')

print 'numbers的所有元素AFTER: %s' % r.lrange('numbers', 0, -1)

# 对列表某个索引位置重新赋值 lset

r.rpush('fruits', 'banana', 'orange', 'apple')

print 'fruits的所有元素: %s' % r.lrange('fruits', 0, -1)

r.lset('fruits', 1, 'melon')

print 'fruits的所有元素: %s' % r.lrange('fruits', 0, -1)

# 删除对应列表中的指定值 lrem

r.rpush('number', 'one', 'two', 'two', 'two', 'three', 'four', 'five', 'five', 'five', 'six')

print 'number的所有元素: %s' % r.lrange('number', 0, -1)

r.lrem('number', 'five', 0)

print 'number的所有元素0: %s' % r.lrange('number', 0, -1)

r.lrem('number', 'six', -1)

print 'number的所有元素-1: %s' % r.lrange('number', 0, -1)

r.lrem('number', 'two', 2)

print 'number的所有元素2: %s' % r.lrange('number', 0, -1)

# 移除列表左侧的第一个元素返回值是移除的元素 lpop

r.lpush('desks', 'board', 'secretaire', 'end table')

print 'desks的所有元素: %s' % r.lrange('desks', 0, -1)

print '移除desks左侧的元素，返回值: %s' % r.lpop('desks')

print 'desks的所有元素: %s' % r.lrange('desks', 0, -1)

# 移除列表中没有在该索引之内的元素 ltrim

print 'numbers的所有元素: %s' % r.lrange('numbers', 0, -1)

r.ltrim('numbers', 0, 1)

print 'numbers的所有元素: %s' % r.lrange('numbers', 0, -1)

# 从一个列表的最右边移除一个元素，同时添加到另一个列表的最左边 rpoplpush

print 'numbers的所有元素: %s' % r.lrange('numbers', 0, -1)

print 'number的所有元素: %s' % r.lrange('number', 0, -1)

r.rpoplpush('numbers', 'number')

print 'numbers的所有元素: %s' % r.lrange('numbers', 0, -1)

print 'number的所有元素: %s' % r.lrange('number', 0, -1)

# 同rpoplpush，多了个timeout，取数据的列表没元素后的阻塞时间，0为一直阻塞

print 'numbers的所有元素: %s' % r.lrange('numbers', 0, -1)

print 'number的所有元素: %s' % r.lrange('number', 0, -1)

r.brpoplpush('numbers', 'number', timeout=0)

print 'numbers的所有元素: %s' % r.lrange('numbers', 0, -1)

print 'number的所有元素: %s' % r.lrange('number', 0, -1)

# 将多个列表排列，按照从左到右去移除各个列表的元素 blpop 同blpop，按照从右到左去移除各个列表的元素 brpop

# r.lpush('number1', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# print 'number1的所有元素: %s' % r.lrange('number1', 0, -1)

# r.lpush('number2', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# print 'number2的所有元素: %s' % r.lrange('number2', 0, -1)

# while True:
#     print '移除列表元素后的返回值L:', r.blpop(['number1', 'number2'], timeout=5)
#     print 'number1的所有元素: %s' % r.lrange('number1', 0, -1)
#     print 'number2的所有元素: %s' % r.lrange('number2', 0, -1)
