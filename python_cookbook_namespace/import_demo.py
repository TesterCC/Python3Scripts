#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/2 11:28'

# Python CookBook 3.0   10-5 利用命名空间导入目录分散的代码   直接运行单个import_demo.py

import sys
sys.path.extend(['foo_package', 'bar_package'])

import spam.bar
import spam.foo

