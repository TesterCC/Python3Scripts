#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-09-24 14:15'


import os
import sys
from bs4 import BeautifulSoup as BS
import requests

"""
hexo 博客专用，向百度站长平台提交所有网址
本脚本必须放在hexo博客的根目录下执行！需要已安装生成百度站点地图的插件。
百度站长平台提交链接：http://zhanzhang.baidu.com/linksubmit/index
主动推送：最为快速的提交方式，推荐您将站点当天新产出链接立即通过此方式推送给百度，以保证新链接可以及时被百度收录。
从中找到自己的接口调用地址
python环境：
pip install beautifulsoup4
pip install requests
xcode-select --install  
pip install lxml 
"""

# 写你自己的, 在blog根目录下执行 workon python3demo

YOUR_DOMAIN = ''
YOUR_PUSH_TOKEN  = ''

YOUR_BD_PUSH_URL = 'http://data.zz.baidu.com/urls?site={}&token={}'.format(YOUR_DOMAIN,YOUR_PUSH_TOKEN)

baidu_sitemap = os.path.join(sys.path[0], 'public', 'baidusitemap.xml')
google_sitemap = os.path.join(sys.path[0], 'public', 'sitemap.xml')
sitemap = [baidu_sitemap, google_sitemap]
assert (os.path.exists(baidu_sitemap) or os.path.exists(
    google_sitemap)), "没找到任何网站地图，请检查！"
# 从站点地图中读取网址列表
def getUrls():
    urls = []
    for _ in sitemap:
        if os.path.exists(_):
            with open(_, "r") as f:
                xml = f.read()
        soup = BS(xml, "xml")
        tags = soup.find_all("loc")
        urls += [x.string for x in tags]
        if _ == baidu_sitemap:
            tags = soup.find_all("breadCrumb", url=True)
            urls += [x["url"] for x in tags]
    return urls

# POST提交网址列表
def postUrls(urls):
    urls = set(urls)  # 先去重
    print("一共提取出 %s 个网址" % len(urls))
    print(urls)
    data = "\n".join(urls)
    return requests.post(YOUR_BD_PUSH_URL, data=data).text
if __name__ == '__main__':
    urls = getUrls()
    result = postUrls(urls)
    print("提交结果：")
    print(result)
#    msvcrt.getch()