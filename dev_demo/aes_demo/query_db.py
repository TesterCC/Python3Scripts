# -*- coding: utf-8 -*-
import traceback

import pymongo

db_name = "admin"
db_host = "127.0.0.1"
db_port = "27017"

username = "root"
password = "xxxxxx"


try:
    print(f'[*] Test auth login {db_name} database ...')
    mongo_client = pymongo.MongoClient(f'mongodb://{db_host}:{db_port}')
    # mongo_client = pymongo.MongoClient(db_host,int(db_port))

    db = mongo_client[db_name]
    # auth login
    db.authenticate(username, password)  
    
    print("pass auth ...")

    # 注意counters作为计数器需要存在，初始化需要，task_id自增需要
    counters_col = db['testcol']
    counters_col.drop()
    #counters_col.insert_one({"_id": "log_id", "sequence_value": int(0)})
    counters_col.insert_one({"_id": "task0001", "name":"测试登录认证"})

    print(f"[*] Finish {db_name} connection ...")

except:
    traceback.print_exc()
