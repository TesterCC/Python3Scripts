#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/15 13:45'

"""
边界匹配
"""

import re

qq = '100001'

# 4-8
r = re.findall('\d{4,8}', qq)

print(r)
