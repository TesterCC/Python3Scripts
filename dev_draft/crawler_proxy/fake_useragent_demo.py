#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/8 20:55'

"""
https://pypi.org/project/fake-useragent/
"""

from fake_useragent import UserAgent

ua = UserAgent()

print("Radom UA:\n{}".format(ua.random))
print(type(ua.random))
print("")
print("IE UA:\n{}".format(ua.ie))
print("Chrome UA:\n{}".format(ua.chrome))
print("Firefox UA:\n{}".format(ua.firefox))
print("Firefox UA:\n{}".format(ua.firefox))