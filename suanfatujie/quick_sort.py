#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-28 14:31'

"""
P52  quick sort  快速排序
时间复杂度: O(n*logn)

遇到使用任何已知算法都无法解决的问题，可以使用分而治之（divide and conquer, D&C）思路来解决。
D&C每次递归都必须缩小问题的规模。

D&C工作原理：
1.找出简单的基线
2.确定如何缩小问题的规模，使其符合基线条件


"""


def quick_sort(array):
    if len(array) < 2:
        return array    # 基线条件：为空或只包含一个元素的数组是"有序"的
    else:
        pivot = array[0]    # 取第一个列表元素为基准，递归条件
        less = [i for i in array[1:] if i <= pivot]    # 由所有小于等于基准值的元素组成的子数组
        greater = [j for j in array[1:] if j > pivot]  # 由所有大于基准值的元素组成的子数组
        return quick_sort(less) + [pivot] + quick_sort(greater)  # [pivot]否则拼合报错


def quick_sort_v2(array:list) -> list:
    if len(array) < 2:
        return array

    pivot = array[0]   # baseline
    less = [ i for i in array[1:] if i <= pivot]
    more = [ i for i in array[1:] if i > pivot]
    return quick_sort_v2(less) + [pivot] + quick_sort_v2(more)


if __name__ == '__main__':
    List = [3, 8, 12, 0, 3, 1, 5, 9, 6]
    List2 = [-3, 8, 12, 0, 3, 1, 5, 9, 6]
    List3 = [6]
    List4 = [4, 4]
    List5 = [10, 5, 2, 3]
    # print(quick_sort(List))
    # print(quick_sort(List2))
    # print(quick_sort(List3))
    # print(quick_sort(List4))
    # print(quick_sort(List5))


    print(quick_sort_v2(List))
    print(quick_sort_v2(List2))
    print(quick_sort_v2(List3))
    print(quick_sort_v2(List4))
    print(quick_sort_v2(List5))
