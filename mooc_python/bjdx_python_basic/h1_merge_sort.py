#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-22 23:20'

"""
归并排序

归并操作(merge)，也叫归并算法，指的是将两个顺序序列合并成一个顺序序列的方法。

归并排序（MERGE-SORT）是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
"""


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = int(len(lst) / 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))  # 左到右，从小到大，比较时假如小的值到list第一位
    merged.extend(right if right else left)
    return merged


data_lst = [6, 202, 100, 301, 38, 8, 1]
print(merge_sort(data_lst))
