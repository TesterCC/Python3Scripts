#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/6 23:53'

"""
Python网络爬虫--从入门到实践   P42-44
解析真实地址抓取

http://www.santostang.com/2017/03/02/hello-world/

抓取来必力评论:
"https://api-zero.livere.com/v1/comments/list?callback=jQuery1124025451041961429377_1523032354340&limit=10&repSeq=3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1523032354342"
"https://api-zero.livere.com/v1/comments/list?callback=jQuery1124025451041961429377_1523032354340&limit=10&offset=2&repSeq=3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1523032354345"
"https://api-zero.livere.com/v1/comments/list?callback=jQuery1124025451041961429377_1523032354340&limit=10&offset=3&repSeq=3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1523032354346"

User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36

关于find link：

应该点JS，然后看里面的Preview或者Response，里面响应的是Ajax的内容，然后如果去爬网站的评论的话，点开js那个请求后点Headers -->在General里面拷贝 RequestURL
"""

import json
import requests
from bs4 import BeautifulSoup

# TARGET_URL = "https://api-zero.livere.com/v1/comments/list?callback=jQuery1124025451041961429377_1523032354340&limit=10&offset=2&repSeq=3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1523032354345"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

# print(r.text)
# print(type(r.text))  'str'


def single_page_comment(link):
    r = requests.get(link, headers=headers)

    # 从 json数据中提取评论。上述的结果比较杂乱，但是它其实是 json 数据，可以使用 json 库解析数据，从中提取想要的数据。

    # get json string
    json_string = r.text

    # 提取字符串中符合json格式的部分
    json_string = json_string[json_string.find('{'):-2]    # 提取数据，因为返回的数据不是直接的标准json格式

    json_data = json.loads(json_string)    # Deserialize a json str -> Python Object

    comment_list = json_data['results']['parents']

    for each in comment_list:
        comment = each['content']
        print(comment)


def bs4_get(link):
    r = requests.get(link, headers=headers)
    json_string = r.text
    soup = BeautifulSoup(json_string, 'lxml')
    # print(soup)


if __name__ == '__main__':
    bs4_get("http://www.santostang.com/2017/03/02/hello-world/")



