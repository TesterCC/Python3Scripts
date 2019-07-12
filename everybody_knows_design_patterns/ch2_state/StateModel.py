#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-11 23:37'

"""
P32 什么是状态模式:
允许一个对象在其内部发生改变时改变其行为，使该对象看上去像改变了类型一样

注意开闭原则
注意表示状态的类应该只会有一个实例
"""

from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):
    """
    状态模式的上下文环境类
    """

    def __init__(self):
        pass

