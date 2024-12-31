#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-26 13:20'


class ClassC:
    def __new__(cls, *args, **kwargs):
        print("new", args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print("init", args, kwargs)


c = ClassC("arg1", "arg2", a=1, b=2)
