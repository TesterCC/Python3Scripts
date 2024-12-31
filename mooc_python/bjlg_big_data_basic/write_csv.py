#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-24 00:23'

import csv

keys = ['a','b','c','d']

data = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

with open('data.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(keys)
    #writer.writerows(data)   # 一次写入多个
    for row in data:
        writer.writerow(row)