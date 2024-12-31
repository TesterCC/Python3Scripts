#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/14 16:51'


"""
在Python中参数的传递要注意传入的是可更改的还是不可更改的对象。

可更改对象
在python中，可更改的对象有list（列表）、dict（字典）、set（集合）等等

不可更改对象
不可更改的对象有strings、tuples、numbers等等。

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484034&idx=1&sn=16dd09595166378832edcea56796565b&scene=19#wechat_redirect
"""


def sum_tuple(seq):
    """
    元组传递 求和
    :param seq:
    """
    sum = 0
    for s in seq:
        sum += s
    return sum


def str_join(str1, str2, str3):
    """
    字符串连接函数
    :param str1:
    :param str2:
    :param str3:
    :return: str1 + str2 + str3
    """
    return str1 + str2 + str3


if __name__ == '__main__':
    print(u"元组传参，求和实例：")
    tuple_1 = (1, 9, 10, 2, 2, 39, 0, 11, 20)
    print(tuple_1)

    res = sum_tuple(tuple_1)
    print(u"和为： %d" % res)

    print("-"*50)
    print(u"字符串连接实例: ")

    str1 = u"大家好，"
    str2 = u"我的目标是："
    str3 = u"全栈工程师"

    str_j = str_join(str1, str2, str3)
    print(str_j)

