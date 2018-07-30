# _*_ coding:UTF-8_*_

# 位置参数
def name(name):
    print "平台开发部: %s" % name

name('JCM')

# 默认参数 默认参数必须指向不变对象
def custom(name, department):
    print "%s: %s" % (department, name)

custom('JCM', '平台开发部')

def customDefault(name, department='平台开发部'):
    print "%s: %s" % (department, name)

customDefault('JCM')
customDefault('WJX', '人事部')

# 可变参数
def output(*name):
    for item in name:
        print "姓名: %s" % item

output('WJX', 'LWD')
l = ['JCM', 'CFF']
output(*l)

# 关键字参数
def person(name, **kw):
    print '姓名: %s' % name
    for item in kw:
        print '%s: %s' % (item, kw[item])

person('JCM', age=12, gender='男')
extra = {
    '1':{
        'name':'JCM',
        'age':22
    },
    '2':{
        'name':'WJX',
        'age':30
    }
}
def persons(**kw):
    for item in kw:
        print 'name: %s' % kw[item]['name']
        print 'age: %d' % kw[item]['age']
persons(**extra)

# 命名关键字参数
def description(name, *, feel):
    print('%s 感到 %s' % (name,feel))
description('JCM', feel='高兴')