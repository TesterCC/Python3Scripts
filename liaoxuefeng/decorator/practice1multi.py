#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/13 16:23'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000#0
思考一下能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
"""
from functools import wraps
from time import time


start_time = time()  # current time

print("\n***Start to Run ......***\n")


def log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("函数{0}()即将执行，此时系统已运行了 {1} 秒\n".format(func.__name__, time() - start_time))
            startTime = time()
            return (func(*args, **kwargs), print("函数{0}()执行了 {1} 秒后，结束了自己\n".format(func.__name__, time()-startTime)))[0]
        return wrapper
    return (decorator, print("我是一个带参数的装饰器，我的参数是 '{}' ".format(text)))[0] if text.__str__() == text else decorator(text)


@log
def abc():
    print("test by abc")

@log("Lily")
def efg():
    print("test by efg")


abc()
efg()

print("运行结束，一共运行了", time()-start_time, "秒")

