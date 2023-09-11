# -*- coding: utf8 -*-
from flask import Flask, request

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    # 获取名为 'file' 的文件列表，这里假设前端表单中的文件字段名为 'file'。你可以根据实际情况修改字段名。
    files = request.files.getlist('file')
    for file in files:
        # 保存文件或执行其他处理操作
        save_file_path = "./upload_file/" + file.filename
        print(f"[D] save file path: {save_file_path}")
        file.save(save_file_path)
    return 'Files uploaded successfully!'


if __name__ == '__main__':
    app.run()
