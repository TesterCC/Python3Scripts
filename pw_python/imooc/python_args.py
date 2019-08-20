#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-17 13:36'

# 3-3 常考函数

def flist(l):
    l.append(0)
    print(l)


l = []
flist(l)
flist(l)


def fstr(s):
    s += 'a'
    print(s)


s = 'hehe'
fstr(s)
fstr(s)



# [0]
# [0, 0]
# hehea
# hehea
