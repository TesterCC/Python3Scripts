#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/23 17:28'

"""
冒泡排序：
最优时间复杂度：O(n)
平均时间复杂度：O(n^2)
最差时间复杂度：O(n^2)
空间复杂度：O(1)
稳定性：稳定

ref:
https://pegasuswang.github.io/python_data_structures_and_algorithms/12_%E5%9F%BA%E6%9C%AC%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95/basic_sort/

execute unittest:

cd ~/algorithm/basic
../pytest.sh bubble_sort.py
"""

def bubble_sort(seq: list) -> list:
    n = len(seq)
    for i in range(n - 1):
        # print(seq)  # for debug and understanding, 打印出来让你看清楚每一轮最高、次高、次次高
        for j in range(n - 1 - i):
            if seq[j] > seq[j + 1]:  # 用>升序，用<降序.这里之所以 n-1 还需要 减去 i 是因为每一轮冒泡最大的元素都会冒泡到最后，无需再比较
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq

def test_bubble_sort():
    seq = list(range(10))  # 注意 python3 返回迭代器，需要用 list 强转; python2 range 返回的就是 list
    import random
    random.shuffle(seq)  # shuffle inplace 操作，打乱数组
    print(f"shuffle seq: {seq}")
    bubble_sort(seq)
    assert seq == sorted(seq)  # 注意: 内置的 sorted 就不是 inplace 的，它返回一个新的数组，不影响传入的参数
    print(f"sorted seq: {seq}")  # bubble_sort()是 inplace的

    assert bubble_sort([]) == []
    assert bubble_sort([7]) == [7]
    assert bubble_sort([88]) == [88]
