import base64
import gzip
from hashlib import md5
import urllib.request

from ctf_writeup.hacking8.aes import AESModeOfOperationCTR

print("一个简单的编程游戏！一共有4题，全部回答完成，即挑战成功。")
exec(urllib.request.urlopen("http://i.hacking8.com/static/aes.py").read().decode())
def Decrypt(key: str, text: str) -> str:
    if len(key) < 32:
        key += ' ' * (32 - len(key))
    elif len(key) > 32:
        key = key[0:32]
    aes = AESModeOfOperationCTR(key.encode())
    s = gzip.decompress(aes.decrypt(base64.b64decode(text)))
    print("[DEBUG] ", str(s, encoding='utf-8'))
    return str(s, encoding='utf-8')
print("第一关:计算结果 1+1=？")
while True:
    key = input("请输入答案:")
    try:
        exec(Decrypt(key, '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'))
        break
    except KeyboardInterrupt:
        raise
    except:
        print("[x] 抱歉，答案错误")