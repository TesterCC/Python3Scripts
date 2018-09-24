#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/9/19 21:43'

"""
《Python+Cookbook》第三版中文v3.0.0   
7.5 定义有默认参数的函数    P219

问题：
你想定义一个函数或方法，它的一个或多个参数是可选的并且有一个默认值

解决方案：
如果默认参数是list，set，dict，可以使用None作为默认值

"""


def spam(a, b=42):
    print(a, b)


spam(1)
spam(1, 2)


def spam2(a, b=None):
    if b is None:
        b = []
    print(a, b)


spam2(1)
spam2(1, [2, 3, 4])
spam2(1, (2, 3, 4, 5))

# 仅仅想测试某个默认参数是否传递进来
_no_value = object()


def spam3(a, b=_no_value):
    if b is _no_value:
        print("No b value supplied.")
    print(a, b)


print("-" * 50)
spam3(1)
# spam3(1, 2)
spam3(1, None)
