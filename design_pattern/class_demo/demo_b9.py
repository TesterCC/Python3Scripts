#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 13:20'

"""
callable() and __call__
"""

class ClassE:
    pass

class ClassF:
    def __call__(self, *args, **kwargs):
        print("This is __call__ function, args:",args)

e = ClassE()
print(callable(e))

f = ClassF()
print(callable(f))
f("arg1","arg2")
