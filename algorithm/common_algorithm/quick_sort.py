#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/7 14:22'


"""
quick sort

http://blog.csdn.net/mrlevo520/article/details/77829204

1.先从数列中取出一个数作为基准数。
2.分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3.再对左右区间重复第二步，直到各区间只有一个数。

时间复杂度：
最坏时间复杂度：O(N^2)
平均时间复杂度：O(nlogn)

不稳定排序（选择排序也是不稳定的）

空间复杂度：
O(logn)
"""

# 快排 分片的思想+递归的思想，这是取了第一个array[0]为基准值
# 栈高为O(log(n)),栈长O(n),所以运行时间为栈高x栈长，也就是算法平均运算时间为O(nlog(n))


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]     # 取第一个列表元素为基准值，也可以取array[-1]最后一个，但范围对应要改成：array[:-1]
        less = [i for i in array[1:] if i < pivot]
        greater = [j for j in array[1:] if j >= pivot]   # 不考虑等于情况的话 List4有bug
        return quick_sort(less) + [pivot] + quick_sort(greater)     # [pivot] 否则拼合报错


if __name__ == '__main__':
    List = [3, 8, 12, 0, 3, 1, 5, 9, 6]
    List2 = [-3, 8, 12, 0, 3, 1, 5, 9, 6]
    List3 = [6]
    List4 = [4, 4]
    List5 = [5, 5, 5]
    print(quick_sort(List))
    print(quick_sort(List2))
    print(quick_sort(List3))
    print(quick_sort(List4))
    print(quick_sort(List5))


