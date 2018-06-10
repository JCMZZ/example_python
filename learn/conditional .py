age = int(input('请输入年龄！！！'))
if age >= 18:
  print('年龄%d,已成年' % age)
else:
  print('年龄%d,未成年' % age)
weight = float(input('请输入重量！！！'))
if weight < 25:
  print('重%.3f,营养不良' % weight)
elif weight >= 25 and weight < 35:
  print('重%.3f,健康' % weight)
elif weight >= 35:
  print('重%.3f,肥胖' % weight)