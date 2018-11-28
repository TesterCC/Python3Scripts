#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/28 21:29'

from functools import singledispatch

"""
Python3中提供了functools.singledispatch这个装饰器
它是单分派泛函数，大家都知道c++中的函数是可以重载的，那么它的作用就和c++中函数的重载类似。
"""


@singledispatch
def show(obj):
    print(obj, type(obj), "obj")


@show.register(str)
def _(text):
    print(text, type(text), "str")


@show.register(int)
def _(n):
    print(n, type(n), "int")


@show.register(bool)
def _(b):
    print(b, type(b), "bool")


show(1)
show("xx")
show([1])
show(True)
show(None)
