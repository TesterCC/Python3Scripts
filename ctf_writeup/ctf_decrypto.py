# coding=utf-8

# https://adworld.xctf.org.cn/task/answer?type=web&number=3&grade=1&id=5326&page=1

miwen="a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws"

import base64

# ROT13字符变换，要变回原顺序再调用一次即可。
def rot13(s, OffSet=13):
    def encodeCh(ch):
        f = lambda x: chr((ord(ch) - x + OffSet) % 26 + x)
        return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)

    return ''.join(encodeCh(c) for c in s)

# 解密要从外到内处理，代码处理顺序   rot13 ->  逆strrev  ->  base64_decode
miwen = rot13(miwen)                # 1.ROT13字符变换，要变回原顺序再调用一次即可。
miwen = miwen[::-1]                 # 2.字符串逆向
miwen = base64.b64decode(miwen)     # 3.base64_decode, 注意返回的是bytes类型，需要转str。
miwen = str(miwen, 'utf-8')
print(miwen)

# 然后进行 ASCII 的转码处理
plain_text = ""
for _0 in range(0, len(miwen)):
    _c = ord(miwen[_0])
    tmp = (_c) - 1
    plain_text += (chr(tmp))
print(plain_text[::-1])


