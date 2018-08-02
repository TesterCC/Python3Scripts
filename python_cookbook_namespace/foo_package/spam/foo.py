#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/2 10:37'


# Python CookBook 3.0   10-5 利用命名空间导入目录分散的代码
# 两个不同的包的spam目录被合并到一起,你可以导入 bar_package 和 foo_package ,并且它们能够工作。

import os

print("This is foo %s " % os.getcwd())
print(os.path.abspath(__file__))
