#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-25 14:40'

"""
9-4 Python生成器原理 2:20
1. python中函数的工作原理
"""

def foo():
    bar()

def bar():
    pass

# python解释器是用C来写的
