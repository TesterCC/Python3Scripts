# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/1 12:16'

"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484117&idx=1&sn=8ded39298f86e20a31c76889604d9093&scene=19#wechat_redirect
06 解析下html

代码运行的流程：

1.运行__init__初始化实例
2.执行handle_starttag
3.执行handle_data
4.执行handle_endtag
5.重复2、3、4直至把所有的a提取完毕

简单的应用场景：
1.爬取目标html元素，自动构建xpath或css定位，用于UI级自动化测试
2.爬取目标URL下所有的链接或form表单相关资源，获取可能的接口测试目标
3.爬取感兴趣的资源，只要你感兴趣就好
4.其他应用场景
"""

from html.parser import HTMLParser
import http.client


class BlogHTMLParse(HTMLParser):
    data = []
    data_key = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.is_a = False   # 默认 is_a为False

    def handle_starttag(self, tag, attrs):
        # 处理开始为a的标签
        if tag == "a":
            self.is_a = True
            for name, value in attrs:
                if name == "href":
                    # 提取a的href属性值
                    self.data_key = value

    def handle_data(self, data):
        # 处理结束为a的标签
        if self.is_a and self.lasttag == "a":
            # 将a标签的href属性值作为key， a的文本作为data构建字典
            self.data.append({self.data_key: data})

    def handle_endtag(self, tag):
        # 处理a结束标签
        if self.is_a and self.lasttag == "a":
            self.is_a = False

    def get_data(self):
        # 返回所有从a中提取到的目标数据
        return self.data


if __name__ == '__main__':

    print("python HTML解析实例")

    print("访问博客网，获取首页html源码")

    # 构建博客园链接
    conn = http.client.HTTPSConnection("www.cnblogs.com")

    # 获取博客园首页html源码
    conn.request("GET", "/")
    r1 = conn.getresponse()
    data = r1.read().decode(encoding="utf-8")

    # 打印返回的html源码
    print(data)
    print("-" * 90)

    # 解析博客园首页html源码，提取所有a的href和文本数据
    blogHtmlParser = BlogHTMLParse()
    blogHtmlParser.feed(data)    # 接收一个字符串类型的HTML内容，并进行解析
    links = blogHtmlParser.get_data()

    # 打印提取的结果
    print(links)
