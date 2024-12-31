#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/5 10:32'

"""
Effective Python编写高质量Python代码的59个有效方法  P7
兼容Python2和Python3的的写法  (用二进制模式来开启待操作的文件)

需求：向文件中随机写入一些二进制数据
"""

import os

# 向文件中随机写入一些二进制数据
with open('./tmp/random.bin', 'wb') as f:    # ./ 相对路径   ／绝对路径
    f.write(os.urandom(10))         # 随机写入10个bytes


