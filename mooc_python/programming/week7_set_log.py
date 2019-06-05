#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-05 17:49'

with open("latex.log") as f:
    ls = f.readlines()
    s = set(ls)
    print("共{}独特行".format(len(s)))