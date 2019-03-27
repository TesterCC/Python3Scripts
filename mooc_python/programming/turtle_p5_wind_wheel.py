#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-27 22:16'

"""
https://python123.io/student/courses/688/groups/5298/problems/programmings/12419
使用turtle库，绘制一个风轮效果，其中，每个风轮内角为45度，风轮边长150像素。
"""

import turtle as t

t.pensize(2)
for i in range(4):
    t.seth(90 * i)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0, 0)

t.done()
