#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/9/6 14:16'


import html

"""
逃逸字符也叫转义字符
如："\n"表示换行，"\r"表示回车
"""

escape_str = '<p>&lt;spam&gt;</p>'

unescape_str = '<item size="large" quantity="6">Testcase</item>'

# 变成非转义
es2unes = html.unescape(escape_str)
print(es2unes)

# 变成转义字符
unes2es = html.escape(unescape_str)
print(unes2es)