#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-10-11 10:47'


import requests
from bs4 import BeautifulSoup as BS

"""
https://ziyuan.baidu.com
url push
9999/day?

simple push by xml
可以挖掘更多url去提交
"""


class PushHelper:

    def __init__(self):
        self.SITE_DOMAIN = ""
        self.SITE_TOKEN = ""

        self.BD_PUSH_URL = 'http://data.zz.baidu.com/urls?site={}&token={}'.format(self.SITE_DOMAIN, self.SITE_TOKEN)

        self.SITEMAP_URL = 'https://xxx.com/sitemap.xml'

        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:62.0) Gecko/20100101 Firefox/61.0'


        self.headers = {
            'Content-Type': "text/plain",
            'cache-control': "no-cache",
            'User-Agent': self.user_agent
        }

    def parse_xmls(self, sitemap_url):
        res = requests.get(sitemap_url, headers=self.headers)

        # print(res.text)
        html = res.text

        xmls = BS(html, "lxml")
        xml_list = [i.text for i in xmls.find_all("loc")]
        # print(xml_list)
        return xml_list

    def parse_xml_url(self, xml_url):
        res = requests.get(xml_url, headers=self.headers)

        xml_html = res.text

        urls = BS(xml_html, "lxml")
        urls_list = [i.text for i in urls.find_all("loc")]
        # print(urls_list)
        # print(len(urls_list))
        return urls_list

    def parse_sitemap(self):
        """
        parse site xml, extract site urls

        https://xxx.com/sitemap-index.xml
        https://xxx.com/sitemap-expo-info.xml
        https://xxx.com/sitemap-expo-cat.xml
        https://xxx.com/sitemap-expo-city.xml
        https://xxx.com/sitemap-expo-month.xml
        """
        xml_list = self.parse_xmls(self.SITEMAP_URL)

        print(f'xml_list:{xml_list}')
        all_url_list = []

        for xml_url in xml_list:
            all_url_list += self.parse_xml_url(xml_url)

        # print(len(all_url_list))
        # print(all_url_list)
        return all_url_list, len(all_url_list)


    def push_urls_to_bd(self, push_urls):
        # need_push_urls = ['https://xxx.com/it/', 'https://xxx.com/pe/',
        #                   'https://xxx.com/gift/']
        need_push_urls = push_urls
        data = "\n".join(need_push_urls)

        response = requests.post(self.BD_PUSH_URL, data=data, headers=self.headers)

        print(response.text)

if __name__ == '__main__':
    push_helper = PushHelper()
    need_push_urls, length = push_helper.parse_sitemap()

    print("*"*77)
    # print(need_push_urls)
    print("total url length: {}".format(length))

    def check_length(need_push_urls):
        if length > 9999:
            if len(need_push_urls[9999:]) <= 9999:
                need_push_urls = need_push_urls[9999:]
            else:
                check_length(need_push_urls)
        print("pass length check")
        return need_push_urls

    push_helper.push_urls_to_bd(need_push_urls)






