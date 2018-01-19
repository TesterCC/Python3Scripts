# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/19 22:08'


"""
Python3快速排序
设要排序的数组是A[0]……A[N-1]，首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面，这个过程称为一趟快速排序。

https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484588&idx=1&sn=bdc6224ec08dd94f03718fac6df5f0ee&chksm=e95da913de2a2005933dfb73daf09276c08324baa6b59a0a168c27ef71520ffa3126443fb47c&mpshare=1&scene=23&srcid=0119YD0f7rcOhAL24NJg0H18#rd
"""


import random


def generator():
    """
    随机生成1-1000之间无序序列整数数据
    """
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))

    return random_data


def quick_sort(data_list, start, end):
    """
    快速排序
    :param data_list:
    :param start:
    :param end:
    """
    # 判断是否需要进行排序
    if start >= end:
        return data_list

    # 设置排序基准值，这里我们设置为第一个元素值
    base = data_list[start]
    left = start
    right = end

    while left < right:
        # 对data_list从右往左找第一个比base小的数的索引位置
        while left < right and data_list[right] >= base:
            right = right - 1

        # 对data_list从左往右找第一个比base大的数的索引位置
        while left < right and data_list[left] <= base:
            left = left + 1

        # 交换数据初步排序
        data_list[left], data_list[right] = data_list[right], data_list[left]

    # 把找到比base小的数据与base交换位置
    data_list[start], data_list[left] = data_list[left], data_list[start]

    # 进入下一轮排序
    quick_sort(data_list, start, left - 1)

    quick_sort(data_list, right + 1, end)

    return data_list


if __name__ == '__main__':
    print("快速排序示例")

    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print("生成随机序列：")
    print(random_data)

    # 快速排序
    length = len(random_data)
    sorted_data = quick_sort(random_data, 0, length - 1)

    # 打印排序结果
    print("完成快速排序的序列：")
    print(sorted_data)

