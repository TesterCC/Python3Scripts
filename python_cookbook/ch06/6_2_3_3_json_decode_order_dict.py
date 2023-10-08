# -*- coding=utf-8 -*-

import json
from collections import OrderedDict

from pprint import pp

# P183 6.2.3 JSON解码时会从所提供的数据中创建出字典或者列表。如果想创建其他类型对象，可以为 json.loads()方法提供object_pairs_hook或object_hook参数。
# 示例：将JSON数据解码为OrderedDict有序字典，以保持数据顺序不变。

s = '{"name":"ACME", "shares":50, "price":490.7}'

data = json.loads(s, object_hook=OrderedDict)
# data = json.loads(s, object_pairs_hook=OrderedDict)  # can run but IDE warning

print(f"[D] data type: {type(data)} \n[D] data: {data}")


