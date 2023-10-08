# -*- coding=utf-8 -*-

import json

from urllib.request import urlopen

from pprint import pprint

# P182 6.2.3 JSON数据打印美化

u = urlopen('https://httpbin.org/get')
resp = json.loads(u.read().decode("utf-8"))
print(type(resp))
print("-" * 66)
pprint(resp)


