#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import os
import sys

data = []

# python3 parse_txt_v2.py 1.txt   ->   1.json

file_path = sys.argv[1]
file_name = os.path.basename(file_path)

if os.path.exists(file_path):
    # dir_data = os.listdir(check_path)
    # print(dir_data)  #  debug ['192.168.1.1.txt', '192.168.1.2.txt', '192.168.1.3.txt']

    json_file_path = f"{file_path}"
    with open(json_file_path) as f:
        for line in f:
            # parse every line to dict
            line_data = json.loads(line)
            data.append(line_data)

    updated_data = [{'sip': item['src_addr'], 'sport': item['src_port'], 'dip': item['dst_addr'],
                     'dport': item['dst_port'], 'protocol': item['protocol']} for item in data]

    # export_data = json.dumps(updated_data)
    # print(f"[D] txt all json data: {data}")
    print(f"[D] replace json data: {updated_data}")
    # print(f"[D] export_data json data: {type(export_data)}, {export_data}")
    # write json
    with open(f"{file_name.replace('.txt','.json')}", "w") as f:
        json.dump(updated_data, f, indent=4)

    print(f"[D] Finish parse and generate file: {file_name.replace('.txt', '.json')}")