#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/10 00:12'

from collections import namedtuple

"""
https://docs.python.org/3.6/library/collections.html
namedtuple()这是个工厂方法,生成有命名字段的tuple子类(译注: tuple中的元素可以用名字的方式来访问)
namedtuple是继承自tuple的子类。namedtuple创建一个和tuple类似的对象，而且对象拥有可访问的属性。
tuple元组的item只能通过index访问，collections模块的namedtuple子类不仅可以使用item的index访问item，还可以通过item的name进行访问。

https://blog.csdn.net/helei001/article/details/52692128
"""

print("------------Basic API test-----------")
tsum = namedtuple('Tsum', ['x', 'y', 'z'])
ts = tsum(10, 20, 30)
print("x={0}, y={1}, z={2}".format(ts.x, ts.y, ts.z))

ts = tsum._make([100, 200, 300])  # _make  classmethod
print(ts.x, ts.y, ts.z)

ts = ts._replace(x=700)  # _replace  classmethod# _make  classmethod
print(ts.x, ts.y, ts.z)

print("------------example test-----------")

websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊'),
    ('Tencent', 'https://www.tencent.com', u'马化腾'),
]

Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
    website = Website._make(website)
    print(website)
