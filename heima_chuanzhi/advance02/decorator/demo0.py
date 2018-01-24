#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/24 15:14'

"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    05-装饰器 01
"""


# example 1
def foo():
    print('foo')


foo  # 表示是函数
foo()   # 表示执行foo函数


# example 2
def foo():
    print('foo')


foo = lambda x: x + 1   # foo指向另一个函数

r = foo(3)   # # 执行下面的lambda表达式，而不再是原来的foo函数，因为foo这个名字被重新指向了另外一个匿名函数

print(r)

