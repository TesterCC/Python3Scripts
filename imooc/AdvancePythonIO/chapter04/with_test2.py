#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/9 13:39'

# try except finally
try:
    print("code started")
    raise IndexError
except KeyError as e:
    print("key error")
else:
    print("other error")
finally:
    print("finally")
