#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/7 14:18'

"""
冒泡排序

最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
最坏时间复杂度：O(n^2)
稳定性：稳定

冒泡排序（英语：Bubble Sort）是一种简单的排序算法。它重复地遍历要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

冒泡排序算法的运作如下：

比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

ref:
https://www.bilibili.com/video/BV1at411Y71D?p=31
"""

"""
method 1的思路
i代表当前index，j代表当前行index
alist长度为n, 索引是 0, n-1

# i  0 ~ n-2    range(0,n-1)    j=0
# i  0 ~ n-3    range(0,n-1-1)    j=1
# i  0 ~ n-4    range(0,n-1-2)    j=2
...
# i             range(0,n-1-j)    j=n

从头开始
[0,1,2,3,...,n-2]
"""

import time
import datetime


# method 1  易理解，记不住就现写内层循环再写外层循环,还是建议记忆这个，而且这个写法能做优化，可以扩展谈
def bubble_sort(alist: list) -> list:
    # a = time.time()
    # b = datetime.datetime.now()
    n = len(alist)
    for j in range(n - 1):  # 外层循环控制要走多少次
        for i in range(n - 1 - j):  # 内层循环控制从头走到尾比较  减去已排序过的数，关键记忆这个
            if alist[i] > alist[i + 1]:  # 如果第一个比第二个大（升序），就交换他们两个。
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

    # print(time.time()-a)
    # print(datetime.datetime.now()-b)
    return alist


"""
method 2思路
从尾部开始
[n-1,n-2,n-3,...,1]
"""


# method 2  易记忆，且实际运行效率更高
def bubble_sort_v2(alist: list) -> list:
    # a = time.time()
    for j in range(len(alist) - 1, 0, -1):   # 这里相较第一种做了优化
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i + 1]:  # 如果第一个比第二个大（升序），就交换他们两个。
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    # print(time.time() - a)
    return alist


# method 1 update  判断有序就立刻退出，在完全有序情况下优势明显
def bubble_sort_v3(alist: list) -> list:
    # a = time.time()
    n = len(alist)
    for j in range(n - 1):  # 外层循环控制要走多少次
        count = 0
        for i in range(n - 1 - j):  # 内层循环控制从头走到尾比较  减去已排序过的数
            if alist[i] > alist[i + 1]:  # 如果第一个比第二个大（升序），就交换他们两个。
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:
            # print(time.time() - a)
            return alist
    # print(time.time() - a)
    return alist


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("=" * 20 + " method 1 " + "=" * 20)
    # print(li)
    bubble_sort(li)
    print(li)

    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("=" * 20 + " method 2 " + "=" * 20)
    # print(li)
    bubble_sort_v2(li)
    print(li)

    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("=" * 20 + " method 3 " + "=" * 20)
    # print(li)
    bubble_sort_v3(li)
    print(li)

    print("=" * 20 + " order test " + "=" * 20)
    li4 = [1, 2, 3, 4, 5, 6]
    bubble_sort(li4)
    print(li4)

    li2 = [1, 2, 3, 4, 5, 6]
    bubble_sort_v2(li2)
    print(li2)

    li3 = [1, 2, 3, 4, 5, 6]
    bubble_sort_v3(li3)
    print(li3)
