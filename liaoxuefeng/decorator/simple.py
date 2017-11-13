#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/13 15:22'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000
装饰器
"""


def now():
    print('2015-3-25')


f = now
f()
print(f.__name__)
print(now.__name__)
print(f.__name__ == now.__name__)
