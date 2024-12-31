#!/usr/bin/env python
# coding: utf-8
# author: XJC
"""
    PYTHON，SYSLOG中转程序（中间客户端，RSYSLOG取不到真实IP）
"""
from socket import *
import logging
import re
from logging.handlers import TimedRotatingFileHandler
import sys
import os
import time

# import socket
import configparser

try:
    import requests
except ImportError:
    print('Error: 请先安装REQUESTS!')
    exit()

out = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(out)




def setup_log(log_name):
    logger = logging.getLogger(log_name)
    log_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "logs")

    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_path = os.path.join(log_path, log_name)
    # 设置日志记录等级
    logger.setLevel(logging.INFO)
    # interval 滚动周期，
    # when="MIDNIGHT", interval=1 表示每天0点为更新点，每天生成一个文件
    # backupCount  表示日志保存个数
    file_handler = TimedRotatingFileHandler(
        filename=log_path, when="MIDNIGHT", interval=1, backupCount=7
    )
    # filename="mylog" suffix设置，会生成文件名为mylog.2020-02-25.log
    file_handler.suffix = "%Y-%m-%d.log"
    # extMatch是编译好正则表达式，用于匹配日志文件名后缀
    # 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除。
    file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
    # 定义日志输出格式
    file_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s] [%(process)d] [%(levelname)s] - %(module)s.%(funcName)s (%(filename)s:%(lineno)d) - %(message)s"
        )
    )
    logger.addHandler(file_handler)
    return logger


def get_host_ip():
    try:
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()


try:
    logger = setup_log("syslog")
except Exception as e:
    print(str(e))

# 获取当前主机IP
host = get_host_ip()
port = 9003
# UPD特性
buf = 65535
addr = ('127.0.0.1', port)
UDPSock = None
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)


def report(syslogType, content):
    data = {}
    data.setdefault("syslogIp", host)
    data.setdefault("syslogContent", content)
    data.setdefault("syslogType", syslogType)
    data.setdefault("syslogTimestamp", int(time.time()))
    print(data)
    logger.info(data)
    return data


# 开始接受当前虚拟机发送的SYSLOG然后保存至服务端
while 1:

    try:
        data, addr = UDPSock.recvfrom(buf)
        if not data:

            print('客户端退出')
            logger.info('客户端退出')
            break
        else:
            sdata = str(data.decode("utf-8"))
            logger.info(sdata)
            syslog_type = sdata.split('@')[0]
            report(syslog_type, sdata[(len(syslog_type) + 1):])
            # print ("\nReceived message '" + sdata + "'")
    except  Exception as e:
        logger.error(str(e))
        UDPSock.close()
        break
UDPSock.close()
