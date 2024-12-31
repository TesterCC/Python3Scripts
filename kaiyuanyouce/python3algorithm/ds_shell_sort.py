#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/29 06:24'

"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484601&idx=1&sn=31200af740d0c064f462ce2fad1a6d2e&chksm=e95da906de2a2010c1cedbd6fc3334d8ca482b6195171f031adcec8badfa664b188bac015cb6&mpshare=1&scene=23&srcid=0124A8pBDUqigsISIS0dzLeQ#rd

希尔排序(Shell's Sort)是插入排序的一种又称“缩小增量排序”（Diminshing Increment Sort），是直接插入排序算法的一种更高效的改进版本。

希尔排序是非稳定排序算法。

希尔排序属于插入类排序,是将整个有序序列分割成若干小的子序列分别进行插入排序。

排序过程：

先取一个正整数d1<n，把所有序号相隔d1的数组元素放一组，组内进行直接插入排序；
然后取d2<d1，重复上述分组和排序操作；
直至di=1，即所有记录放进一个组中排序为止。

"""

import random
import time


# 记录运行时间的装饰器 -- 通用写法
def timelog(func):
    """
    通用计时装饰器(使用通用写法)
    :param func:
    """
    def wrappedfunc(*args, **kwargs):
        print("%s was called..." % func.__name__)
        start_time = time.time()  # current time
        re = func(*args, **kwargs)
        end_time = time.time()    # end time
        print("run times: %f seconds" % (end_time - start_time))
        return re
    return wrappedfunc


def generator():
    """
    随机生成1-1000之间无序序列整数数据
    """
    random_data = []
    for i in range(0, 100):
        random_data.append(random.randint(1, 1000))

    return random_data


@timelog   # 为了记录函数运行的开始和结束时间
def shell_sort(data_list):
    """
    # 希尔排序
    :param data_list:
    """
    # 序列长度
    length = len(data_list)
    # 步长，数据可修改下，查看排序过程
    step = 5
    # 分组
    group = int(length/step)
    print("group: ", group)

    while group > 0:
        # 遍历分组，对所有分组进行排序
        for i in range(0, group):
            j = i + group
            # 对分组进行排序
            while j < length:
                k = j - group
                key = data_list[j]
                while k >= 0:
                    if data_list[k] > key:
                        data_list[k + group] = data_list[k]
                        data_list[k] = key
                    k = k - group
                j = j + group

        group = int(group/step)
    return data_list


if __name__ == '__main__':

    print("希尔算法演示Demo:")

    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print(random_data)

    # 排序
    length = len(random_data)
    sorted_data = shell_sort(random_data)

    # 打印排序结果
    print("排序完成的结果：")
    print(sorted_data)



