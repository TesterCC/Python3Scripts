#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/3 11:50 
# @Author : MFC

"""
攻防世界 crypto 004 不仅仅是Morse
"""

import re

# 密文转化为指定格式
s = 'AAAAABAABBBAABBAAAAAAAABAABABAAAAAAABBABAAABBAAABBAABAAAABABAABAAABBABAAABAAABAABABBAABBBABAAABABABBAAABBABAAABAABAABAAAABBABBAABBAABAABAAABAABAABAABABAABBABAAAABBABAABBA'
a = s.lower()

# 字典  “培根密码”（Bacon's cipher）
CODE_TABLE = {
    'a':'aaaaa','b':'aaaab','c':'aaaba','d':'aaabb','e':'aabaa','f':'aabab','g':'aabba',
    'h':'aabbb','i':'abaaa','j':'abaab','k':'ababa','l':'ababb','m':'abbaa','n':'abbab',
    'o':'abbba','p':'abbbb','q':'baaaa','r':'baaab','s':'baaba','t':'baabb','u':'babaa',
    'v':'babab','w':'babba','x':'babbb','y':'bbaaa','z':'bbaab'
}

# 5个一组进行切割并解密
def baconsdecode(peigen):
    msg =''
    codes = re.findall(r'.{5}', a)
    for code in codes:
        if code =='':
            msg += ' '
        else:
            UNCODE =dict(map(lambda t:(t[1],t[0]),CODE_TABLE.items()))
            msg += UNCODE[code]
    return msg

flag = baconsdecode(a)
print('flag is ',flag)