# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/16 21:09'


"""
数据结构与算法-二分查找

二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好。

其缺点是要求待查表为有序表，且插入删除困难。

因此，折半查找方法适用于不经常变动而查找频繁的有序列表。

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484076&idx=1&sn=cfd6c7aae01ae406bcbe5f3e449c0976&scene=19#wechat_redirect
"""


def binary_search(seq, query):
    """
    二分查找算法
    :param seq: 待查序列
    :param query: 要查找的目标
    """
    # start为起始索引, end为结束索引
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = (start + end) // 2   # // 整除, Python3需要这样
        val = seq[mid]
        if val == query:
            # 在seq中找到目标query, 返回对应的索引值
            return mid
        elif val < query:
            # 目标值query大于中间值, 说明目标值在mid - end之间
            start = mid + 1
        else:
            # 目标值小于中间值, 说明目标值在start - mid之间
            end = mid - 1

    # 目标值不存在于seq中，返回None
    return None


if __name__ == '__main__':
    print("二分查找示例")

    print("二分查找只适合有序的序列")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]

    print(seq)
    print(len(seq))

    print("---------二分查找--------")
    print("找到：", 5, " 索引是： ", binary_search(seq, 5))

    print("---------二分查找--------")
    print("找到：", 4, " 索引是： ", binary_search(seq, 4))

    print("---------二分查找--------")
    print("找到：", 13, " 索引是： ", binary_search(seq, 13))

    print("---------二分查找--------")
    print("找到：", 1, " 索引是： ", binary_search(seq, 1))

    print("---------二分查找--------")
    print("找到：", 25, " 索引是： ", binary_search(seq, 25))
