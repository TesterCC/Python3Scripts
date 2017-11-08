#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/7 22:19'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000#0

利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
"""

from functools import reduce


def str2int(s):
    def char2num(c):
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
                }[c]
    return reduce(lambda x, y: x*10 + y, map(char2num, s))


def str2float(s):
    s_list = s.split('.')
    float_i = str2int(s_list[0])    # 整数部分
    float_f = str2int(s_list[1]) / (10**len(s_list[1]))    # 浮点数部分，利用科学计数法获得浮点数
    # float_f = str2int(s_list[1]) * (10**-len(s_list[1]))   # 浮点数部分，利用科学计数法获得浮点数

    return float_i+float_f


# print('str2float(\'123.456\') =', str2float('123.456'))

if __name__ == '__main__':
    teststr = '456.789'
    r = str2float(teststr)
    print('String \'%s\' str2float  = %s' % (teststr, r))