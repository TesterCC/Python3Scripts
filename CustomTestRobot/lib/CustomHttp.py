#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/9 15:18'

import http.client
import logging

from common.CustomLogging import CustomLogging


# http.client封装
# http管理类
class CustomHttp:
    def __init__(self, protocol, host, port=80,
                 key_file=None,  # ssl
                 cert_file=None,  # ssl
                 timeout=30,
                 log_level=logging.INFO
                 ):
        self.log_level = log_level
        self.log = CustomLogging(level=log_level)
        self.log.output("初始化http连接到: %s:%d" % (host, port))

        self.host = host
        self.port = port
        self.timeout = timeout
        self.key_file = key_file
        self.cert_file = cert_file
        self.response = None
        self.data = None
        self.status = None
        self.reason = None
        self.headers = None

        self.http = None
        if protocol == "http":
            self.http = http.client.HTTPConnection(host=self.host,
                                                   port=self.port, timeout=self.timeout)
        elif protocol == "https":
            self.http = http.client.HTTPSConnection(host=self.host,
                                                    port=self.port,
                                                    key_file=self.key_file,
                                                    cert_file=self.cert_file,
                                                    timeout=self.timeout)
        else:
            print("不支持的协议类型: ", protocol)
            exit()

    # 返回response响应对象
    def request(self,
                method,  # 请求方法 
                url,  # 请求url
                body=None,  # 请求数据
                headers={}  # 请求头
                ):
        self.http.request(method=method, url=url, body=body, headers=headers)

        self.response = self.http.getresponse()

        self.data = self.response.read()
        self.status = self.response.status
        self.reason = self.response.reason
        self.headers = self.response.getheaders()
        self.log.output("------" * 10, self.log_level)
        self.log.output("\nrequest")
        self.log.output("\nurl: %s \nmethod: %s \nheaders: %s \ndata: %s" % (url, method, headers, body),
                        self.log_level)
        self.log.output("\nresponse")
        self.log.output(
            "\nstatus: %s \nreason: %s \nheaders: %s \ndata: %s" % (self.status, self.reason, self.headers, self.data),
            self.log_level)

        return self.response

    # 关闭连接
    def close(self):
        if self.http:
            self.http.close()

    # 返回响应内容
    def get_data(self):
        return self.data

    # 返回指定响应头
    def get_header(self, name):
        for header in self.headers:
            if header[0] == name:
                return header[1]

        return None

    # 返回完整的响应头列表
    def headers(self):
        return self.headers

    # 返回状态码及文本说明
    def get_status_reason(self):
        return self.status, self.reason

