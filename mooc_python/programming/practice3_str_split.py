#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-12 15:21'

"""
字符串分段组合

描述:
获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。

期望输入：
Alice-Bob-Charis-David-Eric-Flurry

期望输出：
Alice+Flurry
"""

s = input()

print("{}+{}".format(s.split("-")[0],s.split("-")[-1]))