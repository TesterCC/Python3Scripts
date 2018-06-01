#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/1 09:45'

from .a import A


class B(A):
    def bar(self):
        print('B.bar')
