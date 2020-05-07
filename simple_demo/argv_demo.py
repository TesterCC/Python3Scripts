#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-05-05 11:11'

import argparse

import urllib.request
import re
import time


"""
cd ~/simple_demo

python argv_demo.py -h
python argv_demo.py -D -v
python argv_demo.py -D -vv

"""

def get_html_a_link(target_url="https://www.postgresql.org"):

    ret = urllib.request.urlopen(target_url, timeout=15)

    data = ret.read()

    # print(data)  # bytes

    content = data.decode('utf-8')

    # print(content,type(content))

    """
    正则表达式：

    href+连接文字 : <a.+?href="(.+?)".*>(.+)
    单独href: <a.+?href="(.+?)".*>    # correct

    href多信息匹配：<a.*?href="(.+)".*?>(.*?)</a>
    """

    pattern = '<a.+?href="(.+?)".*>'  # python3用正则获取href

    """
    用re.search可以查找到第一个

    用re.findall可以查找到所有的
    """
    ret = re.findall(pattern, content)

    pattern_2 = '^/.*'

    new_urls = []
    for i in ret:
        if re.findall(pattern_2, i):
            ret_url = target_url + re.findall(pattern_2, i)[0]
            new_urls.append(ret_url)
        else:
            new_urls.append(i)

    # 斜杠开头的加域名
    # print(ret)
    print(new_urls)

    with open("postgrel_html_a_links.txt", "w+") as f:
        for i in new_urls:
            f.write(i + "\n")

    return new_urls


# just test argparse demo

parser = argparse.ArgumentParser()


parser.add_argument("-D","--demo", help="run a demo function to get postgresql home page a lnks", action="store_true")
parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")

args = parser.parse_args()

delta_time = 0

if args.demo:
    start_time = time.time()
    ret = get_html_a_link()
    delta_time = time.time() - start_time
    print(ret)


if args.verbose == 1:
    print("Running '{}' file.".format(__file__))  # 增加详细现实信息
elif args.verbose > 1:
    print("Running '{}' file.".format(__file__))  # 增加详细现实信息
    print("Running cost time : '{}'.".format(delta_time))  # 增加详细现实信息


