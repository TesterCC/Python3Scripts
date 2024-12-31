# coding=utf-8
"""
DATE:   2021/9/14
AUTHOR: TesterCC
"""

import re

reg = re.compile(r'[^\u4e00-\u9fcf]+好难[^\u4e00-\u9fcf]+')

testsuite = ["正则好难","好难呀","什么？好难？"]

for t in testsuite:
    print(reg.findall(t))

