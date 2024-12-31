# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/7 22:35'


"""
扩展:

深入阅读urllib的源码和官方文档，熟悉其常用个API
基于POM思想，封装urllib，形成基于urllib库的入门测试接口测试框架 -- 个人还是推荐用requests

在httpclient_pom_demo.py的基础上修改

测试对象为豆瓣图书相关开放的API：

https://developers.douban.com/wiki/?title=book_v2

对于实例过程中用到的API请参见该链接API说明。

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484146&idx=1&sn=8e4db3b5a48e6cbd163cc0dd6b6acfc6&scene=19#wechat_redirect

下面实例中所有代码的封装不采用python任何的高级特性，只使用基本特性

必备知识：
urllib常用API
unittest
logging
PO模式

命令行运行：
python urllib_pom_demo.py

主要演示如何基于urllib + logging + unittest + pom进行基本的接口测试，
大家吸收下基本的思路就好，毕竟基于http.client这类的过于低层次的库来做还是太麻烦。
"""

import logging
import unittest
import urllib.parse
import urllib.request


# 日志管理类
LOGGING_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] -- %(levelname)s %(message)s'


class CustomLogging:
    def __init__(self,
                 level=logging.DEBUG,  # 日志级别
                 format=LOGGING_FORMAT,  # 日志格式
                 datefmt='%Y-%m-%d %a %H:%M:%S',  # 日期格式
                 filename='custom.log',  # 日志文件名
                 filemode='w'  # 文件打开模式
                 ):
        self.level = level
        self.format = format
        self.datefmt = datefmt
        self.filename = filename
        self.filemode = filemode

        # 初始化日志同时输出到console和日志文件
        logging.basicConfig(level=self.level,
                            format=self.format,
                            datefmt=self.datefmt,
                            filename=self.filename,
                            filemode=self.filemode)

        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('CustomHTTPLogger').addHandler(console)
        self.log = logging.getLogger("CustomHTTPLogger")

    # 日志输出
    def output(self, msg, level=logging.DEBUG):
        if level == logging.DEBUG:
            # 调试信息
            self.log.debug(msg)
        elif level == logging.INFO:
            # 一般的信息
            self.log.info(msg)
        elif level == logging.WARNING:
            # 警告信息
            self.log.warning(msg)
        elif level == logging.ERROR:
            # 错误信息
            self.log.error(msg)
        else:
            # 批评信息
            self.log.critical(msg)

    def set_level(self, level=logging.DEBUG):
        self.log.set_level(level)


# urllib封装
# http管理类
class CustomHttp:
    def __init__(self, timeout=30, log_level=logging.INFO):
        self.log_level = log_level
        self.log = CustomLogging(level=log_level)
        self.log.output("日志初始化完成，日志级别： %s" % self.log_level)

        self.timeout = timeout

        self.http = None
        self.response = None
        self.data = None
        self.status = None
        self.reason = None
        self.headers = None

    # 返回response响应对象
    def request(self,
                method,  # 请求方法
                url,  # 请求url
                body=None,  # 请求数据
                headers={}  # 请求头
                ):



        response = urllib.request.urlopen(url)

        if method == "GET":
            response = urllib.request.urlopen(url)
        elif method == "POST" and isinstance(body, dict):
            data = bytes(urllib.parse.urlencode(body), encoding='utf8')
            req = urllib.request.Request(url, data=data, headers=None)
            response = urllib.request.urlopen(req)
        else:
            print("目前仅支持POST和GET方法的请求")

        self.response = response

        self.data = self.response.read()
        self.status = self.response.status
        self.reason = self.response.reason
        self.log.output("------" * 10, self.log_level)
        self.log.output("\nrequest")
        self.log.output("\nurl: %s \nmethod: %s \nheaders: %s \ndata: %s" %
                        (url, method, headers, body), self.log_level)
        self.log.output("\nresponse")
        self.log.output("\nstatus: %s \nreason: %s \nheaders: %s \ndata: %s" %
                        (self.status, self.reason, self.headers, self.data), self.log_level)

        return self.response

    # 返回响应内容
    def get_data(self):
        return self.data

    # # 返回指定响应头
    # def get_header(self, name):
    #     for header in self.headers:
    #         if header[0] == name:
    #             return header[1]
    #
    #     return None

    # 返回完整的响应头
    def headers(self):
        return self.headers

    # 返回状态码及文本说明
    def get_status_reason(self):
        return self.status, self.reason


# Page基类
class Page:
    """
        基类，所有的page models都需要继承该类
    """

    def __init__(self, timeout=30, log_level=logging.INFO):
        self.http = CustomHttp(timeout=timeout, log_level=log_level)

    def request(self, method, url, body=None, headers={}):
        self.http.request(method=method, url=url, body=None, headers={})


# 测试jsontest.com提供的API
# 测试IP page
# 接口 ip.jsontest.com
class BookSearchPage(Page):
    """
    继承自基类
    """
    def __init__(self, timeout=30, log_level=logging.INFO):
        Page.__init__(self, timeout=timeout,
                      log_level=log_level)

    # 查询python相关的书籍
    def search_python_book(self, method, url, uri, body=None, headers={}):
        self.request(method=method, url=url+uri, body=body, headers=headers)

        return self.http.get_data()


# 测试用例
class TestSearchBookPage(unittest.TestCase):
    def setUp(self):
        self.book_search_page = BookSearchPage()

    def test_search_python_book(self):
        # 查找python相关的书籍即q=python，只找两本即count=2
        books = self.book_search_page.search_python_book(method="GET", url="https://api.douban.com", uri="/v2/book/search?q=python&count=2")

        # 获取并断言下http status及reason
        status, reason = self.book_search_page.http.get_status_reason()
        self.assertEqual(status, 200)
        self.assertEqual(reason, "OK")

        # 获取并断言下http header 例如断言下返回的Content-Type是不是application/json; charset=utf-8
        # content_type = self.book_search_page.http.get_header("Content-Type")
        # print("****" * 20)
        # self.assertEqual(content_type, "application/json; charset=utf-8")

        # 看一下返回的数据类型
        print("/v2/book/search?q=python&count=2返回的数据类型为： ", type(books))
        # 断言下返回类型
        self.assertIsInstance(books, bytes)

        # 强制将bytes类转成成dcit类型
        # 这里运行时 可能会出现一些警告信息，不用理会
        books_dict = eval(str(books, encoding="utf-8"))

        # 断言下count计数，应该为2, 因为我们只查找2本
        self.assertEqual(books_dict["count"], 2)

    def tearDown(self):
        print("Urllib POM Test End...")


if __name__ == "__main__":

    print("Python3 urllib Restful API测试实例")

    unittest.main()







