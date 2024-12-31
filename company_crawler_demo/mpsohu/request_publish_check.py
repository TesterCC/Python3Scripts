#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/4 09:46'


"""   
https://mp.sohu.com/v2/main/news/preview_by_id.action?id=225206939
https://www.sohu.com/a/225206939_134221
"""

from time import sleep

import unittest

import requests

article_id = "225206939"
preview_url = "https://mp.sohu.com/v2/main/news/preview_by_id.action?id={}".format(article_id)

req = requests.get(preview_url)
print("Visit Preview: {}".format(req.status_code))

sleep(5)
print("Wait for Test")

published_url = "https://www.sohu.com/a/{0}_134221".format(article_id)
print(published_url)

req = requests.get(published_url)
print(req.status_code)

# print(notes.md.text)

if u"活动家" in req.text:
    print("Published Success!")
else:
    print("Failed, please check error!")

print("check完毕")

