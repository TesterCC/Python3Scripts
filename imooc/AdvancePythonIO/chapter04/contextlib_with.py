#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/8 08:59'

"""
4-13 contextlib简化上下文管理器
"""

import contextlib


# 不习惯用这个就直接用with语句
@contextlib.contextmanager
def file_open(filename):
    print("file open")  # 对应__enter__
    yield {}
    print("file end")  # 对应__exit__


with file_open("test.txt") as f:
    print("file processing")
