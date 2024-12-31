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
"""

def showImg(i,j):
    img = Image.open('./cat.jpeg')
    img = np.array(img)
    # print(img)
    print(img.shape)
    img[:,:,i] = img[:,:,i]*0
    img[:,:,j] = img[:,:,j]*0
    print(img[:,:,0])  # 数组的每个值都代表像素点的深浅
    plt.imshow(img)
    plt.show()

showImg(1,2)  # red
showImg(0,2)  # green
showImg(0,1)  # blue