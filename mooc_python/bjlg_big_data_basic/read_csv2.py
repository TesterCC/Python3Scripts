#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-24 00:26'

import csv


data = []

with open('data2.csv','r') as file:
    reader = csv.DictReader(file)
    field_names=reader.fieldnames
    print(field_names)

    for row in reader:
        data.append(dict(row))
    print(data)