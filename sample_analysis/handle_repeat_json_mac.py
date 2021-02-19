# coding=utf-8
"""
DATE:   2021/2/4
AUTHOR: Yanxi Li
"""

import json
import os

# 读取样本原始日志信息
with open('./poc_v1.json', 'r') as f:
    data = json.load(f)

print("poc_v1.json count: ", len(data))
# print(type(data))
# print(data)

sample_char = "plugins/v3.400.7-win64/TitanAgent_for_All_x86_64.exe"
repeat_files = []      # 记录重复文件名
for item in data:
    if sample_char in item['desc']:
        # print(item['filename'])
        repeat_files.append(item['filename'])
        data.remove(item)


# print(repeat_files)
print(f"[*] Repeat info count: {len(repeat_files)} ")   # 312 -> 246
print(f"{len(data)}")

with open('poc_v2.json', 'w') as f:
    f.seek(0)
    f.truncate()
    json.dump(data, f, indent=4)



with open('poc_v2.json', 'r') as f:
    data = json.load(f)
    print("[TEST] handle data count: ", len(data))
