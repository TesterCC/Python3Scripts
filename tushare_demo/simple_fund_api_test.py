#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-12 22:26'

from tushare.fund import nav


# def test_get_nav_open():
#     # lst = ['all', 'equity', 'mix', 'bond', 'monetary', 'qdii']
#     lst = ['monetary']
#     print('get nav open................\n')
#     for item in lst:
#         print('=============\nget %s nav\n=============' % item)
#         fund_df = nav.get_nav_open(item)
#         print('\nnums=%d' % len(fund_df))
#         print(fund_df[:2])    # 返回的数据 return pd.concat(fund_dfs, ignore_index=True)
#
# test_get_nav_open()
# TypeError: first argument must be an iterable of pandas objects, you passed an object of type "DataFrame"

# get fund history info
ret = nav.get_nav_history("160716", start="2019-03-01",end="2019-03-12")

print(type(ret))
print(ret)

# get fund detail info
ret2 = nav.get_fund_info("160716")
print(type(ret2))
print(ret2)
