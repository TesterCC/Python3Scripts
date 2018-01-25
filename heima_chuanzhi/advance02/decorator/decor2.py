#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/25 17:58'

"""
01.python高级1
  02.python高级2-生成器、闭包、装饰器
    05-装饰器 03 多个装饰器
完成数据包裹，增加html效果
"""


# 定义函数：完成包裹数据
def makeBold(fn):
    """
    加粗效果
    """
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped    # 返回的是函数而非函数的调用


# 定义函数：完成包裹数据
def makeItalic(fn):
    """
    斜体效果
    """
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped    # 返回的是函数而非函数的调用


#  定义函数：完成包裹数据
def makeUnderline(fn):
    """
    下划线效果
    """
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped    # 返回的是函数而非函数的调用


@makeBold
def test1():
    return "hello world-1"


@makeItalic
def test2():
    return "hello world-2"


@makeUnderline
def test3():
    return "hello world-3"


@makeBold
@makeItalic
@makeUnderline
def test4():
    return "hello world-4"


print(test1())
print(test2())
print(test3())
print(test4())

