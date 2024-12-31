#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/13 15:27'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000
假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

本质上，decorator就是一个返回函数的高阶函数。
"""


# 要定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):   # 包装器
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处
@log          # 把@log放到now()函数的定义处，相当于执行了语句 now = log(now)
def now():
    print('2017-07-07')


f = now
f()     # 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志

