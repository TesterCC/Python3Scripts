#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/15 17:55'

"""
custom double while
"""

a = 0
b = 3

while a < 3:
    # b = 2     # b设置在这里则输入结果不同
    print("a is {}".format(a))
    while b > 0:  # 内循环结束才回到外循环
        print("a->{}, b->{}".format(a, b))
        b -= 1
    a += 1
