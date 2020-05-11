#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-10-11 10:47'

import datetime
import json
import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse

# 注意定义logging
import logging
logging.basicConfig(level=logging.INFO,
                    # format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt = '%Y-%m-%d  %H:%M:%S %a'    #注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                    )
"""
auto push urls to baidu
未完成
"""

# TODO 先把python argparse文档学网，然后把这个脚本做成seo小工具，解析目标网站sitemap.xml然后上传到bdzz
# 1.脚本稳定测试
# 2.命令行参数设置和实现
# 3.打包
# 4.安装测试
# 5.文档说明

class PushHelper:

    def __init__(self, input_sitemap_url:str, site_token:str):

        urlparse_info = urlparse(input_sitemap_url)
        # print(urlparse_info)

        self.SITE_DOMAIN = urlparse_info.netloc
        self.SITE_TOKEN = site_token  # 百度站长平台获取

        self.PUSH_URL = 'http://data.zz.baidu.com/urls?site={}&token={}'.format(self.SITE_DOMAIN, self.SITE_TOKEN)

        self.SITEMAP_URL = input_sitemap_url

        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:62.0) Gecko/20100101 Firefox/61.0'


        self.headers = {
            'Content-Type': "text/plain",
            'cache-control': "no-cache",
            'User-Agent': self.user_agent
        }

    def parse_xmls(self, sitemap_url):
        res = requests.get(sitemap_url, headers=self.headers)


        html = res.text

        xmls = BS(html, "lxml")
        xml_list = [i.text for i in xmls.find_all("loc")]

        return xml_list

    def parse_xml_url(self, xml_url):
        res = requests.get(xml_url, headers=self.headers)

        xml_html = res.text

        urls = BS(xml_html, "lxml")
        urls_list = [i.text for i in urls.find_all("loc")]

        return urls_list

    def parse_sitemap(self):
        """
        parse site xml, extract site urls

        https://xxx.com/sitemap-index.xml
        https://xxx.com/sitemap-city.xml
        https://xxx.com/sitemap-month.xml
        """
        xml_list = self.parse_xmls(self.SITEMAP_URL)

        print(f'xml_list:{xml_list}')
        all_url_list = []

        for xml_url in xml_list:
            all_url_list += self.parse_xml_url(xml_url)

        return all_url_list, len(all_url_list)


    def push_urls_to_bd(self, push_urls):
        need_push_urls = push_urls
        data = "\n".join(need_push_urls)

        try:
            response = requests.post(self.PUSH_URL, data=data, headers=self.headers, timeout=7)
        except RuntimeError as err:
            print("Please check post data!!!\n")

        print(response.text)   # str
        # print(response.content)  # bytes
        # print(type(json.loads(response.text)))   # dict
        remain_count = json.loads(response.text).get('remain', '')
        return remain_count


    def check2send(self, need_push_urls, bd_push_max=2000):
        """
        :param need_push_urls: List
        :param bd_push_max: 百度允许的最大单次url推送数量
        :return:
        """
        need_push_urls.reverse()
        push_urls_list = [need_push_urls[i:i + bd_push_max] for i in range(0, len(need_push_urls), bd_push_max)]

        print("[+] Debug info: ",push_urls_list)

        for urls in push_urls_list:
            # print(urls[:bd_push_max])
            ret = push_helper.push_urls_to_bd(urls[:bd_push_max])   # 如果超过了会报错
            print(ret)
            if ret < bd_push_max:
                break

        print(f"{datetime.datetime.now()} -- Bundle push to BD finished!!!")


if __name__ == '__main__':

    push_helper = PushHelper("https://xxx.com/sitemap.xml","xxxxxxxxx")
    need_push_urls, length = push_helper.parse_sitemap()

    print("*"*77)
    # print(need_push_urls)
    logging.info(datetime.datetime.now())
    logging.info("total url length: {}".format(length))

    push_helper.check2send(need_push_urls)








