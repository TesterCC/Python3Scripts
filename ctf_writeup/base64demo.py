#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '18/1/8 23:07'


"""
百度杯

题目:贝丝贝丝，我爱你（大声循环2的6次方ing）

ZmxhZ3tpY3FlZHVfZ29nb2dvX2Jhc2U2NH0=

Fast method, run in terminal:
MacOS:
echo 'ZmxhZ3tpY3FlZHVfZ29nb2dvX2Jhc2U2NH0=' | base64 -D

Linux Ubuntu:
echo 'ZmxhZ3tpY3FlZHVfZ29nb2dvX2Jhc2U2NH0=' | base64 -d
flag{icqedu_gogogo_base64}
"""

import base64
s = 'ZmxhZ3tpY3FlZHVfZ29nb2dvX2Jhc2U2NH0='
print(base64.b64decode(s))

