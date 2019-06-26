#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 11:51'

"""
P370 附录B
"""

class ClassA:
    def __new__(cls):
        print("ClassA.__new__")
        return super().__new__(cls)

    def __init__(self):
        print("ClassA.__init__")

    def __call__(self, *args, **kwargs):
        print("ClassA.__call__args:", args)

a = ClassA()
a("arg1","arg2")