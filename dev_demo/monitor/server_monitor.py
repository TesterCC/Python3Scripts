# coding=utf-8
"""
DATE:   2021/1/19
AUTHOR: Yanxi Li
"""
import os
import socket
import smtplib
import traceback
from email.mime.text import MIMEText
from email.header import Header
import time

# func: 监控端口服务是否存在，线上服务是否宕机
# ref: https://zuiseng.com/496.html
# P.S: 已测试，挺稳定的

monitor_target = ['10.0.4.141:8600']

# run in CentOS
cmd_get_ip = "ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d 'addr:'"
local_ip = os.popen(cmd_get_ip).read()
local_ip = local_ip.replace('\n', '')
print(local_ip)


def get_ip_status(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((ip, port))
        return True
    except Exception as e:
        return False
    finally:
        server.close()


def send_mail(content):
    # 替换 @yyy.com 相关内容
    mail_host = "smtp.exmail.qq.com"
    mail_user = "xxx@yyy.com"     # username
    mail_pass = "-"               # password
    mail_res = ["t0@yyy.com", "t1@yyy.com"]

    sub = time.strftime("%Y-%m-%d", time.localtime())

    sender = "xxx@yyy.com"  # 也可以和mail_user一致
    msg = MIMEText(content, _subtype='plain')
    msg['Subject'] = sub + '服务器宕机日常检测'
    msg['From'] = Header("CRM_Monitor", 'utf-8')
    msg['To'] = Header(mail_res[0], 'utf-8')

    s = smtplib.SMTP(mail_host, 25)
    s.starttls()
    s.login(mail_user, mail_pass)
    s.sendmail(sender, mail_res, msg.as_string())
    s.close()


def main_monitor():
    global monitor_target
    message = ""

    print("[TEST] monitor_target: ", monitor_target)
    for line in monitor_target:
        ip = line.split(':')[0]
        port = int(line.split(':')[1])

        if (get_ip_status(ip, port)):
            pass
        else:
            # print("服务器 【{}】上，服务【{}】 的服务宕机了 ".format(local_ip, line))
            message += "\n服务器 【{}】，目标服务【{}:{}】 宕机了".format(local_ip, ip, port)

    if (len(message) > 4):
        send_mail(message)
        print("[*] 被监控服务宕机，告警通知邮件已发送成功")
    else:
        # send_mail("一切正常，请放心")
        print("[*] 被监控服务正常运行中……")


if __name__ == '__main__':
    count = 0
    while True:
        time.sleep(15)

        count += 1

        try:
            main_monitor()

        except:
            traceback.print_exc()

        print("[TEST] finish server check", count, 'times ...')
