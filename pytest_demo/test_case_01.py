#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-10 15:36'


import pytest

class TestClass(object):

    def test_one(self):
        x = 'this'
        assert  'i' in x

    def test_two(self):
        x = 'hello'
        assert not hasattr(x, 'check')