# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/18 17:20'


"""
附件格式邮件
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


def send_email_attachment():
    """
    发送附件格式邮件示例
    构建文本和html格式的邮件使用MIMEText构建--使用plain标识文本内容格式，使用html标识html内容格式
    对于附件格式则需使用MIMEMultipart
    """
    print("发送附件格式邮件示例:")

    # 邮件发送者
    sender = "grtest00@163.com"

    # 邮件接收地址列表
    # 请将xxx改为你的126邮箱名或整个改为你的目标接收邮箱地址
    receivers = "moneyfromcat@protonmail.com"  # 容易被当作垃圾邮件, QQ直接收不到

    # 发送内容构建
    # html标识发送内容为文本格式
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("[Python全栈研习社]_FullstackPentest_附件发送测试", "utf-8")

    # 构建邮件正文内容
    msg.attach(MIMEText("微信公众号：Python全栈研习社", "plain", "utf-8"))

    # 构造附件,多个附件同理
    attach1 = MIMEText(open("python3_send_text.py", 'rb').read(), "base64", "utf-8")
    attach1["Content-Type"] = "application/octet-stream"

    # 这里filename随意写，将会在邮件中显示
    attach1["Content-Disposition"] = "attrachment;filename=after_add.py"

    # 关联附件到邮件中
    msg.attach(attach1)

    # smtp服务
    smtpserver = "smtp.163.com"
    smtpport = 25

    # 发送人邮件用户名或专用于smtp账户用户名
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
    send_email_attachment()
