#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/24 09:11'

"""
python-qrcode是个用来生成二维码图片的第三方模块，依赖于 PIL 模块和 qrcode 库。

首先，我们要安装三个模块，qrcode，image，PIL。

pip install qrcode

pip install image

pip install pillow

ref:
https://www.cnblogs.com/sfnz/p/5457862.html
http://pythonware.com/products/pil/

version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。
error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
ROR_CORRECT_H：大约30%或更少的错误能被纠正。
box_size：控制二维码中每个小格子包含的像素数。
border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）。
img.save：是将生成二维码图片保存到哪里。
"""

import os
import datetime

from PIL import Image
import qrcode

# 带有logo图案的二维码
qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
qr.add_data("https://aictf.com")

qr.make(fit=True)

img = qr.make_image()
img = img.convert("RGBA")

icon = Image.open(os.getcwd() + "/favicon_wx.png")

img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)

icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
icon = icon.convert("RGBA")
img.paste(icon, (w, h), icon)

# save qrcode
filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

img.save('{}/generate_qrcode/{}.png'.format(os.getcwd(), filename), quality=100)

img.show()
