#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/5/22 01:34'

"""
用Flask实现短网址功能应用
pip install -i https://pypi.douban.com/simple/ flask flask-mysqldb flask-redis

具体实现内容：
- 代码里实现了短网址生成算法
- 数据库使用mysql
- 计数器使用Redis

需要补充的：短网址还原为长网址的前后端代码
"""

import os

from flask import Flask,jsonify,render_template,request
from flask_mysqldb import MySQL
# from flask.ext.redis import FlaskRedis  # 可能是新安装包改了导入路径
from flask_redis import FlaskRedis

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWD')   # 写在本地环境变量中
app.config['MYSQL_DB'] = 'testdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['REDIS_URL'] = f"redis://:{os.getenv('REDIS_PASSWD')}@localhost:6379/2"  # 需要启动redis

mysql = MySQL(app)
redis_store = FlaskRedis(app)

CHARS="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

DOMAIN_NAME = 'http://127.0.0.1:5000/'  # 最好能写成动态获取，http://127.0.0.1:5000/替换为短网址服务域名

def encode(num):
    # 10进制->62进制
    if num == 0:
        return CHARS[0]
    res = []   # 保存二进制串的列表
    while num:
        num, rem = divmod(num, len(CHARS))   # 对 CHARS的长度62  取余数,rem表示余数，num表示商
        res.append(CHARS[rem])
    return ''.join(reversed(res))

# 生成短网址逻辑
@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['url']
    long_url = long_url.replace("*","").replace(" ","")   # 做简单的输入判断和过滤，这里仅举例，还不够全面
    if not long_url:
        return jsonify({"url":"输入的url为空"})
    index = int(redis_store.incr('SHORT_CNT'))    # 获取自增index, 因为第一次会会返回1，所以没有使用到短网址为a
    token = encode(index)   # 10进制->62进制
    sql = 'INSERT INTO short_url(token,url) VALUES(%s,%s)'  # 这种写法要注意防止sql注入
    cur = mysql.connection.cursor()
    cur.execute(sql,(token, long_url))
    mysql.connection.commit()
    short_url = f'{DOMAIN_NAME}' + token
    return jsonify(url=short_url)  # 返回短网址的json数据

@app.route('/')
def index():
    return render_template('index.html')  # html模版放在templates目录下

if __name__ == '__main__':
    app.run(debug=True)
