#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-07-03 17:06'

# local

# online
import os

DB_HOST = 'xxx.com'
DB_USER = ''
DB_PASSWD = ''
DB_NAME = ''
DB_PORT = 3306
DB_CHARSET = 'utf8'

CUR_PATH = os.getcwd() + '/test/' # linux

WEB_ACCOUNT = {
    'guanwei': {
        "name": "xxxx@xxx.com",
        "password": "xxx",
    }
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    # 'Host': 'www.huodongjia.com',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}

# 12 industry
CAT_INFOS = [
    (2, u"IT互联网", "it"),
    (6, u"金融财经", "finance"),
    (4, u"医疗医学", "medical"),
    (3, u"能源化工", "energy"),
    (9, u"农林牧渔", "agricultur"),
    (118, u"教育培训", "edutrain"),
    (120, u"加工制造", "manufact"),
    (122, u"地产建筑", "realestate"),
    (124, u"文化传媒", "culmedia"),
    (126, u"服务行业", "servindust"),
    (128, u"交通物流", "tralogist"),
    (96, u"其它行业", "trade")
]

CAT_INFO_LIST = [{'cat_eid': 'it', 'cat_name': 'IT互联网', 'cat_id': 2},
                 {'cat_eid': 'finance', 'cat_name': '金融财经', 'cat_id': 6},
                 {'cat_eid': 'medical', 'cat_name': '医疗医学', 'cat_id': 4},
                 {'cat_eid': 'energy', 'cat_name': '能源化工', 'cat_id': 3},
                 {'cat_eid': 'agricultur', 'cat_name': '农林牧渔', 'cat_id': 9},
                 {'cat_eid': 'edutrain', 'cat_name': '教育培训', 'cat_id': 118},
                 {'cat_eid': 'manufact', 'cat_name': '加工制造', 'cat_id': 120},
                 {'cat_eid': 'realestate', 'cat_name': '地产建筑', 'cat_id': 122},
                 {'cat_eid': 'culmedia', 'cat_name': '文化传媒', 'cat_id': 124},
                 {'cat_eid': 'servindust', 'cat_name': '服务行业', 'cat_id': 126},
                 {'cat_eid': 'tralogist', 'cat_name': '交通物流', 'cat_id': 128},
                 {'cat_eid': 'trade', 'cat_name': '其它行业', 'cat_id': 96}]



