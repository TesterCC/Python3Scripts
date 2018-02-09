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
pip isntall pytest-html

pytest pytest-html
执行文件：
pytest -q pytest_requests.py --html=./log.html   # 生成html report
pytest -q pytest_requests.py 


@pytest.mark.parametrize 为pytest参数化用法

演示下pytest和requests结合应用的示例

要输出html格式的报告，要事先安装pytest-html这个pytest的插件才行
"""

import pytest
import requests


# 基于 pytest + requests 测试接口
class TestRequestDemo:

    # 初始化
    url = "http://jsonplaceholder.typicode.com"
    session = requests.session()

    # 测试获取所有用户信息接口
    def test_get_posts(self):
        r = self.session.get(self.url + "/posts")

        # 断言状态码
        assert r.status_code == 200

        # 断言响应头信息
        assert r.headers["Content-Type"] == "application/json; charset=utf-8"

        # 断言用户总数
        assert len(r.json()) == 100

    # 测试获取指定用户信息接口
    def test_get_posts_by_id(self):
        r = self.session.get(self.url + "/posts/1")

        # 断言状态码
        assert r.status_code == 200

        # 断言响应头信息
        assert r.headers["Content-Type"] == "application/json; charset=utf-8"

        # 验证用户id
        data = r.json()
        assert data["userId"] == 1

    # 测试删除指定用户信息接口
    def test_delete_posts_by_id(self):
        r = self.session.delete(self.url + "/posts/1")

        # 断言状态码
        assert r.status_code == 200

        # 断言响应头信息
        assert r.headers["Content-Type"] == "application/json; charset=utf-8"


if __name__ == "__main__":
    pytest.main()




