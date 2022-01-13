# coding=utf-8
"""
DATE:   2022/1/10
AUTHOR: TesterCC
"""

from dev_demo.sec_event_mock.sec_event_data import read_json

ret = read_json("./analysis_data.json")

print(ret)
print(len(ret))