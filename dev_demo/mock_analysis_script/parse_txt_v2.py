#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import os
import sys

# python3 parse_txt_v2.py 1.txt   ->   1.json

data = []

# file_path = "/opt/ips/1.txt"
file_path = sys.argv[1]
file_name = os.path.basename(file_path)

with open(file_path) as f:
    count = 0
    for line in f:
        # parse every line to dict
        line_data = {count: line}
        print(line_data)
        data.append(line_data)
        count += 1
print("[D] all data: ", data)
# write json
with open(f"{file_name.replace('.txt','.json')}", "w") as f:
    json.dump(data, f, indent=4)

print(f"[D] Finish parse and generate file: {file_name.replace('.txt','.json')}")