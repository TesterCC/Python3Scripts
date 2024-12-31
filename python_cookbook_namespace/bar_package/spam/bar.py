#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/2 10:36'

# Python CookBook 3.0   10-5 利用命名空间导入目录分散的代码

import os


print("This is bar %s " % os.getcwd())
print(os.path.abspath(__file__))
