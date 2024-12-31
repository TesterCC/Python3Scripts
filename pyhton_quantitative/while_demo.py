#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/15 17:51'

"""
Python与量化投资从基础到实战  P34
"""

from time import sleep
import random


# a = True
a = False

while a:
    print("test while: {}".format(random.random()))
    sleep(1)
else:
    print("Test while False")

# while a=True, need to end by keyborad