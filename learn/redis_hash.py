# -*- coding:UTF-8 -*-

import redis

r = redis.Redis('localhost', 6379)

# 向对应的 Hash 中设置一个键值对(不存在则创建，否则，则修改) hset

r.hset('pepole', 'ear', 'two')

# 在对应的Hash中根据key获取value  hget

print 'pepole中ear的值: %s' % r.hget('pepole', 'ear')

# 向Hash中批量的设置键值对 hmset

foods = {'fruits': 'banana', 'vegetables': 'eggplant', 'cereals': 'wheat'}

r.hmset('foods', foods)

# 获取Hash的所有键值 hgetall

print 'foods的所有键值: %s' % r.hgetall('foods')

# 在对应Hash中获取多个key的值 hmget

keys = ['fruits', 'vegetables', 'cereals']

print '获取foods的多个key值: %s' % r.hmget('foods', keys)

print '获取foods的多个key值: %s' % r.hmget('foods','fruits', 'vegetables', 'cereals')

# 获取Hash中键值对的个数 hlen

print 'foods中键值对的个数: %s' % r.hlen('foods')

# 获取Hash中所有key的值 hkeys

print 'foods中所有key的值: %s' % r.hkeys('foods')

# 获取Hash中所有value的值 hvals

print 'foods中所有value的值: %s' % r.hvals('foods')

# 检查当前Hash中是否存在传入的key hexists

print 'foods中是否存在key fruits: %s' % r.hexists('foods', 'fruits')

print 'foods中是否存在key JCM: %s' % r.hexists('foods', 'JCM')

# 删除指定Hash对应的key所在的键值对

print 'del_before foods中所有的键值对: %s' % r.hgetall('foods')

r.hdel('foods', 'fruits')

print 'del_after foods中所有的键值对: %s' % r.hgetall('foods')

# 自增Hash中对应键的值 不存在则创建 hincrby(整数)

r.hmset('boy', {'height': 175, 'weight': 72})

print 'boy中所有的键值对: %s' % r.hgetall('boy')

r.hincrby('boy', 'height')

print 'boy中所有的键值对: %s' % r.hgetall('boy')

# 自增 hincrbyfloat(浮点数)

r.hincrbyfloat('boy', 'weight', 0.5)

print 'boy中所有的键值对: %s' % r.hgetall('boy')

