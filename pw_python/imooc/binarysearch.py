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
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid
        else:
            begin = mid + 1

    return -1


def test():
    """
    如何设计测试用例: (等价类划分)
    - 正常值功能测试
    - 边界值（如：最大最小值，最左最右值）
    - 异常值（如：None,空值,非法值）

    pytest binarysearch.py
    """
    # 正常值，包含有和无两种结果
    assert binary_search([0,1,2,3,4,5],1) == 1
    assert binary_search([0,1,2,3,4,5],6) == -1
    assert binary_search([0, 1, 2, 3, 4, 5], -1) == -1

    # 边界值
    assert binary_search([0, 1, 2, 3, 4, 5], 0) == 0
    assert binary_search([0, 1, 2, 3, 4, 5], 5) == 5
    assert binary_search([0], 0) == 0

    # 异常值
    assert binary_search([], 1) == -1
    # assert binary_search('asdkjal', 1) == -1  # TypeError: '>' not supported between instances of 'str' and 'int'
