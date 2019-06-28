#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-28 15:35'

"""
P28 
将数组元素按从小到大的顺序排列

选择排序   稳定的

时间复杂度：O(n^2)
"""


# 找出数组中最小的元素
def findSmallest(arr):
    smallest = arr[0]  # 存储最小的值
    smallest_index = 0  # 存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# 编写选择排序
def selectionSort(arr):  # 对数组进行排序
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)  # 找出数组中最小的元素，并将其加入到新数组中
        newArr.append(arr.pop(smallest_index))  # 加入新数组，同时从就数组中删除
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
