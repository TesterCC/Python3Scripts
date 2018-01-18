# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/18 12:54'


"""
文本邮件示例
https://mp.weixin.qq.com/s?__biz=MzI0NDQ5NzYxNg==&mid=2247484068&idx=1&sn=dd5626cdad7815143b38d77e2db34cf8&scene=19#wechat_redirect
"""

import smtplib
from email.mime.text import  MIMEText
from email.header import Header


def send_email_text():
    print("发送文本邮件示例")

    # 邮件发送者
    sender = "grtest00@163.com"

    # 邮件接收地址列表
    # 请将xxx改为你的126邮箱名或整个改为你的目标接收邮箱地址
    receivers = "moneyfromcat@protonmail.com"    # 容易被当作垃圾邮件, QQ直接收不到

    # 发送内容构建
    # text标识发送内容为文本格式
    msg = MIMEText("Hello All, \n测试开发邮件－－测试专用", "plain", "utf-8")
    msg["From"] = sender
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("[测试]邮件测试，请忽略", "utf-8")

    # smtp服务
    smtpserver = "smtp.163.com"
    smtpport = 25

    # 发送人邮件用户名或专用于smtp账户用户名  邮件名
    username = "grtest00@163.com"

    # 发送人邮件密码或专用于smtp账户的密码
    password = "123456xx"   # 授权码即可

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 连接到smtp服务
    con = smtp.connect(smtpserver, smtpport)
    print("连接结果： ", con)

    # 登录smtp服务
    log = smtp.login(username, password)
    print("登录结果：", log)

    # 发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果： ", res)

    # 退出
    smtp.quit()
    print("send email finish")


if __name__ == '__main__':
    send_email_text()
