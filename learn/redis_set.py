# -*- coding:UTF-8 -*-

import redis

r = redis.Redis('localhost', 6379)

# SET 集合就是不允许重复的列表 set

# 给对应的集合添加元素 sadd 获取集合的所有值 smembers

r.sadd('desks', 'board')

print 'desks的所有元素: %s' % r.smembers('desks')

r.sadd('desks', 'board', 'end table', 'secretaire')

print 'desks的所有元素: %s' % r.smembers('desks')

# 获取对应集合的元素个数 scard

r.sadd('number', 1, 2, 3)

print 'number集合的所有元素: %s' % r.smembers('number')

print 'number集合的元素个数: %d' % r.scard('number')

# 获取第一个对应的集合中，且不在其他对应集合中的元素集合 sdiff

r.sadd('number1', 1, 2, 3)

print 'number1集合的所有元素: %s' % r.smembers('number1')

r.sadd('number2', 3, 4)

print 'number2集合的所有元素: %s' % r.smembers('number2')

r.sadd('number3', 5, 6, 7)

print 'number3集合的所有元素: %s' % r.smembers('number3')

print 'sdiff集合的所有元素: %s' % r.sdiff('number1', 'number2', 'number3')

# 将sdiff获取的集合指向到指定的集合中 sdiffstore

r.sdiffstore('numberdiff', 'number1', 'number2', 'number3')

print 'numberdiff集合的所有元素: %s' % r.smembers('numberdiff')

print 'number2集合的所有元素: %s' % r.smembers('number2')

r.sdiffstore('number2', 'number1', 'number2', 'number3')

print 'number2集合的所有元素: %s' % r.smembers('number2')

# 获取多个对应集合的并集 sinter (获取所有集合的并集元素集合)

r.sadd('number4', 0, 1, 2, 3)

r.sadd('number5', 3, 4, 5, 0)

r.sadd('number6', 0, 2, 3, 4)

print '获取多个集合的并集: %s' % r.sinter('number4', 'number5', 'number6')

# 将sinter获取到的集合指向指定集合 sinterstore

r.sinterstore('numbersinter', 'number4', 'number5', 'number6')

print 'numbersinter的所有元素: %s' % r.smembers('numbersinter')

# 检查集合中是否有传入的元素 sismember

r.sadd('person', 'foot', 'ears', 'head')

print 'person集合中是否有元素body: %s' % r.sismember('person', 'body')

print 'person集合中是否有元素ears: %s' % r.sismember('person', 'ears')

# 将某个元素从一个集合移动到另一个集合 smove

r.sadd('toys', 'bear', 'panda', 'brown bear', 'car')

print 'toys的所有元素: %s' % r.smembers('toys')

r.sadd('traffic', 'boat', 'plane', 'truck')

print 'traffic的所有元素: %s' % r.smembers('traffic')

r.smove('toys', 'traffic', 'car')

print 'toys的所有元素: %s' % r.smembers('toys')

print 'traffic的所有元素: %s' % r.smembers('traffic')

# 在指定集合右侧移除一个元素并返回 spop

r.sadd('weight', '71kg', '72kg', '73kg')

print 'weight的所有元素: %s' % r.smembers('weight')

r.spop('weight')

print 'weight的所有元素: %s' % r.smembers('weight')

# 从指定集合中随机获取n个元素 srandmember

r.sadd('height', 175, 180, 132, 165)

print 'height的所有元素: %s' % r.smembers('height')

print 'height中随机获取2个元素: %s' % r.srandmember('height', 2)

print 'height中随机获取2个元素: %s' % r.srandmember('height', 2)

# 删除对应集合中的某些元素 srem

print 'height的所有元素: %s' % r.smembers('height')

r.srem('height', 132, '132')

print 'height的所有元素: %s' % r.smembers('height')

# 获取多个集合的并集 sunion (获取所有集合的元素并去重)

print 'number1的所有元素: %s' % r.smembers('number1')

print 'number2的所有元素: %s' % r.smembers('number2')

print 'number3的所有元素: %s' % r.smembers('number3')

print '多个集合的并集: %s' % r.sunion('number1', 'number2', 'number3')

# 获取多个集合的并集，并指向一个集合 sunionstore 

print '多个集合的并集: %s' % r.sunion('numberset', 'number1', 'number2', 'number3')

print 'numberset的所有元素: %s' % r.smembers('numberset')
