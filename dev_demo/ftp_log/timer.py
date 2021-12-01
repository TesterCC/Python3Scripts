# coding=utf-8
"""
DATE:   2021/12/1
AUTHOR: TesterCC
"""
import time
from datetime import datetime, timedelta

cur_time = datetime.now()
print(cur_time)

# 1 month ago , 30 days
# past_time = cur_time - timedelta(days=30)     # online
past_time = cur_time - timedelta(seconds=1800)  # 0.5h

print(past_time)

# 转换为时间戳
ago_timestamp = int(time.mktime(past_time.timetuple()))

print(ago_timestamp)
