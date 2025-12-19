# -*- coding: utf-8 -*-
# @Auther: liyanxi
# @date  : 2025/12/10

"""
方案3：运行时动态编码检测
文件读取时的智能编码处理

ref: 有其它方案值得学习
https://yuanbao.tencent.com/chat/naQivTmsDa/1cf96c2b-69a8-41d9-b50c-337fd6985388

pip install chardet -i https://mirrors.aliyun.com/pypi/simple/

今日解析文件编码处理 todo
https://yuanbao.tencent.com/chat/naQivTmsDa/e1b1c164-c97f-4340-90b1-0b6634c31d5a
"""

import chardet
import codecs


def read_file_smart(file_path, default_encoding='utf-8'):
    """智能读取文件，自动检测编码"""
    with open(file_path, 'rb') as f:
        raw_data = f.read()

    # 检测编码
    detected = chardet.detect(raw_data)
    encoding = detected['encoding'] if detected['confidence'] > 0.7 else default_encoding

    print(f"detect encoding: {encoding}")   # debug

    try:
        if encoding == 'UTF-8-SIG':
            # 这样确实可以将GBK格式的python文件中的中文注释还原出来
            return raw_data.decode('utf-8-sig').encode('gbk', errors='ignore').decode('utf-8', errors='ignore')
            # return raw_data.decode('utf-8-sig').encode('utf-8-sig', errors='ignore').decode('utf-8', errors='ignore')
        else:
            return raw_data.decode(encoding)
    except UnicodeDecodeError:
        # 尝试常见编码
        for enc in ['utf-8', 'gbk', 'gb2312', 'latin-1']:
            try:
                return raw_data.decode(enc)
            except UnicodeDecodeError:
                continue
        # 最后尝试忽略错误
        return raw_data.decode(default_encoding, errors='ignore')


# 使用示例
# content = read_file_smart("files/gbk_demo/ssh_burst.py")
# print(content)   # encoding: UTF-8-SIG

# content2 = read_file_smart("files/utf_demo/ssh_burst.py")
# print(content2)  # encoding: utf-8

# content3 = read_file_smart("files/gb18030_demo/ssh_burst.py")
# print(content3)  # encoding: GB2312

# 这种格式semgrep检测貌似有问题，待验证
# content4 = read_file_smart("files/utf16_demo/ssh_burst.py")
# print(content4)  # encoding: UTF-16  # utf16-be




## utf-8-sig处理方式

# try:
#     data = resp.read()
#
#     # step1 用utf-8-sig解码，处理BOM
#     decoded_content = data.decode('utf-8-sig')
#
#     # step2 修复双重编码问题
#     try:
#         # 将字符串编码回GBK（恢复原始UTF-8字节）
#         recovered_bytes = decoded_content.encode('gbk', errors='ignore')
#         # 用UTF-8解码恢复的字节
#         fixed_content = recovered_bytes.decode('utf-8', errors='ignore')
#     except:
#         # 如果修复失败，使用原始解码内容
#         fixed_content = decoded_content
#
#     return {"file_content": fixed_content}
# finally:
#     resp.close()