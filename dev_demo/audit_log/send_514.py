# coding=utf-8
"""
DATE:   2022/3/17
AUTHOR: TesterCC
"""

import os
import time
import socket
import traceback


eps = 100
syslog_addr = ('10.0.0.1', 514)
syslog_file = 'syslog12.log'


with open(syslog_file) as f:
    syslog_list = f.readlines()

tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   # tcp
tcp_socket.connect(syslog_addr)

for syslog in syslog_list:
    # print(syslog.encode('utf8'))
    # date = time.strftime('%B %d %H:%M:%S', time.localtime())
    # syslog = syslog.replace('{{date}}', date)
    tcp_socket.sendall(syslog.encode('utf8'))
    time.sleep(1/eps)
