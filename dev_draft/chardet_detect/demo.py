#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/26 09:33'

import chardet

"""
REF:
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001510905171877ca6fdf08614e446e835ea5d9bce75cf5000
"""

bytes_str = b'\xE7\xB1z\xAE\xE0\xF5\xDE\x8D\xB6O\xD6\x00\x00'

response = chardet.detect(bytes_str)
# {'encoding': 'Windows-1253', 'confidence': 0.6359051371978052, 'language': 'Greek'}
# 检测出的编码是Windows-1253，注意到还有个confidence字段，表示检测的概率是0.6359051371978052（即63.59051%）。 说明这个监测结果并不一定是对的

print(response)


bs = b'\xf9P\xb3\xb7\xa2\xee\x05\x9e\xa2\xaa\x9dD\x92\xbb\x0c\x8bx\x81\x12\x1a\t\xa7\xe0\x91\x88'

response = chardet.detect(bs)

print(response)

