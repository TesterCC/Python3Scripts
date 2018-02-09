#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/9 15:20'

import logging
from lib.CustomHttp import CustomHttp


# Page基类
class Page:
    """
    基类，所有的page models都需要继承该类
    """

    def __init__(self, protocol, host, port=80,
                 key_file=None,  # ssl
                 cert_file=None,  # ssl
                 timeout=30,
                 log_level=logging.INFO):
        self.http = CustomHttp(protocol=protocol,
                               host=host,
                               port=port,
                               key_file=key_file,
                               cert_file=cert_file,
                               timeout=timeout,
                               log_level=log_level)

    def request(self, method, url, body=None, headers={}):
        self.http.request(method=method, url=url, body=None, headers={})

    def close(self):
        if self.http:
            self.http.close()
