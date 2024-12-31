#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/20 17:13'


"""
Python与量化投资从基础到实战 - P68

Pandas数据结构:
Series        一维数组，与NumPy中的一维Array类似  
DataFrame     二维的表格型数据结构
Panel         三维数组
"""

import pandas as pd

obj = pd.Series([40, 12, -3, 25])

print(obj)

print(obj[0])
print(obj[2])

print(obj.index)
print(obj.values)