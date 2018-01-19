# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/19 23:20'


"""
任务二_细化 扩展任务
前提:已经将快学Python3系列基础示例练习完
需求:综合理利用上述基础知识完成以下任务：
实现一个基本的爬虫，利用豆瓣API爬取python相关数据信息，
包括但不限于：书名、作者、定价、摘要等等，
并将这些信息格式化到excel文档中

豆瓣API快速入门
https://developers.douban.com/wiki/?title=guide
"""

from time import sleep

import requests
from openpyxl import Workbook


def get_data_save_excel(keyword, filename):
    """
    用Requests库请求目标API接口
    注意反爬虫策略
    :param keyword:
    :param filename:
    """

    target_url = "https://api.douban.com/v2/book/search?q={0}".format(keyword)

    r = requests.get(target_url)    # requests.models.Response

    ebook_dict = r.json()   # dict

    count = ebook_dict["count"]  # 本页书籍
    total = ebook_dict["total"]  # 总共书籍数

    print("每页展示 %d 本书的信息" % count)
    print("总计搜索到 %d 本书的信息" % total)

    print("开始将相关书籍信息写入Excel")

    print("Please wait (Maybe a long time...)")

    # 这段代码采集了大量数据，容易被封IP，所以注释了
    for start in range(1, int(total / count) + 1):
        print("开始解析第{0}页数据".format(start))
        url = "https://api.douban.com/v2/book/search?q=%s&start=%d" % (keyword, start)
        try:
            response = requests.get(url)
            sleep(4)    # 增加延时，防止反爬虫策略
        except KeyboardInterrupt:
            print("没耐心了，那就不要爬了")
            break
        except Exception as e:
            print("程序异常, 别老爬别人的数据，要爬也别太快，会被封IP的")
            print(e)
            break

        ebook_dict = response.json()
        # print(ebook_dict)
        # print(type(ebook_dict))

        # 构建一个Workbook对象
        wb = Workbook()

        # 激活第一个sheet
        ws = wb.active

        # 写入表头
        ws.append(["书名", "作者", "描述", "出版社", "价格"])

        # 写入书信息
        for book in ebook_dict["books"]:
            ws.append([book["title"],
                       ",".join(book["author"]),
                       book["summary"],
                       book["publisher"],
                       book["price"]])
            # print("当前页书籍信息已写入Excel")

        # 保存
        wb.save(filename)
        print("完成第{0}页数据写入".format(start))
    print("目前获取的结果已写入excel")


if __name__ == '__main__':
    get_data_save_excel("Python", "douban_spider_python_book.xlsx")




