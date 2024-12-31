#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-23 11:34'

"""
2 输入并运行成功判断天数的程序。
3 输入并运行成功计算函数的程序。
4.输入并运行成功打印三角形的程序。
"""

import datetime

dtstr = "20181206"
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
another_dtstr = dtstr[:4] + '0101'
another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
print(int((dt - another_dt).days) + 1)

x = float(input())
a = 2
b = -45
c = 13
y = a * x ** 2 + b * x + c
print(x, y)


# 4.输入并运行成功打印三角形的程序。
n = int(input())
for i in range(n):
    line = " "*(n-1-i)+"@"*(2*i+1)
    print(line)
