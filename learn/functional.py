# _*_ conding:UTF-8_*_
from functools import partial,reduce

# map
def ride(x):
    return x ** 2
r = map(ride,list(range(1,10)))
listr = list(r)
print(listr)
print(list(map(str,listr)))

# reduce
def add(x,y):
    return x+y
a = reduce(add, list(range(0,4)))
print(a)

def num(x,y):
    return x*10 + y
num = reduce(num, list(range(0,10)))
print(num)

def strint(string):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def numl(x):
        return DIGITS[x]
    def num(x, y):
        return x*10 + y
    return reduce(num,map(numl,string))
numberStr = '123'
numberInt = strint(numberStr)
print("字符串类型: %s ;数字类型: %d" % (numberStr, numberInt))

# lambda简化
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def strintsimplify(string):
    return reduce(lambda x,y: x*10 + y,map(lambda x: DIGITS[x],string))
numberSimplifyStr = '0123'
numberSimplify = strintsimplify(numberSimplifyStr)
print("字符串类型: %s ;数字类型: %d" % (numberSimplifyStr, numberSimplify))

# filter
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x:x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始化序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 打印10以内的素数
for n in primes():
    if n < 10:
        print(n)
    else:
        break

# 偏函数
max2 = partial(max,10)
print(max2(11,2,3))
int2 = partial(int,base=16)
print('整数: %d' % int2('121'))
