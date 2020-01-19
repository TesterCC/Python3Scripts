#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020-01-19 21:02'

"""
如何抓取、格式化和绘制，比特币过去一个小时在 Genimi 交易所的价格曲线


可以使用 Zipline 进行策略回测，或者用 Pyfolio 进行投资组合分析。
而许多交易所也都提供了基于 Python 的 API 客户端。

思考题：高频交易和中低频交易，哪个更适合使用 Python？为什么？

思考题答案：Python 更适合中低频量化交易中的使用，高频交易以 C++ 等速度更快，对系统底层访问更友好的编程语言为主。

"""

import matplotlib.pyplot as plt
import pandas as pd
import requests

# 选择要获取的数据时间段
periods = '3600'   # 3600s = 1h

# 通过 Http 抓取 btc 历史价格数据
resp = requests.get('https://api.cryptowat.ch/markets/gemini/btcusd/ohlc',
                    params={
                        'periods': periods
                    })
data = resp.json()

# print(data['result'])

print("=" * 50)

# 转换成 pandas data frame
df = pd.DataFrame(
    data['result'][periods],
    columns=[
        'CloseTime',
        'OpenPrice',
        'HighPrice',
        'LowPrice',
        'ClosePrice',
        'Volume',
        'NA'])

# 输出 DataFrame 的头部几行
print(df.head())

# 绘制 btc 价格曲线
df['ClosePrice'].plot(figsize=(14, 7))

plt.show()   # 现实绘制的图片