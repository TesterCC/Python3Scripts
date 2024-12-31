#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/16 20:42'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000
定制类
Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

能不能直接在实例本身上调用呢？
任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
"""


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Alice')
s()   # self参数不要传入

# __call__()还可以定义参数。
# 对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

# 我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(s))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))
