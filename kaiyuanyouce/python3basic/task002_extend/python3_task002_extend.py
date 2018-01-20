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

纯单IP:  150/3600 = 0.041666 = 0.041 次/s   24s/次
"""

from time import sleep

import requests
from openpyxl import Workbook


def douban_spider_ver2(keyword, file_name="douban_book.xlsx"):
    """
    用Requests库请求目标API接口
    注意反爬虫策略
    :param keyword:
    :param filename:
    """

    target_url = "https://api.douban.com/v2/book/search?q={0}".format(keyword)

    print("api url: %s " % target_url)

    r = requests.get(target_url)    # requests.models.Response
    ebook_dict = r.json()   # dict

    count = ebook_dict["count"]  # 本页书籍
    total = ebook_dict["total"]  # 总共书籍数

    print("每页展示 %d 本书的信息" % count)
    print("总计搜索到 %d 本书的信息" % total)

    print("开始将相关书籍信息写入Excel")

    print("Please wait (Maybe a long time...)")

    # 创建一个excel工作区
    wb = Workbook()

    # 获取sheet名称
    # print(wb.get_sheet_names())

    # 激活当前工作簿 worksheet
    ws = wb.active

    ws.append(["书名", "作者", "描述", "出版社", "价格"])

    # 从第2页开始，获取其他书籍信息
    for start in range(1, int(total / count) + 1):
        print("开始解析第{0}页数据".format(start))
        url = "https://api.douban.com/v2/book/search?q=%s&start=%d" % (keyword, start)
        try:
            response = requests.get(url)
            sleep(5)
        except KeyboardInterrupt:
            print("没耐心了，那就不要爬了")
            break
        except Exception as e:
            print("抛出异常，自己看堆栈报错信息:")
            print(e)
            break

        ebook_dict = response.json()   # dict

        # 输出书籍信息
        for book in ebook_dict["books"]:
            ws.append([book["title"],
                       ",".join(book["author"]),
                       book["summary"],
                       book["publisher"],
                       book["price"]])

            # 保存为excel文件
            wb.save(file_name)

            sleep(1)  # 暂时使用增加等待时间的方案，以防被封ip，最好要用动态UA和IP代理

        print("完成写入第{0}页数据".format(start))


if __name__ == '__main__':
    douban_spider_ver2("Python", "python_book_requests.xlsx")
    douban_spider_ver2("java", "java_book_requests.xlsx")






