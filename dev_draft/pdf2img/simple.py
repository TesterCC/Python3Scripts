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

import time
from wand.image import Image

import requests


# pdf_urls = ['', '']     # get untrans pdf url from list



def download_pdf(pdf_urls):
    pass


def convert_pdf_to_jpg(filename):
    with Image(filename=filename) as img:
        print('total pages = ', len(img.sequence))

        with img.convert('jpeg') as converted:
            converted.save(filename='image/page.jpeg')   # generate pic name: page-0.jpeg page-1.jpeg, same name covered directly


if __name__ == '__main__':
    start_time = time.time()
    convert_pdf_to_jpg("test.pdf")
    delta_time = time.time() - start_time
    print("Cost time: {}".format(delta_time))    # 6 pages, Cost time: 5.823540925979614
