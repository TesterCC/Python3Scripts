# -*- coding: utf-8 -*-
# !/usr/bin/python3
# @Time    : 2022/8/28
# @Author  : SecCodeCat

import tempfile

'''
http://t.zoukankan.com/liuhui0308-p-12464003.html
https://blog.csdn.net/weixin_37926734/article/details/123563067
https://docs.python.org/zh-tw/dev/library/tempfile.html
'''

print('TemporaryFile:')
with tempfile.NamedTemporaryFile() as temp:
    temp.write(b"abcd")
    temp.seek(0)
    print(f"[D] temp file content: {temp.read()}")
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))
