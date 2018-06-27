#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/6/27 10:26'

"""
round() 方法返回浮点数x的四舍五入值

以下是 round() 方法的语法:

round( x [, n]  )
参数
x -- 数字表达式。
n -- 表示从小数点位数，其中 x 需要四舍五入，默认值为 0。

返回值
返回浮点数x的四舍五入值。

http://www.runoob.com/python3/python3-func-number-round.html
"""

print("round(70.23456) : ", round(70.23456))
print("round(56.659,1) : ", round(56.659, 1))
print("round(80.264, 2) : ", round(80.264, 2))
print("round(100.000056, 3) : ", round(100.000056, 3))
print("round(-100.000056, 5) : ", round(-100.000056, 5))

print("在实际使用中发现round函数并不总是如上所说的四舍五入。")
# http://www.runoob.com/w3cnote/python-round-func-note.html
"""
在python2.7的doc中，round()的最后写着，"Values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done away from 0." 
保留值将保留到离上一位更近的一端（四舍六入），如果距离两端一样远，则保留到离0远的一边。所以round(0.5)会近似到1，而round(-0.5)会近似到-1。

但是到了python3.5的doc中，文档变成了"values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done toward the even choice." 
如果距离两边一样远，会保留到偶数的一边。比如round(0.5)和round(-0.5)都会保留到0，而round(1.5)会保留到2。

除非对精确度没什么要求，否则尽量避开用round()函数。

对浮点数精度要求如果很高的话，请用decimal模块。
"""
print(round(2.355, 2))




