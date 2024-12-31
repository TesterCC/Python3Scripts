#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/9/12 09:39'

"""
《Python+Cookbook》第三版中文v3.0.0   
7.4 返回多个值的函数    P218

问题：构造一个可以返回多个值的函数

解决方案：
函数直接return一个元组就行
"""


def myfunc():
    return 1, 2, 3


print(myfunc())

# 实际上是先创建了一个元组然后返回
a, b, c = myfunc()  # 元组的解包

print(a)
print(b)
print(c)

x = myfunc()
print(x)

