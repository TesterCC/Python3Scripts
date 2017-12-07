#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/7 11:15'


"""
冒泡算法的原理是比较相邻的元素,如果第一个比第二个大（正序），就交换他们两个的位置，然后继续往下找，每次找出最大或最小的那个值放在顶端

两层循环的实现方式： 
1:双层for循环嵌套； 
2.判断条件如果满足，交换两数位置；

时间复杂度为O(n^2)
缺点: 冒泡排序解决了桶排序浪费空间的问题, 但是冒泡排序的效率特别低
"""


def bubble_sort(relist):
    lenlist = len(relist)
    for i in range(lenlist):
        for j in range(lenlist-i-1):
            if relist[j] > relist[j+1]:
                relist[j], relist[j+1] = relist[j+1], relist[j]
    return relist

if __name__ == '__main__':
    List = [3, 8, 12, 0, 3, 1, 5, 9, 6]
    print(bubble_sort(List))