#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/20 23:48'

import re

"""
re.match() 能够匹配出以xxx开头的字符串
"""

result = re.match("fullstack", "fullstackpentest.com")

print(result.group())