#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/7 13:51'


"""
http://blog.csdn.net/mrlevo520/article/details/77829204
​基本思想(参考自–选择排序)：
第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；
第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
以此类推，
第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。


http://www.cnblogs.com/qlshine/p/6018018.html
选择排序每次只记录最大数的索引值. 类似于冒泡排序, 也是要比较n-1次, 
区别是冒泡排序每次都交换, 选择排序只在最后比较完后才进行交换
"""


def select_sort(relist):
    len_list = len(relist)
    for i in range(len_list):
        min_index = i
        for j in range(i+1, len_list):   # 这个循环会找到 值比第i个索引所代表值小的索引
            if relist[j] < relist[min_index]:
                min_index = j
        relist[i], relist[min_index] = relist[min_index], relist[i]
    return relist


if __name__ == '__main__':
    List = [3, 8, 12, 0, 3, 1, 5, 9, 6]
    List2 = [-3, 8, 12, 0, 3, 1, 5, 9, 6]
    List3 = [6]
    List4 = [4, 4]
    List5 = [5, 5, 5]
    print(select_sort(List))
    print(select_sort(List2))
    print(select_sort(List3))
    print(select_sort(List4))
    print(select_sort(List5))

