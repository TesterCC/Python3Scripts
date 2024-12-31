#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/27 11:27'

"""
用多种方法来实现单例模式：

使用模块
使用 __new__
使用装饰器（decorator）
使用元类（metaclass）
"""


class Singleton(object):
    """
    为了使类只能出现一个实例，我们可以使用 __new__ 来控制实例的创建过程
    """
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    a = 1


if __name__ == '__main__':
    mc1 = MyClass()
    mc2 = MyClass()
    mc3 = MyClass()

    print(mc1)
    print(mc2)
    print(mc3)
