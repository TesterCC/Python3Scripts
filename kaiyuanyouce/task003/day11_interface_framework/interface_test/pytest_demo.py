#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/9 21:39'


"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484209&idx=1&sn=4d9d535aab51450e69082ddb91e6a997&scene=19#wechat_redirect

pytest + requests示例

实例中用到的接口:
http://jsonplaceholder.typicode.com

安装pytest，命令如下：
pip install pytest

执行文件：
pytest -q pytest_demo.py

@pytest.mark.parametrize 为pytest参数化用法
"""

import pytest


class TestDemo:
    """
    测试加减法
    """
    # 加法
    @pytest.mark.parametrize("a, b, expected", [(1,2,3), (2,3,5), (3,4,8)])
    def test_add(self, a, b, expected):
        # 求和
        sum = a + b

        # 断言
        assert sum == expected

        # 减法
    @pytest.mark.parametrize("a, b, expected", [(1, 2, -1), (8, 3, 5), (3, 4, 8)])
    def test_sub(self, a, b, expected):
        # 减法
        s = a - b

        # 断言
        assert s == expected




