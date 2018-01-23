#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/24 03:39'

"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    02-闭包
      04.看一个闭包的实际例子
"""


def line_conf(a, b):
    """
    :param a:
    :param b:
    :return: line
    """

    def line(x):
        # 函数line与变量a,b构成闭包
        return a * x + b

    return line


if __name__ == '__main__':
    line1 = line_conf(1, 1)
    line2 = line_conf(4, 5)

    print(line1(5))
    print(line2(5))

