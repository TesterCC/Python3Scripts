#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/11/7 17:16'


"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320027235877860c87af5544f25a8deeb55141d60c5000
PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片
"""

import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter


# 随机字母
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色
def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色2
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

# 图片大小 240 x 60
width = 60*4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)

# 创建Draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y), fill=rndColor())

# 输出文字
for t in range(4):
    draw.text((60*t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

print("Finish generate captcha.")








