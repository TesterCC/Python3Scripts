#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-30 14:21'

# 3-7 Python单元测试

def binary_search(array, target):
    # 二分查找
    if not array:
        return -1

    begin, end = 0 , len(array)

    while begin < end:
        mid = begin + (end - begin) // 2   # python3
