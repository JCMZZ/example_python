# -*- coding:UTF-8 -*-

import redis

r = redis.Redis(host='localhost',port=6379)

r.set('JCM','jiang')

print r.get('JCM')