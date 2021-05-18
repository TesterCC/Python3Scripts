# coding=utf-8
"""
DATE:   2021/5/18
AUTHOR: Yanxi Li
"""

import requests
from bs4 import BeautifulSoup

from dev_demo.sec_event_mock.sec_event_data import *


def get_website_title():
    res = requests.get("https://www.hao123.com/")
    # res.encoding = 'utf-8'  # 百度需要，不然乱码
    soup = BeautifulSoup(res.text, 'lxml')

    # print(soup)
    # print(soup.title.text)
    soup_objs = soup.find_all("a", class_="sitelink icon-site")
    # print(len(soup_objs))
    ret = {}
    for i in soup_objs:
        # print(i.text, i['href'])   # title, url
        if "hao123" not in get_domain(i['href']):
            ret[i.text] = get_domain(i['href'])

    # print(ret)
    write_json("./website.json",ret)


def gen_website_node_json(count=100):
    web_info = read_json("./website.json")
    ret = []

    for i in range(count):
        random_title = random.sample(web_info.keys(), 1)
        data = {
            "title": random_title[0],
            "domain": web_info.get(random_title[0]),   # urlparse处理下，获取domain
            "ip": get_random_wan_ip(),
            "protocol": random.choice(["https","http"])
        }
        # print(random_title, web_info.get(random_title[0]))
        ret.append(data)

    # print(ret)
    write_json("./website_node.json",ret)

if __name__ == '__main__':
    # get_website_title()  # generate simple data
    # print(read_json("./website.json"))
    gen_website_node_json(count=1000)    # generate website_node data
