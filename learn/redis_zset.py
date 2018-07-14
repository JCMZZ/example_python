# -*- coding:UTF-8 -*-

import redis

r = redis.Redis('localhost', 6379)

# 在对应的有序集合中添加元素 zadd

r.zadd('desks', 'secretaire', 2, 'desk', 1, 'end table', 3)

# 按照索引范围获取有序集合的元素 zrange

print '获取desks有序集合的所有元素: %s' % r.zrange('desks', 0, -1, True, True, int)

# 获取有序集合内元素的数量 zcard

print '获取desks有序集合的元素数量: %d' % r.zcard('desks')

# 获取有序集合中分数范围内的元素的个数 zcount

print '获取0-1分之间的有序集合的元素的个数: %d' % r.zcount('desks', 0, 2) 

# 自增有序集合内值对应的分数 zincrby

r.zincrby('desks', 'desk', 3)

print '获取desks有序集合的元素数量: %s' % r.zrange('desks', 0, -1, False, True, int)

# 同zrange，集合是从大到小排列的 zrevrange

print '获取desks有序集合的元素数量: %s' % r.zrevrange('desks', 0, -1, True, int)

# 获取元素在有序集合中的排行位置(从0开始)

print '获取desk元素在desks有序集合中的排行位置: %d' % r.zrank('desks', 'desk')

# 同zrank，从大到小 zrevrank

print '获取desk元素在desks有序集合中的排行位置: %d' % r.zrevrank('desks', 'desk')

# 获取有序集合中元素对应的分数 zscore

print '获取desk元素对应的分数: %d' % r.zscore('desks', 'desk')

# 删除集合中指定的元素 zrem

r.zrem('desks', 'end table')

print '获取desks有序集合中所有的元素: %s' % r.zrange('desks', 0, -1, True, False, int)

# 根据排行范围删除 zremrangebyrank

r.zadd('number1', 'item1', 0, 'item2', 2, 'item3', 4, 'item4', 1, 'item5', 3)

print 'number1有序集合的所有元素: %s' % r.zrange('number1', 0, -1, True, True, int)

r.zremrangebyrank('number1', 2, 3)

print 'number1有序集合的所有元素: %s' % r.zrange('number1', 0, -1, True, True, int)

# 根据分数范围删除 zremrangebyscore

r.zadd('number2', 'item1', 0, 'item2', 2, 'item3', 4, 'item4', 1, 'item5', 3)

print 'number2有序集合的所有元素: %s' % r.zrange('number2', 0, -1, True, True, int)

r.zremrangebyscore('number2', 0, 2)

print 'number2有序集合的所有元素: %s' % r.zrange('number2', 0, -1, True, True, int)

# 获取多个有序集合的交集并指向指定集合，如果遇到相同值，不同分数，按aggregate(SUM,MIN,MAX)操作 zinterstore (获取指定有序集合交集的元素放入指定的有序集合中)

r.zadd('number9', 'item0', 1, 'item2', 7, 'item3', 11)

print 'numbe9有序集合的所有元素: %s' % r.zrange('number9', 0, -1, True, True, int)

r.zadd('number8', 'item11', 12, 'item0', 3, 'item3', 15, 'item4', 22)

print 'numbe8有序集合的所有元素: %s' % r.zrange('number8', 0, -1, True, True, int)

r.zadd('number7', 'item9', 12, 'item0', 72, 'item3', 1, 'item49', 22)

print 'number7有序集合的所有元素: %s' % r.zrange('number7', 0, -1, True, True, int)

r.zinterstore('numberinter', ('number9', 'number8', 'number7'), 'MAX')

print 'numberinter有序集合的所有元素: %s' % r.zrange('numberinter', 0, -1, True, True, int)

# 获取多个有序集合的并集指向指定的有序集合中，其他同 zinterstore zunionstore (获取所有指定有序集合的元素并去重放入指定的有序集合中)

r.zunionstore('numberunion', ('number9', 'number8', 'number7'), 'MIN')

print 'numberunion有序集合的所有元素: %s' % r.zrange('numberunion', 0, -1, True, True, int)
