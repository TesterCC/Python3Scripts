#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-10 15:43'

"""
Assert that a certain exception is raised
https://docs.pytest.org/en/latest/getting-started.html#create-your-first-test

Run in terminal:
pytest -q test_sysexit.py
"""


import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
