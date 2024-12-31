#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/22 22:56'


"""
字符串
https://note.youdao.com/web/#/file/WEB98c227493cf921f71d8b69ba93cef80d/note/WEB7f0ac39f04ec94e91ae095d9fadcc620/
在python3中，所有的字符串都是Unicode编码
strip
"""

if __name__ == "__main__":
    # 去字符串空格示例
    demo_str = "  我的前  后 和 中 间  都有空格  "
    print(demo_str)

    # 去除前面的空格
    lstr = demo_str.lstrip()
    print(lstr)

    # 去除后面的空格
    rstr = demo_str.rstrip()
    print(rstr)

    # 去除前后的空格
    str = demo_str.strip()
    print(str)