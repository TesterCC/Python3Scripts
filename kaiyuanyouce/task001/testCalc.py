# -*- coding:utf-8 -*-

"""
Test Calc.py by unittest
"""
import unittest

from .Calc import Calc


class CalcTest(unittest.TestCase):
    """四则运算程序测试用例"""
    def setUp(self):
        self.cal = Calc(4, 5)

    def tearDown(self):
        print('\nTestcase Finish.')

    def test_add(self):
        result = self.cal.add()
        self.assertEqual(result, 9)

    def test_sub(self):
        result = self.cal.sub()
        self.assertEqual(result, -1)
    
    def test_mul(self):
        result = self.cal.mul()
        self.assertEqual(result, 20)

    def test_div(self):
        result = self.cal.div()
        self.assertEqual(result, 0.8)

    def test_div_except(self):
        self.cal = Calc(4, 0)
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()

