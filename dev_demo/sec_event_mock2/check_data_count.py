# coding=utf-8
"""
DATE:   2022/1/10
AUTHOR: TesterCC
"""

from dup_merge_data.sec_event_mock2.sec_event_data import read_json

ret = read_json("./analysis_data.json")

print(type(ret))
print(len(ret))

for i in ret[:10]:
    print(i)