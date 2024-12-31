#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/7 15:51'

"""
选择排序

最优时间复杂度：O(n^2)
最坏时间复杂度：O(n^2)
稳定性：不稳定（考虑升序每次选择最大的情况）

选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在 未排序序列 中找到最小（大）元素，存放到 排序序列 的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

ref:
https://www.bilibili.com/video/BV1at411Y71D?p=32
"""

# 选择排序， 现写内层，再写外层
def selection_sort(alist:list):
    n = len(alist)

    for j in range(n-1):  # j in 0 ~ n-2
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index], alist[j]

    return alist

if __name__ == '__main__':
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    selection_sort(alist)
    print(alist)