# -*- coding: utf8 -*-
from flask import Flask, Response, send_file, request

app = Flask(__name__)


# http://localhost:3001/user/download?id=7
# test by vue.js simple crud demo
# project go_curd_demo by gin also implement the function

@app.route('/user/download', methods=['GET'])
def download_file():
    tid = request.args.get('id')
    print(f"tid: {tid}, {type(tid)}")
    if tid != "7":
        return {}
    # 读取文件a.json的内容
    with open('./data.json', 'rb') as f:
        file_data = f.read()

    # 指定响应头，告诉浏览器下载文件，并指定文件名为b.json
    response = Response(file_data, content_type='application/json')
    response.headers['Content-Disposition'] = 'attachment; filename=d.json'

    return response


if __name__ == '__main__':
    app.run(debug=True, port=3001)
