#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-01-09 00:23'

import xlrd

workbook = xlrd.open_workbook(r'sponsor.xls')

print(workbook.sheet_names())

# 获取第一个sheet的name
sheet = workbook.sheet_names()[0]

print(sheet)

sheet_obj = workbook.sheet_by_name(sheet)

row1 = sheet_obj.row_values(1)   # 获取行
print(row1)

print("-"*70)
black_list_sponsor = sheet_obj.col_values(0)   # 获取列

print(type(black_list_sponsor))
print(black_list_sponsor)