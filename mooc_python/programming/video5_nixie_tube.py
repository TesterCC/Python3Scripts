#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-04-16 23:55'

import turtle as t
import time


def drawGap():  # 绘制数码管间隔
    t.penup()
    t.fd(5)


def drawLine(draw):  # 绘制单段数码管
    drawGap()
    t.pendown() if draw else t.penup()  # 真值落笔，非真抬笔
    t.fd(40)
    drawGap()
    t.right(90)


def drawDigit(d):  # 根据数字绘制七段数码管
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    t.left(90)
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)

# 输出将要输出的字符
def drawDate(date):
    t.pencolor("red")
    for i in date:
        if i == '-':
            t.write('年', font=("Arial", 18, "normal"))
            t.pencolor("green")
            t.fd(40)
        elif i == '=':
            t.write('月', font=("Arial", 18, "normal"))
            t.pencolor("blue")
            t.fd(40)
        elif i == '+':
            t.write('日', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))    # 通过eval()函数将数字变为整数


def main():
    t.setup(800, 350, 200, 200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    # print(time.strftime('%Y-%m=%d+', time.gmtime()))
    drawDate(time.strftime('%Y-%m=%d+', time.gmtime()))
    t.hideturtle()
    t.done()


main()