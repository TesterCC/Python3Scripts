#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-22 06:50'

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import string, os, time

"""
ref：
https://www.bilibili.com/video/BV11E411w7ec

用ffmpeg分解视频
ffmpeg -i original_videos vName.mp4 -s 320*180 ./pictures/vName/out%d.png
"""

ascii_chars = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def showImg():
    img = Image.open('./cat7.png')
    img = np.array(img)[:,:,0]

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            code = img[i][j]
            print(ascii_chars[int(code/100)],end='')
            print(ascii_chars[int(code/100)],end='')
        print('')

showImg()

