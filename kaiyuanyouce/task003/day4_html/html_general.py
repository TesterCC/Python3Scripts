# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/31 22:04'

"""
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484117&idx=1&sn=8ded39298f86e20a31c76889604d9093&scene=19#wechat_redirect

加深

根据上文的练习，对贵公司最复杂的页面进行数据提取分类。
并形成一个html解析通用类。
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

    print("获取首页html源码")

    # 构建博客园链接
    # conn = http.client.HTTPSConnection("www.fullstackpentest.com")
    conn = http.client.HTTPSConnection("www.csdn.net")

    # 获取博客园首页html源码
    conn.request("GET", "/")
    r1 = conn.getresponse()
    data = r1.read().decode(encoding="utf-8")

    # 打印返回的html源码
    print(data)
    print("-" * 90)

    # 解析目标首页html源码，提取所有a的href和文本数据
    blogHtmlParser = BlogHTMLParse()
    blogHtmlParser.feed(data)    # 接收一个字符串类型的HTML内容，并进行解析
    links = blogHtmlParser.get_data()

    # 打印提取的结果
    print("获取到的所有link：")
    print(links)
