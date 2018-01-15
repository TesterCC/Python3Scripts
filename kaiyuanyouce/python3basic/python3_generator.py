# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/15 20:42'

"""
生成器和迭代器
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484049&idx=1&sn=cc9a4ea66a8efa78f975d35a1d35bbef&scene=19#wechat_redirect
"""

import sys

"""
使用了yield的函数，我们称之为生成器
生成器返回的是一个迭代器的函数，只能用于迭代操作
在调用生成器的过程中，每次遇到yield时，函数就会暂停并保存当前运行状态，返回yield的值，并在下一次执行next() 方法时从当前位置继续运行。
"""


def fibonacci(n):
    """
    生成器实现斐波那切数列
    斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
    1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    """
    # 初始化变量
    a, b, count = 0, 1, 0

    while True:
        if count > n:
            return

        yield a

        a, b = b, a+b
        count = count + 1


if __name__ == '__main__':
    # 初始化生成器函数,产生一个生成器函数
    f = fibonacci(10)

    while True:
        try:
            print(next(f), end=' ')
        except StopAsyncIteration:
            sys.exit(0)
