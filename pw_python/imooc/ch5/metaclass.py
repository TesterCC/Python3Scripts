#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/9 01:30'

"""
#### 元类(Meta Class)是创建类的类

- 元类允许我们控制类的生成，比如修改类的属性等
- 使用type来定义元类
- 元类最常见的一个使用场景就是ORM框架
"""


# example 1
class Base:
    pass


class Child(Base):
    pass


# ipython: type?  可查看相关docstring
# type(name, bases, dict) -> a new type
# 等价定义：注意Base后要加上逗号，否则就是不是tuple了。
SomeChild = type('Child', (Base,), {})


# example 2, 类加上方法和类变量
class ChildWithMethod(Base):
    bar = True

    def hello(self):
        print('hello')


def hello(self):
    print('hello')


# 等价定义
ChildWithMethod = type(
    'ChildWithMethod', (Base,), {'bar': True, 'hello': hello}
)
