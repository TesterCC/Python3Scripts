#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/15 20:53'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000
生成器

斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

import sys


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b     # 用yield即是把函数改成generator, b的值为fib数列中b的前两个数字之和
        a, b = b, a+b
        n = n+1
    return 'done'


# 通常把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
for n in fib(7):
    print(n, end="  ")

print("\n"+"-"*50)
print("换一种遍历方式:")

g = fib(6)
while True:
    try:
        x = next(g)
        print(x, end="  ")
    except StopIteration as e:
        # print('Generator return value: %s' % e.value)
        # print('\nGenerator return value:', e.value)
        sys.exit()

