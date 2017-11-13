#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/13 16:07'

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
"""
from functools import wraps


def log(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('begin call')
        func(*args, **kwargs)   # 函数调用
        print('end call')

    return wrapper


@log
def now():
    print('2017-07-07')


# test
f = now
# print(f.__name__)
f()