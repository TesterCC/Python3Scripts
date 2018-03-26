#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/3/26 09:35'

"""
P4 1.1  数据结构与算法：Python语言描述
"""

def sqrt(x):
    y = 1.00
    while abs(y*y-x) > 1e-6:
        y = (y+x/y)/2
    return y