# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/19 15:39'


"""
Python3插入排序
插入排序的基本操作是将一个数据插入到已经排序好的有序序列中，从而获得一个新的有序序列。

插入排序适合什么样的场景
适合数据量相对较小的排序需求场景。其时间复杂度为：O（n^2），是一种稳定的排序方法。

https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F
原地算法（in-place algorithm）基本上不需要额外辅助的数据结构,然而,允许少量额外的辅助变量来转换数据的算法。

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484587&idx=1&sn=fd38419ae2d67baaab9ad8da445066aa&chksm=e95da914de2a200283b09d218774129a6b6708a820f6c6bd06f55f298480d339b334508c95e1&mpshare=1&scene=23&srcid=01181OFYnho7P5YTwvJtAUt7#rd
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


def insert_sort(arr):
    """
    插入排序
    :param arr:
    """
    # 序列长度
    n = len(arr)

    # 当前需要排序的元素(arr[i])，跟已经排序好的最后一个元素比较(arr[i-1]==arr[j])
    for i in range(1, n):
        key = arr[i]    # 当前需要排序的元素
        j = i - 1
        while j >= 0:
            # 比较，进行插入排序
            if arr[j] > key:
                arr[j+1] = arr[j]
                arr[j] = key
            # j = j-1
            j -= 1

    return arr


if __name__ == '__main__':
    print("插入排序示例：")

    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print("生成随机序列：")
    print(random_data)

    # 插入排序
    sorted_data = insert_sort(random_data)

    # 打印排序结果
    print("完成插入排序的序列：")
    print(sorted_data)


