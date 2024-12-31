# -*- coding: utf-8 -*-
# @Time    : 2023/1/21
# @Author  : SecCodeCat

import pandas as pd
import tushare as ts

# https://tushare.pro/document/1?doc_id=290
# https://tushare.pro/document/1?doc_id=13

# api doc: https://tushare.pro/document/2?doc_id=103
# get data: https://tushare.pro/document/1?doc_id=230

# ref: https://blog.csdn.net/lost0910/article/details/104521881/
#  > 900: https://tushare.pro/document/2?doc_id=103

TOKEN = 'your-tushare-token'

ts.set_token(TOKEN)
pro = ts.pro_api()

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
print(data)

# ===
df = pro.daily(trade_date='20230109')

print(df)
