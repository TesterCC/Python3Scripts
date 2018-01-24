#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/24 03:41'


"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    02-闭包
      03.闭包再理解: 内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包。
"""

# closure3.py


def counter(start=0):
    count = [start]

    def incr():
        count[0] += 1
        return count[0]

    return incr


if __name__ == '__main__':
    c1 = counter(5)   # c1 -> incr
    print("c1:")
    print(c1())
    print(c1())

    c2 = counter(100)
    print("c2:")
    print(c2())
    print(c2())


