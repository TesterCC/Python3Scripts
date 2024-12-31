#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/2 13:33'

"""
20-生成器-4-完成多任务
类似协程
"""


def test1():
    while True:
        print("--1--")
        yield None


def test2():
    while True:
        print("--2--")
        yield None


t1 = test1()
t2 = test2()

while True:
    t1.__next__()
    t2.__next__()
