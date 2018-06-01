#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/1 09:45'


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def bar(self):
        print('B.bar')

