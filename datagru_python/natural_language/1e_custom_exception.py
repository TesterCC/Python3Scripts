#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/9 17:37'

"""
第一周 Python基础 week01e
"""


# 自定义异常
class Networkerror(RuntimeError):
    def __init__(self, args):
        self.args = args

try:
    raise Networkerror("Bad hostname")
except Networkerror as e:    # Python 3.5 syntax,  Python 2.7 -> except Networkerorr,e:
    print(e.args)