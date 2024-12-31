#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-25 15:30'


class Base(object):
    def hello(self):
        print('hello')

class C(Base):
    def hello(self):
        # python2
        return super(C,self).hello()

c = C()
c.hello()


class C2(Base):
    def hello(self):
        # python3
        return super().hello()

c2 = C2()
c2.hello()