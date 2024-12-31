# -*- coding=utf-8 -*-

import json
from collections import OrderedDict

from pprint import pp

# P184 通过解码JSON数据而创建的字典作为单数的参数传递给了__init__()

s = '{"name":"ACME", "shares":50, "price":490.7}'


# 将JSON字典转变为Python对象
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


data = json.loads(s, object_hook=JSONObject)

print(f"[D] {data.name} , {data.shares}, {data.price}")
