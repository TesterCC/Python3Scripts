#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/9 15:01'


import unittest
import os
import time
from pathlib import Path

"""
issue:
SystemError: Parent module '' not loaded, cannot perform relative import

resolve:
直接将CustomTestRobot作为跟目录打开

"""

LOG_PATH = os.path.normpath(os.path.dirname(__file__) + time.strftime("/logs/%Y-%m-%d.log", time.localtime()))
print("日志存放路径: ", LOG_PATH)

if __name__ == "__main__":

    print("Launch >>>> CustomTestRobot start...")

    print("关注公众号: fullstackpentest")

    if not os.path.exists(LOG_PATH):
        print("创建日志文件...")
        Path(LOG_PATH).touch()

    print("加载测试用例...")
    case_dir = os.path.normpath(os.path.dirname(__file__) + "/testcase")
    print(case_dir)

    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
    print(discover)

    print("执行测试用来...")
    runner = unittest.TextTestRunner()
    runner.run(discover)
