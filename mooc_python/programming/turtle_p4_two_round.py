#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-27 21:31'

"""
https://python123.io/student/courses/688/groups/5298/problems/programmings/2170
使用turtle库，绘制一个叠边形，其中，叠边形内角为80度。
"""

import turtle as t
t.pensize(4)
for i in range(9):
    t.fd(150)
    t.left(80)    # 720/9
t.done()