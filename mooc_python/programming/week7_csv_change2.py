#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-05 17:46'

with open("data.csv") as f:
    for line in f:
        line = line.strip("\n")
        ls = line.split(",")
        ls = ls[::-1]
        print(",".join(ls))
