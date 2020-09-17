# coding=utf-8
'''
DATE: 2020/09/17
AUTHOR: Yanxi Li
'''

# P175 6.1读写CSV

import csv

# write csv
headers = ["Symbol", "Price", "Date", "Time", "Change", "Volume"]

rows = [
    ('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
    ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
    ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
    ('TEST', 77.77, '6/11/2020', '9:36am', -0.01, 808000)
]

# 不设置newline的话，默认每行csv数据会空一行
with open('stocks.csv', 'w', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
