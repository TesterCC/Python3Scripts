# coding=utf-8
"""
DATE:   2022/5/24
AUTHOR: TesterCC
"""

"""
5.1 读写文本数据

问题：读写各种不同编码的文本数据。如ASCII，UTF-8或UTF-16编码等。

解决方案：
使用rt模式的open()函数读取文本文件。

当读取一个未知编码的文本时使用latin-1编码永远不会产生编码错误。即使不能产生完全正确的文本解码数据，但是它也能从中提取出足够多的有用数据。
如果将数据写回去，原先的数据还是会保留。

对于文本处理，首要原则是确保你总是使用的是正确编码。当摸棱两可时，就使用默认的设置（通常为UTF-8）
"""
# 读取整个文件内容到一个字符串中
# with open('test.txt','rt') as f:
with open('test.txt','rt', encoding="latin-1") as f:
    data = f.read()

print(len(data),type(data),data)


# 迭代每一行
# 加errors参数忽略错误，除非必要尽量少用
with open('test.txt','rt', encoding="ascii", errors="ignore") as f:
    for line in f:
        print(line)

# print(type(f))
