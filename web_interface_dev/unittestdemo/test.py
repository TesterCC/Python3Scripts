#!/usr/bin/env python
# coding=utf-8

'''
Author: Yanxi
Date: 2017/06/15
Describe: 实现简单计算器 + - * / 的unittest
Web接口开发与自动化测试-基于Python语言  P98-99
'''


import unittest
from web_interface_dev.unittestdemo.module import Calculator


class ModuleTest(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator(8, 4)

    def tearDown(self):
        # print("Testcase tear down.")
        pass

    def test_add(self):
        result = self.cal.add()
        self.assertEqual(result, 12)

    def test_sub(self):
        result = self.cal.sub()
        self.assertEqual(result, 4)

    def test_mul(self):
        result = self.cal.mul()
        self.assertEqual(result, 32)

    def test_div(self):
        result = self.cal.div()
        self.assertEqual(result, 2)


if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest("test_sub"))
    suite.addTest(ModuleTest("test_mul"))
    suite.addTest(ModuleTest("test_div"))

    # 执行测试
    runner = unittest.TextTestResult()
    runner.run(suite)         # 运行测试集
