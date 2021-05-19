# coding=utf-8
"""
DATE:   2021/5/18
AUTHOR: Yanxi Li
"""

import requests
from bs4 import BeautifulSoup

from dev_demo.sec_event_mock.sec_event_data import *


def get_website_data():
    res = requests.get("https://www.hao123.com/")
    # res.encoding = 'utf-8'  # 百度需要，不然乱码
    soup = BeautifulSoup(res.text, 'lxml')

    ret = []
    # print(soup)
    # print(soup.title.text)

    soup_objs = soup.find_all("ul", class_="cool-row")

    for i in range(len(soup_objs)):
        # print(i.text, i['href'])   # title, url
        item_class = soup_objs[i].li.text
        item_obj = soup_objs[i].find("a", class_="sitelink icon-site")
        item_title = item_obj.text
        item_domain = get_domain(item_obj['href'])

        data = {
            "title": item_title,
            "domain": item_domain,
            "class": item_class,
            "ip": get_random_wan_ip(),
            "protocol": random.choice(["https", "http"]),
            "record_location": get_random_location(),
            "value": random.choice(["高", "中", "低"]),
            "create_time": get_random_create_time(),
        }

        ret.append(data)

    print(ret)
    write_json("./website_node_v2.json", ret)


# def gen_website_node_json(count=100):
#     web_info = read_json("./website.json")
#     ret = []
#
#     for i in range(count):
#         random_title = random.sample(web_info.keys(), 1)
#         data = {
#             "title": random_title[0],
#             "domain": web_info.get(random_title[0]),   # urlparse处理下，获取domain
#             "ip": get_random_wan_ip(),
#             "protocol": random.choice(["https","http"])
#         }
#         # print(random_title, web_info.get(random_title[0]))
#         ret.append(data)
#
#     # print(ret)
#     write_json("./website_node.json",ret)

if __name__ == '__main__':
    get_website_data()  # generate simple data
    # print(read_json("./website.json"))
    # gen_website_node_json_v2(count=1000)  # generate website_node data
