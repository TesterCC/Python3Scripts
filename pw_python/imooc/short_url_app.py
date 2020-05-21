#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2020/5/22 01:34'

"""
用Flask实现短网址功能应用
pip install -i https://pypi.douban.com/simple/ flask flask-mysqldb flask-redis
"""

import os

from flask import Flask,jsonify,render_template,request
from flask_mysqldb import MySQL
# from flask.ext.redis import FlaskRedis  # 可能是新安装包改了导入路径
from flask_redis import FlaskRedis

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWD')
app.config['MYSQL_DB'] = 'testdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['REDIS_URL'] = f"redis://:{os.getenv('REDIS_PASSWD')}@localhost:6379/2"

mysql = MySQL(app)
redis_store = FlaskRedis(app)

CHARS="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# todo main logic    10-2 19:35
@app.route('/shorten', methods=['POST'])
def shorten_url():
    pass

@app.route('/')
def index():
    return render_template('short_url_index.html')  # html模版放在templates目录下

if __name__ == '__main__':
    app.run(debug=True)
