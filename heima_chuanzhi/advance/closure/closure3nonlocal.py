#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/24 03:52'


"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    02-闭包
      03.闭包再理解: 内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包。
"""


def counter(start=0):
    """
    nonlocal访问外部函数的局部变量(python3)
    :param start:
    """
    def incr():
        nonlocal start
        start += 1
        return start

    return incr


if __name__ == '__main__':
    c1 = counter(5)
    print(c1())
    print(c1())

    c2 = counter(50)
    print(c2())
    print(c2())

    print("C1() return:")
    print(c1())
    print(c1())

    print("C2() return:")
    print(c2())
    print(c2())
