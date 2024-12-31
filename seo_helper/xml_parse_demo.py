#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-10-11 11:20'


"""
for test xml parse

https://xxx.com/sitemap-index.xml
https://xxx.com/sitemap-expo-info.xml
https://xxx.com/sitemap-expo-cat.xml
https://xxx.com/sitemap-expo-city.xml
https://xxx.com/sitemap-expo-month.xml
"""


from bs4 import BeautifulSoup as BS
import requests

SITEMAP_URL = 'https://xxx.com/sitemap.xml'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:62.0) Gecko/20100101 Firefox/61.0'
headers = {
    "User-Agent": user_agent
}

def parse_xmls(sitemap_url):
    res = requests.get(sitemap_url, headers=headers)

    # print(res.text)
    html = res.text

    xmls = BS(html,"lxml")
    xml_list = [i.text for i in xmls.find_all("loc")]
    print(xml_list)
    return xml_list

def parse_xml_url(xml_url):

    res = requests.get(xml_url, headers=headers)

    xml_html = res.text

    urls = BS(xml_html,"lxml")
    urls_list = [i.text for i in urls.find_all("loc")]
    # print(urls_list)
    # print(len(urls_list))
    return urls_list

def parse_sitemap():
    """
    parse site xml, extract site urls

    https://xxx.com/sitemap-index.xml
    https://xxx.com/sitemap-expo-info.xml
    https://xxx.com/sitemap-expo-cat.xml
    https://xxx.com/sitemap-expo-city.xml
    https://xxx.com/sitemap-expo-month.xml
    """
    xml_list = parse_xmls(SITEMAP_URL)

    all_url_list = []
    for xml_url in xml_list:
        all_url_list += parse_xml_url(xml_url)

    # print(len(all_url_list))
    # print(all_url_list)
    return all_url_list,len(all_url_list)

if __name__ == '__main__':
    push_urls, length = parse_sitemap()
    print(push_urls)
    print(length)





