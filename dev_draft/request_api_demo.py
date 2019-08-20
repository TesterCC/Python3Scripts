#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-20 11:00'

import json
import requests

"""
for query xxx info
"""

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:62.0) Gecko/20100101 Firefox/60.0'

headers = {
    "User-Agent": user_agent
}

def query_sponsor(keywords):

    TARGET_URL = f"http://xxxxx.com/api/v2/sponsor/new_sponsor/?search={keywords}"

    res = requests.get(TARGET_URL, headers=headers)

    ret = json.loads(res.content)

    return ret.get('results')[0]

def query_venue(keywords):

    TARGET_URL = f"http://xxxxx.com/api/v2/venue/venue/?search={keywords}"

    res = requests.get(TARGET_URL, headers=headers)

    ret = json.loads(res.content)

    return ret.get('results')[0]

if __name__ == '__main__':
    d = query_sponsor("中国国际经济合作学会商务诚信工作委员会")
    # d = query_venue("北京国际会议中心 ")
    print(d)
    print(type(d))