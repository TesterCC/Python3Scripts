#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-10-11 10:47'

import datetime
import json
import requests
from bs4 import BeautifulSoup as BS

"""
auto push urls to baidu
"""


class PushHelper:

    def __init__(self):
        self.SITE_DOMAIN = "https://expo.huodongjia.com"
        self.SITE_TOKEN = "F9o2j3CZvu4CwWRz"

        self.BD_PUSH_URL = 'http://data.zz.baidu.com/urls?site={}&token={}'.format(self.SITE_DOMAIN, self.SITE_TOKEN)

        self.SITEMAP_URL = 'https://expo.huodongjia.com/sitemap.xml'

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

        https://expo.huodongjia.com/sitemap-index.xml
        https://expo.huodongjia.com/sitemap-expo-info.xml
        https://expo.huodongjia.com/sitemap-expo-cat.xml
        https://expo.huodongjia.com/sitemap-expo-city.xml
        https://expo.huodongjia.com/sitemap-expo-month.xml
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

        response = requests.post(self.BD_PUSH_URL, data=data, headers=self.headers)

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

        # print(push_urls_list)

        for urls in push_urls_list:
            #print(urls)
            ret = push_helper.push_urls_to_bd(urls[:bd_push_max])
            print(ret)
            if ret < bd_push_max:
                break

        print(f"{datetime.datetime.now()} -- Bundle push to BD finished!!!")


if __name__ == '__main__':
    push_helper = PushHelper()
    need_push_urls, length = push_helper.parse_sitemap()

    print("*"*77)
    # print(need_push_urls)
    print(datetime.datetime.now())
    print("total url length: {}".format(length))

    push_helper.check2send(need_push_urls)








