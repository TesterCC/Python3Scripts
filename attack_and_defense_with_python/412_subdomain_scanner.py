# coding=utf-8
"""
DATE:   2020/12/3
AUTHOR: Yanxi Li

4.1.2 子域名挖掘
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple beautifulsoup4

usage:
python 412_subdomain_scanner.py huodongjia.com 200

这个是最简化脚本，可以用多线程或多进程优化
todo:
v2 多线程版
v3 多进程版
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

def bing_search(site, pages):
    subdomain = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
               'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.5',
               'Accept-Encoding': 'gzip,deflate',
               'referer': 'https://cn.bing.com/search?q=test&qs=n&form=QBRE&sp=-1&pq=test&sc=8-4'}


    for i in range(1, int(pages)+1):
        url = "https://cn.bing.com/search?q=site%3a" + site + "&go=Search&qs=ds&first=" + str((int(i) - 1) * 10)+"&FORM=PER"
        conn = requests.session()
        conn.get('http://cn.bing.com',headers=headers)
        html = conn.get(url, stream=True, headers=headers,timeout=8)
        soup = BeautifulSoup(html.content,'html.parser')
        job_bt = soup.findAll('h2')
        # print(job_bt,type(job_bt))   # debug

        for i in job_bt:
            if i.a:
                link = i.a.get('href')
            else:
                continue
            domain = str(urlparse(link).scheme + "://" + urlparse(link).netloc)

            if domain not in subdomain:
                subdomain.append(domain)

                print(domain)

    return subdomain

if __name__ == '__main__':
    if len(sys.argv) == 3:
        site = sys.argv[1]
        page = sys.argv[2]
    else:
        print("usage: %s xxx.com 10" % sys.argv[0])
        sys.exit(-1)

    subdomain = bing_search(site,page)
    print(subdomain)



