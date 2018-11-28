#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/26 16:30'

import time

"""
Python 函数运行时间装饰器
Python2 Python3通用
"""


def count_runtime(func):
    def fi(*args, **kwargs):
        s = time.time()
        res = func(*args, **kwargs)
        print('====>>> RUN TIME: <%s> : %s' % (func.__name__, time.time() - s))
        return res

    return fi
