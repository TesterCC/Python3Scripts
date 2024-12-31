# coding=utf-8
'''
DATE: 2020/09/18
AUTHOR: Yanxi Li
'''

# P178-179  6.2读写JSON数据

# 将Python数据结构转换为JSON

import json

data = {
    "name": "TESTER",
    "shares": 100,
    "price": 547.16
}

json_str = json.dumps(data)
print(type(json_str), json_str)