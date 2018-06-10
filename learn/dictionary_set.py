print('==========dictionary==========')
dictClass = {
  'name':'Jack',
  'age':22
}
print(dictClass)
print(dictClass['name'])
print('name' in dictClass)
for item in ['name','age','gender']:
  item in dictClass and print(dictClass[item])
  print(dictClass.get(item))
dictTuple = {
  (1,):'元组',
  (1,0):'两个元素',
  (1,(1,)):'含有二维tuple'
}
print(dictTuple)
for item in dictTuple:
  print(dictTuple.get(item))
print('==========set==========')
setDict = set(list(range(10)))
print(setDict)
setDict.add(11)
print('添加一个元素',setDict)
setDict.remove(0)
print('删除一个元素',setDict)
setDict1 = set(list(range(3,7)))
print('并集',setDict | setDict1)
print('交集',setDict & setDict1)
setTuple = set([(1,),(0,(1,)),(3,2)])
print(setTuple)