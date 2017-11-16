#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/16 12:05'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000
定制类
Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
"""


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

# 但会发现交互模式 直接敲变量不用print，打印出来的实例还是不好看
    __repr__ = __str__
# 因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

s = Student('Lily')

print(Student('Lily'))
print(s)

# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了
# 这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。

