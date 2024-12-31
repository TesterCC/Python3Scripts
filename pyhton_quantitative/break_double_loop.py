#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/15 18:14'


"""
Python与量化投资从基础到实战  P36

break语句用在双层循环中，跳出最内层的循环的示例
"""

a = 5
while a <= 8:
    a += 1
    for i in range(1, 3):
        print("a --> {}, i --> {}".format(a, i))

        if i == 2:
            break
