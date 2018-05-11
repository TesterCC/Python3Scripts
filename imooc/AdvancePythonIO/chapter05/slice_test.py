#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/9 22:09'

"""
5-4 实现可切片的对象
"""

aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]

print(aList[::])  # 返回包含原列表中所有元素的新列表
print(aList[::-1])  # 返回包含原列表中所有元素的逆序列表
