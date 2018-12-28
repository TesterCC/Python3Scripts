#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2018-12-28 14:55'

"""
https://docs.pytest.org/en/latest/

Detail Doc:
https://docs.pytest.org/en/latest/contents.html#toc
"""

def inc(x):
    return x + 1


def test_error_answer():
    assert inc(3) == 5


def test_correct_answer():
    assert inc(3) == 4

"""
To execute it:

$ pytest
"""

