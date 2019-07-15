#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-15 11:32'

"""
lesson 4

线性结构：
1.内存连续
2.下标访问


cd ~/Python3Demo/pw_python/algorithm
pytest array_and_list.py
"""

from array import array

arr = array('u', 'asdf')

print(arr)

print(arr[0])
print(arr[1])


class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1

    a.clear()
    assert a[0] is None
