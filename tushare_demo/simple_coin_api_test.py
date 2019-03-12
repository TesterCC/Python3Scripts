#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-12 21:53'


from tushare.coins import market

ret = market.coins_bar(broker='chbtc')

print(type(ret))
print(ret)