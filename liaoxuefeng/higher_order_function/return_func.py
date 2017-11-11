#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/10 22:25'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000
实现一个可变参数的求和
"""


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


if __name__ == '__main__':
    print(calc_sum(5, 3, 6, 7))

    f = lazy_sum(1, 3, 5, 7, 9)
    print(f)      # 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
    print(f())    # 调用函数f时，才真正计算求和的结果

