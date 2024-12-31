#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/18 00:56'

"""
分组
"""

import re

a = 'PythonPythonPythonPythonPythonJS'

r = re.findall('PythonPythonPython', a)   # 最笨的匹配3个连续的Python

r2 = re.findall('(Python){3}(JS)', a)

print(r)

print(r2)
