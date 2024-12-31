#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/19 00:57'


"""
Python与量化投资从基础到实战 - P60
numpy使用 
金融数据分析主要用Pandas, NumPy的使用了解即可
"""

import numpy as np

# 除np.array函数，还有其他函数可以快速创建数组

# 创建3x3全0数组

arr = np.zeros((3, 3))

print(arr)
print(type(arr))

# 创建3x3全0数组

arr1 = np.ones((3, 3))    # 创建3x3全1数组

print(arr1)

# 创建1~10且差为2的等差数列
print("创建1~10且差为2的等差数列:")
arr2 = np.arange(1, 10, 2)
print(arr2)


# 创建1~10且长度为4的等差数列
print("创建1~10且长度为4的等差数列:")

arr3 = np.linspace(1, 10, 4)
print(arr3)





