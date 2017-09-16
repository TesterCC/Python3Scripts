#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/16 15:53'

# A Byte of Python -- P64 -- Python3


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return "The numbers are equal."
    else:
        return y

print(maximum(2, 3))


def some_function():
    pass         # pass用于指示一个没有内容的语句块

print(some_function())