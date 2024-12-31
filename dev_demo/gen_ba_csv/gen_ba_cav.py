# coding=utf-8
"""
DATE:   2022/3/1
AUTHOR: TesterCC
"""
import csv
import json


json_file = "./ba_type.json"
with open(json_file, 'r', encoding='utf-8') as f:
    ba_dict = json.load(f)

# print(type(ba_dict))
# print(ba_dict)

rows = []
for ba_l3_id in ba_dict:
    # print(ba_l3_id, ba_dict[ba_l3_id].get('name'))
    rows.append((ba_l3_id, ba_dict[ba_l3_id].get('name')))


# 不设置newline的话，默认每行csv数据会空一行
with open('ba_info.csv', 'w', newline="", encoding="utf-8") as f:
    f_csv = csv.writer(f)
    # f_csv.writerow(headers)
    f_csv.writerows(rows)

