#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/3 10:49'

"""
use Wand for pdf to images
http://docs.wand-py.org/en/latest/

Install:
pip install Wand -i https://pypi.douban.com/simple/

install other lib which needed

ref(recommend):
https://blog.csdn.net/wwj_748/article/details/78135879?utm_source=tuicool&utm_medium=referral

"""

import os
import time
from wand.image import Image
from PIL import Image as Image2

import requests


# pdf_urls = ['', '']     # get untrans pdf url from list

base_dir = os.getcwd()
print(base_dir)

ZIP_PATH = base_dir + '/zip'
PDF_PATH = base_dir + '/pdf'
LOG_PATH = base_dir + '/log'

print(ZIP_PATH)
print(PDF_PATH)
print(LOG_PATH)



def download_pdf(pdf_urls):
    pass


def convert_pdf_to_jpg(filename):
    with Image(filename=filename) as img:
        print('total pages = ', len(img.sequence))

        with img.convert('png') as converted:
            converted.save(filename='image/page.png')   # generate pic name: page-0.jpeg page-1.jpeg, same name covered directly


# 图片压缩批处理
def compress_image(srcPath, dstPath):
    for filename in os.listdir(srcPath):
        # 如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
                os.makedirs(dstPath)

        # 拼接完整的文件或文件夹路径
        srcFile = os.path.join(srcPath, filename)
        dstFile = os.path.join(dstPath, filename)

        # 如果是文件就处理
        if os.path.isfile(srcFile):
            # 打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
            im = Image2.open(srcFile).convert('P')
            im.save(dstFile)
            print(dstFile+" compressed succeeded")
        os.remove(srcFile)
        # 如果是文件夹就递归
        if os.path.isdir(srcFile):
            compress_image(srcFile, dstFile)


if __name__ == '__main__':
    start_time = time.time()
    convert_pdf_to_jpg("issue.pdf")
    delta_time = time.time() - start_time
    print("Cost time: {}".format(delta_time))    # 6 pages, Cost time: 5.823540925979614
