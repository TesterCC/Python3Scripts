#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-12 10:51'

"""
单行动态刷新：
-- 刷新的本质：用后打印字符覆盖之前的字符
-- 不能换行： print()需要被控制
-- 要能退回： 打印后光标退回到之前的未知   刷新的关键是\r  默认将指针返回到最开始后输出（在原位置再次输出）
"""

import time

for i in range(101):
    print("\r{:3}%".format(i),end="")     # 单行动态刷新百分比
    time.sleep(0.1)
    # time.sleep(0.25)
