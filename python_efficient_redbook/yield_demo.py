#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/17 11:29'

"""
Red book P235 use yield
使用yield定义的迭代器也被称为生成器
"""


def demoIterator():
    print("I'm in the 1st call of next()")
    yield 1
    print("I'm in the 2ed call of next()")
    yield 3
    print("I'm in the 3rd call of next()")
    yield 9


for i in demoIterator():
    print(i)

