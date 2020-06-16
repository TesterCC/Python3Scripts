#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/16 12:27'

"""
2-11 对 对象 进行切片
"""

invoice = """

1909  Pimoroni PiBrealla            $17.50        $52.50
1489  6mm Tactile Switch X 20        $4.95         $9.90
"""

SKU = slice(0, 6)

DESCRIPTION = slice(6, 34)
UNIT_PRICE = slice(34,50)
ITEM_TOTAL = slice(50, None)

line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])


