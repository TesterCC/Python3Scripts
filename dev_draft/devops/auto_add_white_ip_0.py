#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-01-09 11:10'

"""
场景：让连接不同WIFI，有不同公网IP的slave自动每天向特定服务器发送IP并写入白名单文件

使用方便，还可以写一些其它的脚本试试
"""

import paramiko
import requests
import re

# set your server info
HOST_NAME = "127.0.0.0"
PORT = "22"
USERNAME = "xxxx"
PASSWORD = "xxxxxxxxxxx"

QUERY_SITE_URL = "http://2018.ip138.com/ic.asp"  # Maybe Changed


def get_ip_by_ip138():
    response = requests.get(QUERY_SITE_URL)
    ip = re.search(r"\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]", response.content.decode(errors='ignore')).group(
        0)  # str [xx.xx.xxx.x]
    ip = ip.strip("[]")
    return ip


def set_white_ip(public_ip):
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(HOST_NAME, PORT, USERNAME, PASSWORD, timeout=10)

    command = "echo '{}' >> /data/log/nginx/xxxxx/ip_white_list.txt; cat /data/log/nginx/xxxxx/ip_white_list.txt".format(
        public_ip)

    # 另一台用 >>, 这台用>

    stdin, stdout, stderr = client.exec_command(command, get_pty=True)
    print(stdout.readlines())

    client.close()


def get_white_ip():
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(HOST_NAME, PORT, USERNAME, PASSWORD, timeout=10)

    command = "cat /data/log/nginx/xxxxx/ip_white_list.txt"

    stdin, stdout, stderr = client.exec_command(command, get_pty=True)
    print(stdout.readlines())

    client.close()


if __name__ == '__main__':
    public_ip = get_ip_by_ip138()
    print("Localhost public IP -->", public_ip)
    set_white_ip(public_ip)

    # get_white_ip()   # 只查看get_white_ip
