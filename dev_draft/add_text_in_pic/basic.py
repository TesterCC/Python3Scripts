#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-15 17:38'

from PIL import Image,ImageFont,ImageDraw


def gen_img(size=None):
    if size is None:
        size = 400
        # 生成大小为400x400RGBA是四通道图像，RGB表示R，G，B三通道，A表示Alpha的色彩空間
    image = Image.new(mode='RGBA', size=(640, 400), color=(255, 55, 55))
    # ImageDraw.Draw 简单平面绘图
    draw_table = ImageDraw.Draw(im=image)
    # 直接显示图片
    image.show()


def pic_open(filepath):
    # 图片打开与显示
    image = Image.open(filepath)
    return image


def get_size(image):
    # 获取图像的宽和高
    width, height = image.size
    return width, height


def pic_text(filepath, size, text, setFont, fillColor, filename, direction=None):
    print(filepath, size, text, setFont, fillColor)
    # 打开图片
    image = pic_open(filepath)
    # 新建绘图对象
    draw = ImageDraw.Draw(image)
    # 显示图片
    image.show()
    draw.text((40, 40), text, font=setFont, fill=fillColor, direction=None)
    image.show()
    # 保存
    pic_save(image, filename)


def pic_save(image, filename):
    # 保存
    image.save(filename)


if __name__ == "__main__":
    size = None
    # gen_img()

    # ** ImageFont模块**
    # 选择文字字体和大小
    setFont = ImageFont.truetype('/Users/TesterCC/Desktop/hdj_new_feature/SourceHanSansCN-Bold.otf', 20)
    # 设置文字颜色
    fillColor = "#FFFFFF"  # 蓝色
    text = "兔子等着瞧"
    size = (40, 40)
    filepath = "/Users/TesterCC/Development/python_workspace/Python3Demo/dev_draft/add_text_in_pic/11.jpg"
    filename = "/Users/TesterCC/Development/python_workspace/Python3Demo/dev_draft/add_text_in_pic/12.jpg"

    # 打开图片
    image = pic_open(filepath)
    # 添加文字
    pic_text(filepath, size, text, setFont, fillColor, filename, direction=None)

    # filepath = "/Users/TesterCC/Development/python_workspace/Python3Demo/dev_draft/add_text_in_pic/11.jpg"
    # image = pic_open(filepath)
    # width, height = get_size(image)
    # print(width)   # 320-480
    # print(height)  # 200-300