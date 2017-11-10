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

if __name__ == '__main__':
    print(calc_sum(5,3,6,7))