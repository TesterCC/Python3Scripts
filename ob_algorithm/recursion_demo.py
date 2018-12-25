#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-25 09:14'

"""
构成递归需具备的条件：
1. 子问题须与原始问题为同样的事，且更为简单；
2. 不能无限制地调用本身，须有个出口，化简为非递归状况处理。

practice:
use recursion print "抱着抱着抱着我的小鲤鱼我的我的我的"
"""

def func(x):
    if x > 0:
        print('抱着', end='')
        func(x-1)
        print('我的', end='')
    else:
        print('我的小鲤鱼', end='')

if __name__ == '__main__':
    func(3)