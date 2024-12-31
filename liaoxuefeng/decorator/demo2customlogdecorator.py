#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/13 15:27'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000
假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

本质上，decorator就是一个返回函数的高阶函数。
如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
"""


# 要定义一个能打印日志的decorator, 且要自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):   # 包装器
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处
# 这个3层嵌套的decorator用法如下
@log('test execute')          # 把@log放到now()函数的定义处，相当于执行了语句 now = log('test execute')(now)
def now():
    print('2017-07-07')

f = now
print(now.__name__)    # wrapper
# 因为返回的那个wrapper()函数名字就是'wrapper'，
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

f()     # 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志

