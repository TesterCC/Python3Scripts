# -*- coding:utf-8 -*-

"""
随机生成100个10至1000之间的数,对生成的100个数进行排序,
禁止使用Python自带的排序函数,要自己实现排序函数
"""

from random import randint


# data = [randint(10, 1001) for i in range(100)]
# print(data)


class MySort:
    """
       生成随机数,返回排序后的结果
       start, end为限制随机数生成的范围
       count为生成的随机数个数
    """

    def __init__(self, start, end, count):
        pass

    def mysort(self):
        pass


# 使用示例
if __name__ == '__main__':
    sorted_data = MySort(10, 1000, 100)

    # 打印排序后的结果
    print(sorted_data)



