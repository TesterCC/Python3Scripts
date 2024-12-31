#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/7 18:24'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317849054170d563b13f0fa4ce6ba1cd86e18103f28000
高阶函数
"""


def add(x, y, f):
    return f(x)+f(y)

print(add(-5, 6, abs))