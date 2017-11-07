#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/7 16:49'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320027235877860c87af5544f25a8deeb55141d60c5000
操作图像
"""

from PIL import Image
from PIL import ImageFilter

# 打开一个jpg图像文件，注意是当前路径
im = Image.open('test.jpeg')

# 获得图像尺寸
w, h = im.size
print('Original image size: %sx%s' % (w, h))

# 缩放到50%
im.thumbnail((w//2, h//2))    # thumbnail((200,300))
print('Resize image to: %sx%s' % (w//2, h//2))

# 把缩放后的图像用png格式保存
im.save('thumbnail.jpeg', 'png')

# 模糊效果
# 打开一个png图像文件，注意是当前路径
im2 = Image.open('thumbnail.jpeg')

# 应用模糊滤镜
im3 = im2.filter(ImageFilter.BLUR)
im3.save('blur.jpeg', 'png')
