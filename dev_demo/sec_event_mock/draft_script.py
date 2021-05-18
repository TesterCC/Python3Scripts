# coding=utf-8
"""
DATE:   2021/5/18
AUTHOR: Yanxi Li
"""

import time
import random


# 这个不用
def random_time_v2():
    a1 = (2021, 5, 16, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（2020-04-12 00：00：00）
    a2 = (2021, 5, 18, 0, 0, 0, 0, 0, 0)  # 设置结束日期时间元组（2020-04-13 00：00：00）

    start = time.mktime(a1)  # 生成开始时间戳
    print("start时间戳:", start)
    end = time.mktime(a2)  # 生成结束时间戳
    print("end时间戳:", end)

    # 随机生成10个日期字符串
    for i in range(10):
        t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
        date_touple = time.localtime(t)  # 将时间戳生成时间元组
        date_str = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
        print(date_str)


import requests
from bs4 import BeautifulSoup


def get_website_title():
    res = requests.get("http://www.sohu.com")
    # res.encoding = 'utf-8'  # 百度需要，不然乱码
    soup = BeautifulSoup(res.text, 'lxml')
    print(soup.title.text)


if __name__ == '__main__':
    get_website_title()
