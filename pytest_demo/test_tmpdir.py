#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-10 15:47'

"""
https://docs.pytest.org/en/latest/getting-started.html#create-your-first-test
"""

def test_needsfiles(tmpdir):
    print(tmpdir)