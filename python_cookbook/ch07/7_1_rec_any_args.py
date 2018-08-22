#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/22 15:41'

"""
《Python+Cookbook》第三版中文v3.0.0   
7.1 可接受任意数量参数的函数    P215
"""


# Scenario 1: 让一个函数能接受任意数量的位置参数，使用一个*参数
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


# sample use
print(avg(1, 2))
print(avg(1, 2, 3, 4, 5))


# Scenario 2: 接受任意数量的关键字参数，使用一个**开头的参数
import html

def make_element(name, value, **attrs):
    pass