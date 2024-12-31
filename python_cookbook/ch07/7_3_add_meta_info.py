#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/9/11 23:43'

"""
《Python+Cookbook》第三版中文v3.0.0   
7.3 给函数参数增加元信息    P217-218
使用函数参数注解   单注释的主要用途还是文档
"""


def add(x: int, y: int) -> int:
    return x + y


# Python解释器不会对注解添加语义

print(add(3, 7))

help(add)

# 函数注解只存储在函数的__annotations__属性中
print(add.__annotations__)
