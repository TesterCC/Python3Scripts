# -*- coding: utf-8 -*-
# @Time    : 2023/6/26
# @Author  : SecCodeCat
import time

import pymongo
import json

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_col']

# 读取 JSON 文件, 96M，也就是说大文件基本不考虑数据入库了。
with open('related.json', 'r') as f:
    data = f.readlines()
    # print(type(data))
    # print(type(data[0]))

st = time.time()
# 批量插入 JSON 数据
# result = collection.insert_many(data)

query = dict()
query['_id'] = round(time.time()*1000)
query['attack_map'] = data[0]
result = collection.insert_one(query)

# 输出插入结果
print(f'Inserted {len(result.inserted_ids)} documents.')

print(f"cost time: {time.time() - st}")

# pymongo.errors.DocumentTooLarge: BSON document too large (100457540 bytes)
# MongoDB的单个文档的BSON size不能超过16MB。