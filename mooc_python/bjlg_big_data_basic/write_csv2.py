#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-24 00:23'

import csv

fieldnames = ['a','b','c']

data = [{'a':1, 'b':2, 'c':3},{'a':4, 'b':5, 'c':6},{'a':7, 'b':8, 'c':9}]

with open('data2.csv','w',newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)