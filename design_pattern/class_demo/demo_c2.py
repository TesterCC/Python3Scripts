#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 17:21'

"""
type()传入3个参数时，用来创建一个类
"""

ClassVariable = type('ClassA', (object,), dict(name="type test"))
a = ClassVariable()
print(type(a))
print(a.name)

class ClassB:
    name = "type test"

b = ClassB()
print(type(b))
print(b.name)