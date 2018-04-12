#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/12 23:00'

"""
《Python+Cookbook》第三版中文v3.0.0
1.1 解压序列赋值给多个变量
"""

P = (4, 5)
x, y = P
print("x->{0}, y->{1}".format(x, y))

data = ['ACME', 50, 91.1, (2012, 12, 21)]

name, shares, price, (year, mon, day) = data

print(name, shares, price, year, mon, day)

s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)

# 有时候,你可能只想解压一部分,丢弃其他的值。对于这种情况 Python 并没有提 供特殊的语法。但是你可以使用任意变量名去占位,到时候丢掉这些变量
# 就行了。
data2 = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print("shares--{}, price--{}".format(shares, price))