#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/20 15:52'

"""
https://note.youdao.com/web/#/file/WEB452c52824d7cff1f9cf37e6df0bf83e8/note/WEBd1101bd05f386cea6388362d6fc11a63/
xml和excel会遇到
内容中含有低位非打印字符，处理方法是对其进行过滤
"""

import re

company = u'\x08TestCompany'

# method 1

s1 = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f]').sub('', company)  # 不推荐，不好识别

print(s1)

# method 2

s2 = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", company)  # 推荐，优雅易理解

print(s2)
