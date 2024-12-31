#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 11:54'


class Sample:
    def __str__(self):
        return "SAMPLE"

class ClassB:
     def __new__(cls):
         print("ClassB.__new__")
         # return Sample()   # 这样的写法也可以
         return super().__new__(Sample)

     def __init__(self):
         print("ClassB.__init__")

b = ClassB()
print(b)
print(type(b))