#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-27 17:49'

"""
自定义metaclass:
1.metaclass.__init__进行一些初始化操作
2.metaclass.__call__创建实例，会调用class的__new__和__init__方法
3.class.__new__进行具体的实例化操作，并返回一个实例对象obj
4.class.__init__对返回的的实例对象obj进行初始化
5.返回一个用户真正需要使用的对象obj
"""


class CustomMetaclass(type):
    def __init__(cls, what, bases=None, dict=None):
        print("CustomMetaclass.__init__ cls:", cls)
        super().__init__(what, bases, dict)

    def __call__(cls, *args, **kwargs):
        print("CustomMetaclass.__call__ args:", args, kwargs)
        self = super(CustomMetaclass, cls).__call__(*args, **kwargs)
        print("CustomMetaclass.__call__ self:", self)
        return self


class CustomClass(metaclass=CustomMetaclass):
    def __init__(self, *args, **kwargs):
        print("CustomClass.__init__, self:", self)
        super().__init__()

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        print("CustomClass.__new__, self:", self)
        return self

    def __call__(self, *args, **kwargs):
        print("CustomClass.__call__ args:", args)


obj = CustomClass("Meta arg1", "Meta arg2", kwarg1=1, kwarg2=2)
print(type(CustomClass))
print(obj)
obj("arg1", "arg2")
