#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/11/26 15:52'

import time
import os

"""
脚本: 监控服务器连接状态

usage:
In terminal:
python netstat_connection.py

end:
Ctrl + C

### 查看并发连接数
#### netstat -nat|grep ESTABLISHED|wc -l

### 查看其他类型连接数
#### netstat -nat|grep CLOSE_WAIT|wc -l
"""

while True:
    time.sleep(0.5)   # 单位：秒
    os.system("clear")
    os.system("netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'")
