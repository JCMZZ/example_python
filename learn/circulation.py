scripts = ['Python','JAVA','SQL']
for name in scripts:
  print('%s语言' % name)
rangeN = list(range(101))
print(rangeN)
sum = 0
for item in rangeN:
  sum += item
print(sum)
whileSum = 0
rangeNW = 100
while rangeNW >= 0:
  whileSum += rangeNW
  rangeNW -= 1
print(whileSum)
for item in (1,2,3,4,5):
  if item % 2 == 0:
    print(item)
  if item == 2:
    break
print('END')
for item in (0,1,2,3,4):
  if item % 2 == 0:
    print('跳过')
    continue
  else:
    print(item)