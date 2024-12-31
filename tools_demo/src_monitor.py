#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-10-29 21:59'

# 简单的SRC监控脚本

import requests
import time
import json
import smtplib
from email.mime.text import MIMEText
header = {
    "Host": "www.butian.net",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "21",
    "Origin": "https://www.butian.net",
    "Referer": "https://www.butian.net/Reward/plan",
    "Cookie": "ccxxxxxxxxxxxxxxxxx",# cookie用自己的
    "X-Forwarded-For": "2.2.30.112"
}
data = {"s":"3","p":"1","sort":"1","token":""}
def sendmail(differ):
    mail_host = 'smtp.163.com'
    #163用户名
    mail_user = 'xxxx@163.com'
    #密码(部分邮箱为授权码)
    mail_pass = 'xxxxxx'
    #邮件发送方邮箱地址
    sender = 'xxxxxx@163.com'
    #邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['xxxxx@163.com', #这里第一个一定要注意，如果你是使用163邮箱，最好第一个收件人填自己，给自己发一份。不然会被其他邮箱拒收。
                 'xxxxxx@qq.com', #
                 ]

    #设置email信息
    #邮件内容设置
    message = MIMEText('新的src上线，请快快查看%s' % (str(differ)),'plain','utf-8')
    #邮件主题
    message['Subject'] = '新的src上线'
    #发送方信息
    message['From'] = sender
    #接受方信息
    message['To'] = receivers[0]

    #登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        #连接到服务器
        smtpObj.connect(mail_host,25)
        #登录到服务器
        smtpObj.login(mail_user,mail_pass)
        #发送
        smtpObj.sendmail(
            sender,receivers,message.as_string())
        #退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error',e) #打印错误



def main():
    url = 'https://www.butian.net/Reward/corps'
    response = requests.post(url, data, headers=header)
    old_json  =json.loads(response.text)
    while True:
        time.sleep(5)
        try:
            response = requests.post(url,data,headers=header)
            jsonstr = json.loads(response.text)
            differ = [v for v in jsonstr['data']['list'] if v not in old_json['data']['list']]
            if len(differ):
                sendmail(differ)
            elif len(differ) == 0:
                old_json = jsonstr
            print("正在监控")
        except Exception as e:
            print("error")
            continue

if __name__ == '__main__':
    main()