#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 11:54'


class ClassB:
     def __new__(cls, *args, **kwargs):
         print("ClassB.__new__")
         # return super().__new__(cls)  # correct
         return 3.0

     def __init__(self):
         print("ClassB.__init__")

b = ClassB()
print(b)