#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-28 14:55'

"""
https://docs.pytest.org/en/latest/

Detail Doc:
https://docs.pytest.org/en/latest/contents.html#toc

To execute it:

$ pytest
"""

def inc(x):
    return x + 1

def sub(x,y):
    return x - y


# def test_error_answer():
#     assert inc(3) == 5


def test_correct_answer():
    assert inc(3) == 4


def test_sub_answer():
    assert sub(3,-1) == 4


