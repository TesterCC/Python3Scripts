#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 3-2 使用urllib发送post请求   http://www.imooc.com/video/12625

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse


TARGET_URL = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"

req = Request(TARGET_URL)

postData = parse.urlencode([
    ("StartStation", "2f940836-cedc-41ef-8e28-c2336ac8fe68"),
    ("EndStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
    ("SearchDate", "2017/08/10"),
    ("SearchTime", "22:00"),
    ("SearchWay", "DepartureInMandarin")
])

# 添加多个header内容
req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
resp = urlopen(req, data=postData.encode("utf-8"))

print(resp.read().decode("utf-8"))