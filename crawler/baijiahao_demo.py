#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/5/21 16:05'

from urllib.parse import quote
from urllib import request
from bs4 import BeautifulSoup
from urllib import error
from openpyxl import Workbook
import time

"""
# 脚本作用：百家号爬虫（获取各领域创作者appid）

ref:
https://www.pythonheidong.com/blog/article/134144/
https://www.jianshu.com/p/bc123402cc01

然后通过author的link去爬去这些作者发送的百家号

https://author.baidu.com/home?type=profile&action=profile&mthfr=box_share&context={"from":"ugc_share","app_id":"1572595784300706"}

xpath:
//div[@user_type='3']//div//@url
"""

# Some User Agents
hds = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}
]


# 当遍历账号后，百度搜索结果会重新开始；所以要获取第一个name，作为停止的判断标准
def name_first(field):
    url = 'https://www.baidu.com/sf?word=%E7%99%BE%E5%AE%B6%E5%8F%B7%2B' \
          + quote(field) + '&pd=cambrian_list&atn=index&title=%E7%99%BE%E5%AE%B6%E5%8F%B7%2B' \
          + quote(
        field) + '&lid=9080249029523443283&ms=1&frsrcid=206&frorder=1&pn=0&data_type=json%20---------------------%20'
    Response_1 = str(request.urlopen(url).read().decode('utf-8'))
    soup_1 = BeautifulSoup(Response_1, 'lxml')
    name_1 = soup_1.find('div', class_= \
        'c-color-link c-font-big sfc-cambrian-list-subscribe-title c-line-clamp1').string.strip()
    print(name_1)
    return name_1


def appid_list_excel(appid_list, field):
    wb = Workbook()
    ws = wb.active
    ws.append(['name', 'field', 'appid', 'smallfont', 'vip_info'])
    for i in range(len(appid_list)):
        lists = appid_list[i]
        ws.append([lists[0], lists[1], lists[2], lists[3], lists[4]])
    save_path = field
    save_path += '.xlsx'
    wb.save(save_path)


# 从百度搜索获取各领域百家号账号信息
def get_appid(field, name_1):
    number = 0  # URL地址中，pn=number为账号定位，XHR,每次从pn开始返回10账号，所以要循环操作
    appid_list = []
    name = 'name'

    while number <= 10000 and name != name_1:

        url = 'https://www.baidu.com/sf?word=%E7%99%BE%E5%AE%B6%E5%8F%B7%2B' \
              + quote(field) + '&pd=cambrian_list&atn=index&title=%E7%99%BE%E5%AE%B6%E5%8F%B7%2B' \
              + quote(field) + '&lid=9080249029523443283&ms=1&frsrcid=206&frorder=1&pn=' \
              + str(number) + '&data_type=json%20---------------------%20'

        try:
            req = request.Request(url, headers=hds[number % len(hds)])
            Response = str(request.urlopen(req).read().decode('utf-8'))
            soup = BeautifulSoup(Response, 'lxml')
            subsrcibes = soup.find_all('div', class_="sfc-cambrian-list-subscribe")
        except error.HTTPError as e:
            print("HTTPError")
            print(e.code)
        except error.URLError as e:
            print("URLError")
            print(e.reason)

        for subsrcibe in subsrcibes:
            smallfont = subsrcibe.find('div', class_='c-font-small c-gray c-line-clamp1').string.strip()
            name = subsrcibe.find('div', class_= \
                'c-color-link c-font-big sfc-cambrian-list-subscribe-title c-line-clamp1').string.strip()
            img_info = subsrcibe.find_all('img')  # 从图片地址截取信息
            try:
                appid_info = str(img_info[0])
                appid = appid_info[appid_info.find('_') + 1:appid_info.find('.jpeg')]
            except:
                appid = '缺失'
            try:
                vip_info = str(img_info[1]) \
                    [str(img_info[1]).find('vip'):str(img_info[1]).find('vip') + 5]
            except:
                vip_info = '暂无'
            if number >= 10 and name == name_1:
                break
            appid_list.append([name, field, appid, smallfont, vip_info])

        number += 10
        print('%s==%d' % (field, number))
        time.sleep(1)

    return appid_list


if __name__ == '__main__':
    #    field_list = ['人文’,'科技','互联网','数码','社会']

    # field_list = ['OKR培训','OKR公开课','OKR']
    field_list = ['区块链']
    for field in field_list:
        name_1 = name_first(field)
        appid_list = get_appid(field, name_1)
        appid_list_excel(appid_list, field)
    print('ok')
