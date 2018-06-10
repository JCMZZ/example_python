print('==========调用函数==========')
# 绝对值函数abs
floatN = abs(12.111)
absN = abs(-12.111)
intN = abs(12)
print('%.3f'% floatN,'\n%.3f' % absN,'\n%d' % intN)
absNew = abs
absNewN = absNew(-12)
print('重定向函数abs',absNewN)
print('******类型转换******')
print('整数转换',int('123'))
print('整数转换',int(124.56))
print('浮点数转换',float('123'))
print('浮点数转换',float('123.45'))
print('字符串转换',str(123))
print('字符串转换',str(123.45))
print('布尔转换',bool(123))
print('布尔转换',bool(''))
print('==========定义函数==========')
# 定义一个什么都不做的函数
def noDoNothing():
  pass
def custom_abs(x):
  if not isinstance(x, (int,float)):
    raise TypeError('bad operand type')
  if x >= 0:
    return x
  else:
    return -x
print('自定义函数取绝对值',custom_abs(-12))
# print('不合法参数取绝对值抛错',custom_abs('-12'))
# print('不合法参数取绝对值抛错',custom_abs(-12,1))
def moreReturn():
  return 'oneString','twoString'
returnTuple = moreReturn()
print(returnTuple)  
one, two = moreReturn()
print(one, two)
print('string:'+ one + two)
one += str(1)
print(one)