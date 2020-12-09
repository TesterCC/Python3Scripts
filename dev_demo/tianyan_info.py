#!/usr/bin/env python3
# coding=utf-8
"""
DATE:   2020/12/9
AUTHOR: Yanxi Li
脚本有些问题，不太好用
"""

# import pysnooper
import requests, re, time, json
from lxml import etree
from urllib.parse import quote, unquote

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
    # "Referer": "https://www.tianyancha.com/login?from=https%3A%2F%2Fwww.tianyancha.com%2Fsearch%3Fkey%3Dbaidu",
    "Referer": "https://www.tianyancha.com/login?from=https%3A%2F%2Fwww.tianyancha.com%2Fsearch%3Fkey%3D",
    "Cookie": "CT_TYCID=123;"
}

# @pysnooper.snoop()
def get_id(search_word):
    url = f"https://www.tianyancha.com/search/p1?key={search_word}"
    r = requests.get(url, headers=headers, timeout=5, allow_redirects=False)
    # print(r.text)
    html = etree.HTML(r.text)
    page = html.xpath('//*[@id="customize"]/div/@onclick')
    # print(page[0])
    print(page)   # debug
    page_total = int(re.search(", (\d+?)\)", str(page[0])).group(1))
    href = html.xpath('//div[@class="search-result-single  "]//a[contains(@class,"name")]/@href')
    # print(href)
    href_id = [re.search("company/(\d+)", url).group(1) for url in href]
    # print(href_id)
    return href_id

# @pysnooper.snoop()
def get_cloud_token(id):
    url = f"https://capi.tianyancha.com/cloud-equity-provider/v4/qq/name.json?id={id}?random={int(time.time())}"
    r = requests.get(url, headers=headers, timeout=5)
    res_data = json.loads(r.text)
    chars = res_data['data']['v']
    fnStr = "".join([chr(int(x)) for x in chars.split(',')])
    cloud_token = re.search("cloud_token=([a-z0-9A-Z]+)?;", fnStr).group(0)
    return cloud_token

# @pysnooper.snoop()
def get_equity(cloud_token, id):
    url = f"https://capi.tianyancha.com/cloud-equity-provider/v4/equity/indexnode.json?id={id}"
    headers['Cookie'] += cloud_token
    headers['Orgin'] = "https://dis.tianyancha.com"
    res_data = requests.get(url, headers=headers, timeout=5).text
    json_data = json.loads(res_data)["data"]["investorList"]
    for k in json_data:
        print("name:" + k["name"] + "-equity:" + str(k["percent"]) + "-id:" + str(k["id"]))
    headers['Cookie'].replace(cloud_token, "")

def  main():
    search_word = quote("网易")    # 只有默认的百度、网易正常，其它多字关键字有问题
    id_list= get_id(search_word)
    print(search_word,id_list)      # debug
    cloud_token = get_cloud_token(id_list[1])
    get_equity(cloud_token, id_list[1])


if __name__ == '__main__':
    main()
