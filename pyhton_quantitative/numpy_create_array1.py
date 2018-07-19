#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/19 00:57'


"""
Python与量化投资从基础到实战 - P59-60
numpy使用 
金融数据分析主要用Pandas, NumPy的使用了解即可
"""

import numpy as np

data = [1, 2, 3, 4]

arr = np.array(data)

print(arr)
print(type(arr))

# 等长序列组成的列表将会被转换为一个多维数组
print("等长序列组成的列表将会被转换为一个多维数组:")

data1 = [data, data]

arr1 = np.array(data1)

print(arr1)
print(type(arr1))