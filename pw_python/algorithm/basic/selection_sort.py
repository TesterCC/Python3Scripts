#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/23 17:41'

"""
选择排序：
最优时间复杂度：O(n^2)
平均时间复杂度：O(n^2)
最差时间复杂度：O(n^2)
空间复杂度：O(1)
稳定性：不稳定

ref:
https://pegasuswang.github.io/python_data_structures_and_algorithms/12_%E5%9F%BA%E6%9C%AC%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95/basic_sort/

选择可以理解为 一个 0 到 n-1 的迭代，每次向后查找选择一个最小的元素。

execute unittest:

cd ~/algorithm/basic
../pytest.sh selection_sort.py
"""


def selection_sort(seq: list) -> list:
    n = len(seq)
    for i in range(n - 1):
        min_index = i
        # print(seq)  # for debug
        for j in range(i + 1, n):
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq


def test_selection_sort():
    seq = list(range(10))
    import random
    random.shuffle(seq)
    print(f"shuffle seq: {seq}")
    selection_sort(seq)   # in place
    print(f"ordered seq: {seq}")
    assert seq == sorted(seq)
