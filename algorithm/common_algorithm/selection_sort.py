#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/7 13:51'


"""
这个算法一般考察没有快速排序和冒泡排序多

选择排序是一种简单直观的排序算法，通过 不断选择未排序部分的最小元素 并放置到已排序部分的末尾，逐步完成整体排序。
其核心特点是 减少交换次数，但时间复杂度较高，适用于小规模数据或教学场景。

核心思想：
1.遍历未排序部分：从数组的未排序区间中找到最小元素。
2.交换位置：将最小元素与未排序区间的第一个元素交换。
3.重复操作：逐步缩小未排序区间，直到数组完全有序。

时间复杂度
所有情况：O(n^2)O，无论数据是否有序，均需遍历 n(n−1)/2 次比较。
空间复杂度：
O(1)，原地排序，仅需常数级额外空间。

不稳定排序
---

http://blog.csdn.net/mrlevo520/article/details/77829204
基本思想(参考自–选择排序)：
第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；
第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
以此类推，
第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。


http://www.cnblogs.com/qlshine/p/6018018.html
选择排序每次只记录最大数的索引值. 类似于冒泡排序, 也是要比较n-1次, 
区别是冒泡排序每次都交换, 选择排序只在最后比较完后才进行交换
"""


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 找到未排序区间的最小值索引
        min_index = i
        # 仅在未排序区间内寻找最小值，避免重复比较已排序部分的元素。
        # 为什么从i+1开始：已排序部分无需再比较：当外层循环进行到第 i 轮时，前 i 个元素已经通过之前的交换操作确定了最终位置（即已排序完成）。
        # 通过这个循环会找到 值比第i个索引所代表值小的那个索引
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 将最小值交换到未排序区间的起始位置
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == '__main__':
    List = [3, 8, 12, 0, 3, 1, 5, 9, 6]
    List2 = [-3, 8, 12, 0, 3, 1, 5, 9, 6]
    List3 = [6]
    List4 = [4, 4]
    List5 = [5, 5, 5]
    print(selection_sort(List))
    print(selection_sort(List2))
    print(selection_sort(List3))
    print(selection_sort(List4))
    print(selection_sort(List5))

