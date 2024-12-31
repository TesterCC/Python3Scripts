#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/15 11:51'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431866385235335917b66049448ab14a499afd5b24db000
获取对象信息
"""


class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()


# 基本类型都可以用type()判断  它返回对应的Class类型
print(type(123))
print(type("test"))
print(type(None))
print(type(abs))   # builtin_function_or_method
print(type(a))   # __main__.Animal

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types


def fn():
    pass

print("--------------------")
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType )
print(type(lambda x: x*x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# object -> Animal -> Dog -> Husky
print("--------------------")
print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Dog) and isinstance(d, Animal))
# 但是，d不是Husky类型
print(isinstance(d, Husky))

# 能用type()判断的基本类型也可以用isinstance()判断
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
# 比如，获得一个str对象的所有属性和方法
print("--------------------")
print(dir('ABC'))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
# 下面的代码是等价的
print(len('ABC'))
print('ABC'.__len__())


# 自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()
# 测试该对象的属性
print(hasattr(obj, 'x'))   # 有属性'x'吗？
print(obj.x)
print(hasattr(obj, 'y'))   # 有属性'y'吗？

setattr(obj, 'y', 19)    # 设置一个属性'y'
print(hasattr(obj, 'y'))     # 有属性'y'吗？
print(getattr(obj, 'y'))   # 获取属性'y'
print(obj.y)    #  获取属性'y'

print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

print(hasattr(obj, 'power'))   # 有属性'power'吗？
print(getattr(obj, 'power'))   # 获取属性'power'

fn = getattr(obj, 'power')     # 获取属性'power'并赋值到变量fn
print(fn())     # 调用fn()与调用obj.power()是一样的