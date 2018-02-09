# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/9 15:11'

import unittest
from model.BookSearchPage import BookSearchPage


# 测试用例
class TestSearchBookPage1(unittest.TestCase):

    def setUp(self):
        self.book_search_page = BookSearchPage(protocol="https", host="api.douban.com", port=443)
    
    def test_search_python_book(self):
        # 查找python相关的书籍即q=python，只找两本即count=2
        books = self.book_search_page.search_python_book(method="GET", url="/v2/book/search?q=python&count=2")
        
        # 获取并断言下http status及reason
        status, reason = self.book_search_page.http.get_status_reason()
        self.assertEqual(status, 200)
        self.assertEqual(reason, "OK")

        # 获取并断言下http header 例如断言下返回的Content-Type是不是application/json; charset=utf-8
        content_type = self.book_search_page.http.get_header("Content-Type")
        self.assertEqual(content_type, "application/json; charset=utf-8")

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
        self.book_search_page.close()

