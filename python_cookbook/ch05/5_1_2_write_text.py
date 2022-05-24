# coding=utf-8
"""
DATE:   2022/5/24
AUTHOR: TesterCC
"""

"""
5.1 读写文本数据

问题：读写各种不同编码的文本数据。如ASCII，UTF-8或UTF-16编码等。

解决方案：
使用wt模式的open()函数写入文本文件。再次执行会清空文件重新写入。
追加文本内容写入使用at模式。

Python支持非常多尔的文本编码，常见编码是：ascii，latin-1,utf-8和utf-16.
Web应用程序中通常使用的是UTF-8
当读取一个未知编码的文本时使用latin-1编码永远不会产生编码错误。即使不能产生完全正确的文本解码数据，但是它也能从中提取出足够多的有用数据。
如果将数据写回去，原先的数据还是会保留。

不使用with的话需要手动关闭文件。
"""
text1 = "aaa"
text2 = "测试"
text3 = "2022"

# 注意：文件读写默认使用系统编码，可以调用函数获取到。
import sys
print(sys.getdefaultencoding())

# 如果知道读写文本的编码方式，可以指定编码参数 encoding。
with open('somefile.txt','wt',encoding='utf-8') as f:
# with open('somefile.txt','at',encoding='utf-8') as f:
    f.write(text1)
    f.write(text2)
    f.write(text3)