#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-24 00:26'

import csv

with open('data.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)