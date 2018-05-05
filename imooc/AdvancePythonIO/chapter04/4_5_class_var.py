#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/5 13:44'

"""
4-5 类变量和实例变量
"""


class A:
    aa = 1  # 类变量

    def __init__(self, x, y):  # self代表实例
        self.x = x  # 实例变量
        self.y = y


a = A(2, 3)
A.aa = 11  # 改变类变量
a.aa = 100  # 给实例a增加了一个实例变量aa

print(a.x, a.y, a.aa)
print(A.aa)

b = A(3, 5)
print(b.aa)  # 因为实例b没有实例变量aa, 故向上取的类变量aa=11
