#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/30 22:53'

"""
http://www.runoob.com/python3/python3-fibonacci-recursion.html
以下代码使用递归的方式来生成斐波那契数列
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""


def recur_fib(n):
    """
    递归函数输出斐波那契数列
    """
    if n <= 1:
        return n
    else:
        return recur_fib(n-1) + recur_fib(n-2)


if __name__ == '__main__':
    # 获取用户输入
    nterms = int(input("您要输出几项? "))
    # 检查输入的数字是否正确
    if nterms <= 0:
        print("输入正数")
    else:
        print("斐波那契数列:")
        for i in range(nterms):  # i 从0开始，对应recur_fib(n)
            print(recur_fib(i))