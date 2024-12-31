#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/9 13:39'

# try except finally
try:
    f_read = open("c4.txt")
    print("code started")
    raise KeyError
    # raise IndexError
    f_read.close()
except KeyError as e:
    print("key error")
    f_read.close()
else:
    print("other error")
finally:
    print("finally")
    f_read.close()
