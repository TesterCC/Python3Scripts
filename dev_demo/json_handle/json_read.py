# coding=utf-8
"""
DATE:   2021/1/7
AUTHOR: Yanxi Li
"""
import json

# read json
with open('audit_ids.json', 'r') as f:
    plm_audit_ids_json = json.load(f)

print(type(plm_audit_ids_json))
print(plm_audit_ids_json)