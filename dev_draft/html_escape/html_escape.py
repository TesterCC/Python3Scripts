#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/18 15:38'

"""
处理<script>等标签，将特殊字符转义
"""

import html

text = "<script>alert('123')</script>"

txt = html.escape(text)

print(txt)    # &lt;script&gt;alert('123')&lt;/script&gt;

