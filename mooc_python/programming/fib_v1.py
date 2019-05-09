#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-09 11:09'

"""
斐波那契数列
F(n) = F(n-1) + F(n-2)

返回斐波那契数列之和
"""

def f(n):
    if n==1 or n==2:
        return 1

    else:
        return f(n-1) + f(n-2)

print(f(10))