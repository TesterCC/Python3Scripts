# coding=utf-8
'''
DATE: 2020/09/17
AUTHOR: Yanxi Li
'''

# P175 6.1读写CSV

# 原则：总是优先用csv模块分割或解析CSV数据

import csv

# write csv
headers = ["Symbol", "Price", "Date", "Time", "Change", "Volume"]

rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
        {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
        {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
        ]

with open('stocks2.csv', 'w', newline="") as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
