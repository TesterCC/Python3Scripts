#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 13:20'

class ClassC:
    def __init__(self):
        print("ClassC.__init__")
        # return 3.0    # TypeError: __init__() should return None, not 'float'

c = ClassC()
print(c)