#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/13 00:17'

"""
《Python+Cookbook》第三版中文v3.0.0.pdf

14.1 测试stdout输出

问题:
你的程序中有个方法会输出到标准输出中(sys.stdout)。也就是说它会将文本打印 到屏幕上面。
你想写个测试来证明它,给定一个输入,相应的输出能正常显示出来。

解决方案:
使用unittest.mock模块中的patch()函数, 可以很方便的在测试运行的上下文中替换对象，且当测试完成时自动返回它们的原有状态
可以为单个测试模拟sys.stdout然后回滚,并且不产生大量的临时变量或在测试用例直接暴露状态变量。
"""

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import mymodule

"""
python -m unittest test_mymodule 
python -m unittest test_mymodule.TestURLPrint
python -m unittest test_mymodule.TestURLPrint.test_url_gets_to_stdout
"""


class TestURLPrint(TestCase):

    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'xueshu'
        domain = 'baidu.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            mymodule.urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)


