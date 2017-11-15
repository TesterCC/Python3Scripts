#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/15 16:25'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186739713011a09b63dcbd42cc87f907a778b3ac73000
使用__slots__
"""


class Student(object):
    pass

s = Student()
s.name = 'Lily'   # 动态给实例绑定一个属性
print(s.name)


# 动态给实例绑定一个属性
def set_age(self, age):   # 定义一个函数作为实例方法
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)   # 给实例绑定一个方法

s.set_age(25)    # 调用实例方法

print(s.age)  # 测试结果

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的

# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s2 = Student()

# 给class绑定方法后，所有实例均可调用
s.set_score(100)
s2.set_score(99)

print(s.score)
print(s2.score)

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。