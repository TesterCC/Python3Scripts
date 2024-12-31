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
"""

import os
import datetime
import qrcode


img = qrcode.make('https://aictf.com')

filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

img.save('{}/generate_qrcode/{}.jpg'.format(os.getcwd(), filename))

img.show()
