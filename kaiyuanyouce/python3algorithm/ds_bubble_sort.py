# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/16 18:09'


"""
冒泡排序

随机选是个1到1000的整数进行排序
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484580&idx=1&sn=c760532bcbecb0800246d909e93dc12c&chksm=e95da91bde2a200d031efa323364b8b010bf1c5fc029071bf84a94f1a06585937997076be64d&mpshare=1&scene=23&srcid=0116H5iPkBv1H9OdBrHB867E#rd
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


def bubble_sort(data_list):
    """
    冒泡排序
    :param data_list:
    """
    # 序列长度
    length = len(data_list)

    for i in range(0, length):
        for j in range(i+1, length):
            if data_list[i] > data_list[j]:
                data_list[i], data_list[j] = data_list[j], data_list[i]
    return data_list


if __name__ == '__main__':
    print("开源优测-积微速成计划基本功提升:")

    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print(random_data)

    # 插入排序
    sorted_data = bubble_sort(random_data)

    # 打印排序结果
    print("冒泡排序后的结果:")
    print(sorted_data)
