#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '18/1/5 05:41'

"""
P51-53 1-2-1  模拟数值类型 二维向量加法和doctest  Python 3.4
"""

# API遇到abs则返回向量的模

from math import hypot


class Vector:
    """Return the Vector

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1+v2
    Vector(4, 5)
    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0
    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# start doc test
if __name__ == "__main__":
    import doctest
    doctest.testmod()