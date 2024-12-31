# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/1/31 05:37'


"""
day2  04 无法绕过的json解析
加深:在完成上文的练习的基础上，自己封装一个json解析通用类
扩展:找不同的json解析库，练习并熟练其基本使用方法
"""

import json


class JsonTool(object):

    def __init__(self, filename):
        self.filename = filename

        # if isinstance(self.filename, list):
        #     self.list2jsonstr()
        # elif isinstance(self.filename, json):
        #     self.read_json()
        # else:
        #     pass

    def python2jsonstr(self):
        """
            实例演示的都是在内存中进行
            将python对象 转化为 json str
        """
        print("python list转化为json串格式化实例:")

        data = self.filename

        json_data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

        # 打印格式化的json串, json是str类型
        print(json_data)

    def read_json(self):
        """
        演示如何读取json_data.json的内容转化python对象
        """
        print("Python读取json内容文件转化成Python对象实例:")
        print("读取文件: %s" % self.filename)

        fp = open(self.filename, 'r')

        json_data = json.load(fp)  # 将已编码的json字符串解码为Python对象

        print(type(json_data))
        print(json_data)

        fp.close()

        return json_data

    def write_json(self, json_data, newfilename):
        """
        将python对象转化存json串存入文件
        """
        print("python写入json串实例")

        data = json_data

        with open(newfilename, 'w') as fp:
            json.dump(data, fp, sort_keys=True, indent=4, separators=(',', ': '))

        fp.close()
        print("文件已写入到: %s" % newfilename)


if __name__ == '__main__':
    jt = JsonTool("json_httpbin.json")
    data = jt.read_json()
    jt.write_json(data, "json_httpin1.json")

