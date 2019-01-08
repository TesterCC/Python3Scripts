#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-01-08 18:08'


import requests
import re


QUERY_SITE_URL = "http://2018.ip138.com/ic.asp"  # 可能会变

def get_ip_by_ip138():
    response = requests.get(QUERY_SITE_URL)
    ip = re.search(r"\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]",response.content.decode(errors='ignore')).group(0)   # str [xx.xx.xxx.x]
    ip = ip.strip("[]")
    return ip

print("Localhost public IP -->", get_ip_by_ip138())

