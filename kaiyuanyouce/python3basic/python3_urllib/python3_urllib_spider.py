# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/17 16:40'


"""
HTTP处理 - urllib模块

豆瓣网API网址：
https://developers.douban.com/wiki/?title=guide

https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484061&idx=1&sn=3f1a1533abf42f0bbfef8047c3aca519&scene=19#wechat_redirect
"""

import urllib.request
import csv
import codecs
from time import sleep


def douban_spider(keyword):
    """
    实例演示了如何使用豆瓣网的API 进行数据爬取
    :param keyword: 搜索关键字
    """

    url = "https://api.douban.com/v2/book/search?q={0}".format(keyword)
    print("api url: %s " % url)

    response = urllib.request.urlopen(url)

    # 将bytes数据流解码成string
    ebook_str = response.read().decode()

    # 将string转换成dict
    ebook_dict = eval(ebook_str)

    # print(ebook_dict)
    # print(type(ebook_dict))

    count = ebook_dict["count"]   # 本页书籍
    total = ebook_dict["total"]   # 总共书籍数

    print("当前页书籍数量: %d" % count)

    with codecs.open('books.csv', 'w', 'utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["书名", "作者", "描述", "出版社", "价格"])
        # 写书信息
        for book in ebook_dict["books"]:
            spamwriter.writerow([book["title"],
                                 ",".join(book["author"]),
                                 book["summary"],
                                 book["publisher"],
                                 book["price"]])
            # print(book)

        # 从第2页开始，获取其他书籍信息
        # 这段代码采集了大量数据，容易被封IP，所以注释了

        for start in range(1, int(total / count) + 1):
            url = "https://api.douban.com/v2/book/search?q=%s&start=%d" % (keyword, start)
            try:
                response = urllib.request.urlopen(url)
                sleep(3)
            except:                
                print("别老爬别人的数据，要爬也别太快，会被封IP的")  
                break

            # 将bytes数据流解码成string
            ebook_str = response.read().decode()

            # 将string转换成dict
            ebook_dict = eval(ebook_str)

            # 输出书籍信息
            for book in ebook_dict["books"]:
                spamwriter.writerow([book["title"], 
                ",".join(book["author"]), 
                book["summary"], 
                book["publisher"], 
                book["price"]])
                sleep(2)      # 增加等待时间，以防被封ip，最好要用动态UA和IP代理
                print(book)

        print("总计搜索到 %d 本书的信息" % total)


if __name__ == '__main__':
    print("urllib爬取豆瓣网数据示例")
    print("搜索下关键字： Python")
    douban_spider("Python")

