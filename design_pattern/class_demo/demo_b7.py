#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 13:20'

"""
一个对象的创建过程
"""

class ClassD:
    def __new__(cls):
        print("ClassD.__new__")
        self = super().__new__(cls)
        print(self)
        return self

    def __init__(self):
        print("ClassC.__init__")
        print(self)

d = ClassD()
print(callable(ClassD))
print(callable(max))
print(callable(object))
