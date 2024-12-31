# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/17 16:40'


"""
HTTP处理 - urllib模块

豆瓣网API网址：
https://developers.douban.com/wiki/?title=guide
https://developers.douban.com/wiki/?title=api_v2

https://github.com/douban/douban-client

不需要授权公开api可以使用http，参数里面如果不包含apikey的话，限制单ip每小时150次，带的话每小时500次。带apikey的例子为: http://api.douban.com/v2/user/1000001?apikey=XXX, XXX为你的apikey(非公开)

纯单IP:  150/3600 = 0.041666 = 0.041 次/s   24s/次
"""


from time import sleep

import urllib.request
from openpyxl import Workbook


def douban_spider(keyword, file_name="douban_book.xlsx"):
    """
    实例演示了如何使用豆瓣网的API 进行数据爬取
    :param keyword: 搜索关键字
    """
    url = "https://api.douban.com/v2/book/search?q={0}".format(keyword)
    # url = "https://api.douban.com/v2/book/search?q=%s" % keyword
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
    total_page = int(total / count) + 1   # 总页数

    print("每页显示书籍的数量: %d 本" % count)
    print("总计搜索到 %d 本书的信息" % total)
    print("需要爬取的总页数为 %d 页" % total_page)

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
            response = urllib.request.urlopen(url)
            sleep(5)
        except KeyboardInterrupt:
            print("没耐心了，那就不要爬了")
            break
        except Exception as e:
            print("抛出异常，自己看堆栈报错信息:")
            print(e)
            break

        # 将bytes数据流解码成string
        ebook_str = response.read().decode()

        # 将string转换成dict
        ebook_dict = eval(ebook_str)

        # 输出书籍信息
        for book in ebook_dict["books"]:
            ws.append([book["title"],
            ",".join(book["author"]),
            book["summary"],
            book["publisher"],
            book["price"]])

            # 保存为excel文件
            wb.save(file_name)

            sleep(1)      # 暂时使用增加等待时间的方案，以防被封ip，最好要用动态UA和IP代理

        print("完成写入第{0}页数据".format(start))


if __name__ == '__main__':
    print("urllib爬取豆瓣网数据示例：")
    print("启动爬虫...")

    input_keyword = input("请输入一个您要检索的关键字:\n")
    print("您输入的搜索关键词为: %s" % input_keyword)
    input_filename = input("请输入你的.xlsx文件名:\n")
    input_filename = input_filename + ".xlsx"
    print("结果将输出到%s文件中" % input_filename)
    douban_spider(input_keyword, input_filename)


