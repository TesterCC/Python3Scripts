#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/8 09:03'

"""
4-12 python中的with语句
"""


# 上下文管理器协议

class Sample:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print('doing something')


with Sample() as sample:
    sample.do_something()
