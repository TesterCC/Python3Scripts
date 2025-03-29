#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/20 21:07'

'''
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484016&idx=2&sn=f16f4b5accfdb85e258f1819f4779eb6&scene=19#wechat_redirect
'''

import math_demo
import cmath
import random


if __name__ == '__main__':
    x = 100
    y = 1.9

    print(u"常用数学函数")

    # 返回x的绝对值
    print(abs(x))

    # 反回最大值
    print(max(x, y))

    # 反回最小值
    print(min(x, y))

    # 计算y^2
    print(pow(y, 2))

    # 返回平方根
    print(math_demo.sqrt(y))

    print(u"常用随机函数")
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    # 从列表a中随机选中一个
    print(random.choice(a))

    # 从指定的范围(2-100按5递增的数据集)中随机选中一个
    print(random.randrange(2, 100, 5))

    # 生成一个随机数，它在(0,1)之间
    print(random.random())

    print(u"常用三角函数")
    x = 100

    # 返回x的反余弦弧度值
    print(cmath.acos(x))

    # 返回x的正弦弧度值
    print(cmath.sin(x))

    # 返回x的余弦弧度值
    print(cmath.cos(x))

    print(u"数字常量")
    print(cmath.pi)      # 返回PI
    print(cmath.e)      # 返回e

