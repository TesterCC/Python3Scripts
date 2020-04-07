#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-04-07 12:02'

"""
ref: 
https://www.cnblogs.com/MrRead/p/7656800.html
https://www.cnblogs.com/chenshengkai/p/11318387.html

Mac环境配置：
brew install tesseract    完成安装后可运行 tesseract --version 检查是否安装成功
pip install pytesseract -i https://pypi.douban.com/simple/ 
pip install pillow -i https://pypi.douban.com/simple/ 
"""

from PIL import Image

import pytesseract

image = Image.open('./img/code2.png')

img_text = pytesseract.image_to_string(image)

print(img_text)