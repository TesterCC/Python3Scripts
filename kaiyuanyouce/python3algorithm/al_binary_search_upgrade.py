# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/16 22:17'


"""
二分查找[策略优化版本]
利用二分查找实现以下功能：

查找目标值在序列中第一次出现时的索引
查找目标值在序列中最后一次出现时的索引

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484078&idx=1&sn=7a0bbafa690a9d29ca71d89d438d29c4&scene=19#wechat_redirect
"""


def first_binary_search(seq, query):
    """
    first优先策略算法实现: 优先显示查找目标值在序列中第一次出现时的索引
    :param seq:待查序列
    :param query:要查找的目标
    """
    # start为起始索引, end为结束索引
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = (start + end) // 2   # // 整除
        if (mid == 0 and seq[mid] == query) or (seq[mid] == query and seq[mid-1] < query):
            # 这是实现first的最关键判断, 和普通二分法区别的关键
            # 在seq中找到目标query第一次出现的位置
            # 返回对应的索引值
            return mid
        elif seq[mid] < query:
            # 目标值大于中间值, 说明目标值在mid - end之间
            start = mid + 1
        else:
            # 目标值小于中间值, 说明目标值在start - mid之间
            end = mid - 1

    # 目标值不存在于seq中，返回None
    return None


def last_binary_search(seq, query):
    """
    last优先策略算法实现: 优先显示查找目标值在序列中最后一次出现时的索引
    :param seq:待查序列
    :param query:要查找的目标
    """
    # start为起始索引, end为结束索引
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = (start + end) // 2   # // 整除
        if (seq[mid] == query and mid == len(seq)-1) or (seq[mid] == query and seq[mid+1] > query):
            # 这是实现last的最关键判断, 和普通二分法区别的关键
            # 在seq中找到目标query第一次出现的位置
            # 返回对应的索引值
            return mid
        elif seq[mid] < query:
            # 目标值大于中间值, 说明目标值在mid - end之间
            start = mid + 1
        else:
            # 目标值小于中间值, 说明目标值在start - mid之间
            end = mid - 1

    # 目标值不存在于seq中，返回None
    return None


if __name__ == '__main__':
    print("二分查找first示例:")
    print("二分查找只适合有序的序列")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]

    # 返回2
    print("3第一次出现的索引位置为： ", first_binary_search(seq, 3))

    # 返回7
    print("5第一次出现的索引位置为： ", first_binary_search(seq, 5))

    # 返回13
    print("7第一次出现的索引位置为： ", first_binary_search(seq, 7))

    # 返回15
    print("8第一次出现的索引位置为： ", first_binary_search(seq, 8))

    print("-"*50)

    print("二分查找last示例:")
    print("二分查找只适合有序的序列")

    # 返回6
    print("3最后一次出现的索引位置为： ", last_binary_search(seq, 3))
    # in last_binary_serach has bug.  (seq,3)和(seq,4)有bug

    # 返回9
    print("5最后一次出现的索引位置为： ", last_binary_search(seq, 5))

    # 返回14
    print("7最后一次出现的索引位置为： ", last_binary_search(seq, 7))

    # 返回15
    print("8最后一次出现的索引位置为： ", last_binary_search(seq, 8))


