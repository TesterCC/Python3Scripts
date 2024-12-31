#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/8 20:40'

"""
代码绘制一只小猪佩奇---python篇
https://www.jianshu.com/p/3af5e7ce1d58

pip install pillow

原理简述：
就是获取图上每一点的RGB值，然后根据这三种值确定这一点采用什么字符，其实根据RGB来确定的交灰值，
所以可以将图片转化成灰度图片，来直接获取每一点的灰度，或者通过灰度的转换公式来使得RGB三值转化成灰度当然了，
深度的原理我也不太懂，这里有链接，有兴趣的可以看一下大神们的解释

将RGB值转换为灰度值的简单算法  
http://www.cnblogs.com/GarfieldTom/archive/2012/12/21/2828506.html
"""

from PIL import Image

# 要索引的字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# ascii_char = list("$@B%8&WM#*oabcdefghikybdpqwmMABCDEFGWZO0QLICJUYXzcvunxrwjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)
img = Image.open('t_img2.jpg')  # 读取图像文件
(width, height) = img.size
# img = img.resize((int(width * 0.5), int(height * 0.2)))  # 对图像进行一定缩小,图片的大小可以根据上传图片的大小来按需调节，
img = img.resize((int(width * 0.25), int(height * 0.1)))  # 对图像进行一定缩小,图片的大小可以根据上传图片的大小来按需调节，
print(img.size)


def convert(img):
    img = img.convert("L")  # 转为灰度图像
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            gray = img.getpixel((j, i))  # 获取每个坐标像素点的灰度
            unit = 256.0 / length
            txt += ascii_char[int(gray / unit)]  # 获取对应坐标的字符值
        txt += '\n'
    return txt


def convert1(img):
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            r, g, b = img.getpixel((j, i))  # 获取每个坐标像素点的rgb值
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)  # 通过灰度转换公式获取灰度
            unit = (256.0 + 1) / length
            txt += ascii_char[int(gray / unit)]  # 获取对应坐标的字符值
        txt += '\n'
    return txt


txt = convert(img)

import datetime
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')

f = open("convert_{}.txt".format(current_time), "w")
f.write(txt)  # 存储到文件中
f.close()
