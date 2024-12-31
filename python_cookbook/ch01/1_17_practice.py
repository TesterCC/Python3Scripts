#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/2 11:59'


"""
1.17  从字典中提取子集 

问题:
  你想构造一个字典,它是另外一个字典的子集。

解决方案:
  最简单的方式是使用字典推导。
"""

price = {
    'status': 1,
    'limit_people': '1',
    'property': 'VIP\xe5\xb0\x8a\xe4\xba\xab',
    'end_time': '2018-07-30 19:00',
    'begin_time': '2018-06-08 17:25',
    'original_price': 0.5,
    'price': 0.03,
    'content': 'VIP\xe5\xb0\x8a\xe4\xba\xab',
    'id': 218764, 'stock': 100
}

# method 2
need_items = {'id', 'price', 'end_time'}

new_price = {key: value for key, value in price.items() if key in need_items}

print(new_price)

