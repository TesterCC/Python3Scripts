# coding=utf-8
"""
DATE:   2021/1/7
AUTHOR: Yanxi Li
"""

# 从mongodb中读取数据，生成并写入json文件

import json
import pymongo

print('[+] Launch CRM & PLM sync tool -- PLM Server ...')
mongo_client = pymongo.MongoClient('mongodb://10.0.4.142:27017')
db = mongo_client['plm']

# run in plm server
# license
audit_col = db['audit']
license_col = db['license']

# print('[+] Total: ', license_col.find({}).count())  # low version pymongo 3.8.0 can use , now count is deprecated
print('[+] Total: ', license_col.count_documents({}))  # current use

audit_list = list(audit_col.find({}, {'_id': 1}))

# print(audit_list)

# write json
with open('audit_ids.json', 'w') as f:
    f.seek(0)
    f.truncate()
    json.dump(audit_list, f, indent=4)