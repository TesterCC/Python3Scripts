#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/15 16:43'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186739713011a09b63dcbd42cc87f907a778b3ac73000
使用__slots__
"""


# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Student(object):
    __slots__ = ('name', 'age')   # 用tuple定义允许绑定的属性名称

s = Student()    # 创建新的实例
s.name = "Lily"   # 绑定属性'name'
s.age = 20    # 绑定属性'age'
# s.score = 99   # 绑定属性'score'    # 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。


class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 120

print(g.score)

# 如果基类使用了slots，子类没有使用slots的情况下子类的属性可以在运行时任意扩展。子类的属性自动继承基类属性
# 如果基类使用了slots,子类也使用了slots,子类在运行时的可扩展属性是基类的slots + 子类的slots。不在基类slots中的属性子类不能继承。
# 另一个比较有意思的地方是，如果基类包含一个实例属性，而它没有在基类的slots中，那么子类无法继承此属性，也无法扩展此属性。
# 你可以通过删除子类(sub class的代码中的__slots__)的slots让子类任意扩展，或者在子类的slots中增加 age 属性,来让子类扩展或者继承 age 属性。

class ClassStudent(Student):
    __slots__ = ('gender')

c = ClassStudent()
c.name = 'Tom'
c.age = 18
c.gender = 'Male'

# c.score = 105