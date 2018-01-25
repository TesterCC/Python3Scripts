#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/25 18:29'

"""
装饰器执行的时间
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    08-2个装饰器-强调   
"""


def w1(func):
    print("--正在装饰1--")

    def inner():
        print("---正在验证权限1---")
        func()
    return inner


def w2(func):
    print("--正在装饰2--")

    def inner():
        print("---正在验证权限2---")
        func()
    return inner


# 只要Python解释器执行到了这个代码，那么就会自动的进行装饰， 而不是等到调用的时候才装饰
@w1   # 后包装的先拆，先等@w2执行完再看，返回的是func，再执行@w1
@w2
def f1():
    print("----f1----")


# 在调用f1之前，已经进行装饰了。 即将w1函数加载到内存
f1()



