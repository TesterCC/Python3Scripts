#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/2 22:39'

"""
Python网络爬虫--从入门到实践   P36-39 3.4 TOP 250电影数据
Crawler Target: 
https://movie.douban.com/top250
https://movie.douban.com/top250?start=25
https://movie.douban.com/top250?start=50
...
https://movie.douban.com/top250?start=225


Host:movie.douban.com
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36


how to install lxml
pip install lxml
"""


import requests
from bs4 import BeautifulSoup


def get_movies():
    movie_list = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Host': 'movie.douban.com'
    }

    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start={0}'.format(i*25)
        # link = 'https://movie.douban.com/top250?start='+str(i*25)
        r = requests.get(link, headers=headers, timeout=7)
        print(str(i+1), "页面响应状态码:", r.status_code)
        # print(r.text)

        soup = BeautifulSoup(r.text, "lxml")  # pip install lxml
        # soup = BeautifulSoup(r.text, "html.parser")  # 这个是python3.5自带的网页解析器,也可以用

        div_list = soup.find_all('div', class_='hd')    # 避开关键词重复，BS中用class要写成class_
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list

# run get_movies()
movies = get_movies()
print(movies)



