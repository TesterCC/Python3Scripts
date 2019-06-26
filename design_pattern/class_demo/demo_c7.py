#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 17:39'

"""
改变类的metaclass
"""

class CustomMetaclass(type):
    pass

class CustomClass(metaclass=CustomMetaclass):
    pass


print(type(object))
print(type(type))

print("-"*80)

obj = CustomClass()
print(type(CustomClass))
print(type(obj))

print("-"*80)

print(isinstance(obj, CustomClass))
print(isinstance(obj, object))