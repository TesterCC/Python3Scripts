#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/8 23:03'

"""
4-10 super真的是调用父类吗？
"""


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        # super(B, self).__init__()   # Python2 继承父类的写法
        super().__init__()  # Python3 继承父类的写法
        

if __name__ == "__main__":
    b = B()
