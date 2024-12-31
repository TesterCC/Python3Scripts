#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/7 21:50'

"""
如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数

https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000
"""

from functools import reduce


def char2num(s):
    return {'0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
            }[s]


def str2int(s):      #  s代表一个字符串str
    return reduce(lambda x, y: x*10 + y, map(char2num, s))    # lambda 匿名函数


if __name__ == '__main__':
    r = str2int('345623')
    print(r)
    print(type(r))
