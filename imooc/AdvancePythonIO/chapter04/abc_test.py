#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/4 13:43'

"""
4-2 抽象基类(abc模块) - 1
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):  # 定义这个可以迭代,支持for和切片
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


com = Company(['tester1', 'tester2'])
print(hasattr(com, "__len__"))
print(hasattr(com, "__del__"))
print(len(com))


class A:
    pass


class B(A):
    pass


# 在某些情况下希望判定某个对象的类型
from collections.abc import Sized

print(isinstance(com, Sized))

b = B()
print(isinstance(b, A))
