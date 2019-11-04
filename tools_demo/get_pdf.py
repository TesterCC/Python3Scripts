#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-10-29 21:02'

import requests
import re

def downloadPDF(url,filename):
    filename = filename + ".pdf"
    response = requests.get(url)
    fp = open(filename, 'wb')
    fp.write(response.content)
    fp.close()
    print(filename + ' has dowload succefully! \n')

if __name__ == '__main__':
    url = "https://www.t00ls.net/pdf.html?pdfid="
    down_url = "https://www.t00ls.net/"
    urls = ""
    for i in range(52550, 53400):
        urls = url + str(i)
        try:
            res = requests.get(urls, timeout=10)
            req = res.text
            print(req)  # 页面源代码中有写pdf下载地址
            string = "error"
            if string not in req:
                reg = re.compile('.*source: "(downloads/pdf.*?pdf)"', re.S)
                if re.match(reg, req):
                    path = reg.findall(req)
                    # print(down_url + path[0])
                    downloadPDF(down_url + path[0], str(i))
        except:
            print('something to wrong!')
        if i == 53399:
            print("All files had been download!")