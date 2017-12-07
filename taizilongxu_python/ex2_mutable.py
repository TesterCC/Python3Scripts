#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/27 17:59'


a = []


def fun(a):
    print("func_in", id(a))  # func_in 53629256
    a.append(1)
print("func_out", id(a))    # func_out 53629256
print(fun(a))
print(a)  # [1]