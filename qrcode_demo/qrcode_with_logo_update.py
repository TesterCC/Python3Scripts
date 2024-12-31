#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/24 10:27'

"""
Python3生成带logo的二维码
https://blog.csdn.net/u013772433/article/details/69523438

最近有个需求：批量生成带Logo的二维码
网上的资源直接加Logo特别丑
"""

import os

from PIL import Image
import qrcode


def create_qrcode(url, filename):
    qr = qrcode.QRCode(
        # 设置二维码矩阵大小
        version=1,
        # 设置容错率为最高
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)    # your target url
    qr.make(fit=True)

    img = qr.make_image()
    # 设置二维码为彩色
    img = img.convert("RGBA")
    icon = Image.open(os.getcwd() + "/favicon_wx.png")
    w, h = img.size
    factor = 4
    size_w = int(w / factor)
    size_h = int(h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((w - icon_w) / 2)
    h = int((h - icon_h) / 2)
    icon = icon.convert("RGBA")
    newimg = Image.new("RGBA", (icon_w + 8, icon_h + 8), (255, 255, 255))
    img.paste(newimg, (w - 4, h - 4), newimg)

    img.paste(icon, (w, h), icon)
    img.save('{}/generate_qrcode/{}.png'.format(os.getcwd(), filename + '.png'), quality=100)

    img.show()


if __name__ == '__main__':
    target_url = "https://aictf.com"
    filename = "qr_with_logo2"
    create_qrcode(target_url, filename)
