#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/16 20:13'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000
定制类
Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
一个链式调用
"""


# api = "http://api.server/user/timeline/list"


class Chain(object):
    """
    For call RESTful API 写一个链式调用
    """

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

c = Chain()
print(c.user.timeline.list)
# print(c.user.timeline.list)
# print(c.test0.test1)

# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变
