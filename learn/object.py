# _*_ coding:UTF-8 _*_

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print('你好，我叫%s,我%d岁了！' % (self.name,self.age))

hanlei = Student('hanlei',12)
hanlei.say()

class Person(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name = name
    def say(self):
        print('%s %d 岁了！' % (self.__name,self.__age))

hanmei = Person('hanmei',22)
print('姓名：%s' % hanmei.get_name())
print('年龄：%d' % hanmei.get_age())
hanmei.say()
hanmei.set_name('hanmeimei')
print('姓名：%s' % hanmei.get_name())

# 继承
class Animal(object):
    def __init__(self,name):
        self.name = name
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,name)
        self.age = age
    def run(self):
        print('Dog is running')
    def eat(self):
        print('Eating meat...')

dog = Dog('Tom',12)
dog.run()
print(dog.name)
print(dog.age)
# 判断数据类型 isinstance
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

# 多态
def run_twice(animal):
    animal.run()

run_twice(Animal('Tom'))
run_twice(Dog('Tom',12))

# 获取对象信息
# print(dir('123'))
