#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 17:21'


class BaseClass:
    name = "Base"


class SubClass(BaseClass):
    pass


base = BaseClass()
sub = SubClass()

print(issubclass(SubClass, BaseClass))  # True
print(issubclass(SubClass, SubClass))   # True
print(issubclass(BaseClass, SubClass))  # False
print(SubClass.__bases__)
