#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/14 03:15'


"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484034&idx=1&sn=16dd09595166378832edcea56796565b&scene=19#wechat_redirect
"""


def sum(a, b):
    c = a + b
    return c


def multi():
    """
    九九乘法表
    """
    data = []
    for i in range(1, 10):
        line = []
        for j in range(i, 10):
            line.append(u"%d * %d = %2d" % (i, j, i*j))
        data.append(line)
    return data


if __name__ == '__main__':
    print(u"函数定义，计算和")
    # 调用函数
    c = sum(1, 2)
    print(c)

    print(u"九九乘法表实例：")
    data = multi()
    for d in data:
        print(d)
