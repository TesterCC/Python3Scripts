#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/6/16 12:39'

"""
2-9 定义和使用具名元组
2-10 具名元组的属性和方法
"""

from collections import namedtuple

# 创建一个具名元组需要两个参数，一个类名，一个是类的各个字段的名字
City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139, 691667))

print(tokyo)
print(tokyo.coordinates)
print(tokyo.population)

print(City._fields)  # 包含这个类所有字段名称的元组

LatLong = namedtuple('LatLong', 'lat long')

delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)  # make()接受一个可迭代对象来生成这个类的一个实例，作用和City(*delhi_data)是一样的

print(delhi._asdict())  # 把具名元组以OrderedDict的形式返回

for key,value in delhi._asdict().items():
    print(key + ":" , value)