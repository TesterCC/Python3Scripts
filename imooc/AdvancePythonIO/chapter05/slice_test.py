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
print(aList[::2])   # 隔一个取一个，获取偶数位置的元素
print(aList[1::2])  # 隔一个取一个，获取奇数位置的元素
print(aList[3:6])   # 指定切片开始和结束的位置
print(aList[0:100])  # 切片结束位置大于列表长度时，从列表尾部截断
print(aList[100:])   # 切片开始位置大于列表长度时，返回空列表