#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/7 01:20'

"""
TEST multi request
"""

import requests

def get_score(score:int):

    TARGET_URL = "http://127.0.0.1:16384/{}".format(score)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }


    r = requests.get(TARGET_URL, headers=headers, timeout=10)

    if r.status_code == 200:
        print(r.json())

if __name__ == '__main__':
    for i in range(988,1050):
        get_score(i)