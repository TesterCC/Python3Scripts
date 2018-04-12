#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/10 09:32'

from time import sleep
import logging
import json
import re

import requests
from bs4 import BeautifulSoup


class HWebCrawler(object):
    """
    for get hdj event json data
    """

    def __init__(self):

        username = "15281005385"  # [18702895635, 15281005385, 18683715921, 18782291154, 18108061758]
        password = ""

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Host': 'www.huodongjia.com'
        }

        # parser_json_url = "https://www.huodongjia.com/event-1322992792.html?json=1"
        domain_url = "https://www.huodongjia.com/"

        username_related = {
            '18702895635': '',           # 全部
            '15281005385': 'medical',    # 医疗医学
            '18683715921': 'it',    # IT互联网
            '18782291154': 'energy',    # 能源化工
            '18108061758': 'finance',    # 金融财经
        }

        cat = username_related.get(username, '')
        cat_url = "https://www.huodongjia.com/{0}".format(cat)
        print(cat_url)

        self.headers = headers
        self.username = username
        self.password = password
        self.article_title = ''
        self.content_message = ''
        self.cat_url = cat_url
        # self.session = requests.session()
        self.domain_url = domain_url

        self.published_event_id = []

    def get_event_url(self):
        # 获取网页内容
        r = requests.get(self.cat_url, headers=self.headers, timeout=10)
        data = r.text

        # 利用正则查找所有event连接
        # 1.先找到 https://www.huodongjia.com/event-1322992792.html，
        # 2.然后拼接成 json， https://www.huodongjia.com/event-1322992792.html?json=1

        link_list = re.findall(r"event-\d{10}.html", data)  # 匹配event-{old_event_id}

        target_url_list = []
        for event_id in link_list:
            if event_id not in self.published_event_id:
                target_url = self.domain_url + event_id + "?json=1"
                # print(target_url)  # for debug
                target_url_list.append(target_url)
        return target_url_list


# main to run
    def get_cat_page_event_data(self):
        """
        Call get_*() to get json data
        main() in the class
        :return:
        """

        target_url_list = self.get_event_url()
        # print(target_url_list)
        # print(len(target_url_list))

        for target_url in target_url_list[:5]:
            req = requests.get(target_url, headers=self.headers, timeout=10).content    # python2 str, python3 bytes

            # the JSON object must be str, not 'bytes'
            req = req.decode("utf-8")  # str

            # 将已编码的json字符串解码为Python对象
            req_dict = json.loads(req)
            # print("req_dict type is %s" % type(req_dict))

            event_url = self.domain_url + req_dict['event']['event_url']   # 不带?json=1

            event_name = req_dict['event']['event_name']

            event_id = req_dict['event']['event_id']

            # id = str(req_dict['event']['id'])   ＃ no use
            # event_status = req_dict['event']['event_status'] ＃ no use

            event_begin_time = req_dict['event']['event_begin_time']

            event_end_time = req_dict['event']['event_end_time']

            def get_event_img_v2():
                d_event = req_dict.get('event')
                # print("Output event_img list:")
                # print(d_event.get('event_img'))
                for item in d_event.get('event_img'):
                    # print(item)
                    # print(type(item))   # dict
                    return item['server__name'] + item['urls']

            event_img_url = get_event_img_v2()

            data = {

            }







if __name__ == '__main__':
    hwb = HWebCrawler()
    hwb.visit_event_cat_page()