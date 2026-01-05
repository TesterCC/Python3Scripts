# -*- coding: utf-8 -*-
# @date  : 2026/1/5

import json

with open("ra_sast_system_rules.json",'r', encoding='utf-8') as f:
    data = json.load(f)

rule_list = data["content"]

total_checker_count = 0
for i in rule_list:
    total_checker_count += i.get("checkerCount")
    print(f"{i.get("name")}: {i.get("checkerCount")}")

print(">>"*33)
# print(rule_list)  # debug
print("所有内置规则集合数：", len(rule_list))  # 55 rule set
print("所有内置规则数：", total_checker_count)  # 8409 rules
