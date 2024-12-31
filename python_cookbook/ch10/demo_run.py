#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/1 10:21'

"""
Python Cookbook 第三版 P374  10.4 将模块分割成多个文件
"""

import mymodule    # 虽然pycharm导入要报错，但实际能在命令行下正常运行

a = mymodule.A()
a.spam()

b = mymodule.B()
b.spam()
b.bar()

