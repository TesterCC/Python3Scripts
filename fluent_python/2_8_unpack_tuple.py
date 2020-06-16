#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-06-17 16:00'

"""
2.3.3 嵌套元组拆包
"""

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689, 139.691)),
    ('Delhi NCR', 'IN', 21.935, (28.6138, 77.208889)),
    ('Mexico City', 'MX', 20.104, (19.433, -99.1333333)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.63583))
]

# 打印表头
print('{:15}| {:^9}| {:^9}'.format('', 'lat.', 'long.'))

# 打印列内容
fmt = '{:15}|{:9.4f}|{:9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
