#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-19 13:07'

"""
issue:
https://stackoverflow.com/questions/36674083/why-is-it-possible-to-replace-sometimes-set-with

set([1,2,3])
should change to:
{1,2,3}

PyCharm Suggest: "Function call can be replaced with set literal" 

Detail explain: 
https://www.cnblogs.com/kaituorensheng/p/6139573.html

set literal is better in performance testing
"""

import timeit

print(set([1, 2, 3]))  # need to change
print({1, 2, 3})
print(timeit.timeit('a = set([1, 2, 3])'))
print(timeit.timeit('a = {1,2,3}'))   # absolutely better in Python3
