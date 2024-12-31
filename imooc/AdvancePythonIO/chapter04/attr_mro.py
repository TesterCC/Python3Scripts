#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/6 23:46'

"""
4-6 类和实例属性的查找顺序—mro查找

MRO：Method Resolution Order，即方法解析顺序，是python中用于处理二义性问题的算法

https://blog.csdn.net/qwertyupoiuytr/article/details/56439134
"""


# Python3  C3算法自己查资料了解

# 新式类
class D:
    pass


class E:
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass


print(A.__mro__)
