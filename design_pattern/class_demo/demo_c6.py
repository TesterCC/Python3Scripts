#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 17:21'

"""
metaclass是type类型
"""

class MyClass:
    pass

m = MyClass()
print(type(MyClass))
print(type(m))
print()

print(isinstance(m, MyClass))
print(isinstance(MyClass, type))