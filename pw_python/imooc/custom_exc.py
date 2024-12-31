#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-09 14:46'

"""
3-4 Python异常机制

为什么自定义异常不是继承自BaseException?
捕获父类异常，其所有子类异常都在捕获范围之内。
根据Exception的层级，BaseException层级在KeyboradInterrupt之上（也在其它Excption之上），
如果自定义异常继承自BaseException，则会捕获BaseException,则其子类KeyboradInterrupt也会被捕获，导致ctrl+c失效。
"""

class MyException(Exception):
    pass

try:
    raise MyException('throw custom my exception')
# except Exception as e:   # 捕获父类异常，其所有子类异常都在捕获范围之内
except MyException as e:
    print(e)