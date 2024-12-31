#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-05-17 11:57'

"""
题目：
轻微改变图片中像素的RGB值，肉眼无法察觉
将8bit R/G/B中的最低1bit，用于隐藏一 个数据文件（如文本）
每3个像素可以隐藏1个字节
注意使用不失真图像格式  BMP／PNG格式
要求：
1）提供图片和数据文件，生成隐藏信息的图片
2）从隐藏信息的图片中提取数据文件

做这个必须弄清楚原理，不然无从下手：

1.图片都由像素组成，一个字节=8位   1 byte = 8 bits
2.一个像素包含红绿蓝（RGB）三个颜色通道的值，最小值为0，用二进制表示为0b00000000，0b是前缀，代表后面的数字是二进制。
最大值为255，用二进制表示为0b11111111，0b后面的8位数字，即一个字节，就代表了颜色的值。一个像素有3个字节。
3.获取一个像素的数据，我们就可以得出(R,G,B)的值，如(67, 140, 255)，我们把数字转化为二进制(0b1000011, 0b10001100, 0b11111111)。
4.对人的肉眼来说，颜色值差1，是看不出区别的。如颜色值255，和254，254的二进制为0b11111110。我们就可以利用最后一位数字来隐藏信息。
这样，一个像素就能存3位（取RGB各最后一位），那么我要存一个字节的信息，需要8位，可知起码需要3个像素才能保存一个字节的信息
5.我把想隐藏的信息化成二进制，假设0b10101010，把0b后面的每一位数字都依次替换到每一个像素的RGB最后一位里，则达到了隐藏信息的目的。
要提取时，直接取像素的RGB值里的最后一个数字，再重新组合成信息，就达到了解密的效果。

REF:
1)https://blog.csdn.net/byakki/article/details/86771836

解题思路：
最基本的，只能存英文和数字，加密信息不能超过255长度，因为我只用8位来保存信息，取信息时也是8位8位的取。
如我要写入’i love you’, 这个共有10个字符。那么我的前8位纪录的就是二进制的10
(没成功)


2)https://blog.csdn.net/gaoapp/article/details/70942478
(有提取代码，但一般建议直接上工具)

LSB 中文名字全称为最低有效位。
常见的信息隐藏图片格式一般为png或者bmp这类无损压缩的图片且是8位图或者24位图，8位图是使用我们的调色板

（实际上，最后3位我们都可以进行改变且我们同样从肉眼看不出其变化，甚至最后5位，6位的改变我们都可以看出图片的大致样子，也就是说最低有效位，我们隐藏的信息是可以放到每个像素字节的后3位，不仅仅是最后一位）

PS:代码运行报错，仅做参考
"""

from PIL import Image

# 将数据写入图片的步骤

image = Image.open('bk.bmp')
strings = 'i love you'

'''
信息加密
'''
def encodeimg(image,strings):
	# 先计算要写入的数据会占用多少个像素，RGB，3个像素装一个字节
    n = (len(strings) + 1) * 3  # 需要n个像素，第一个纪录共有多少数据量
    rgblst = list(image.getdata())[:n]  # 得到图片的RGB，只取所需要的像素

    # 进行位移计算，把二进制最后一位都变0
    rlst = [(r >> 1 << 1, g >> 1 << 1, b >> 1 << 1) for (r, g, b) in rgblst]
    # binevenpix = [(bin(r), bin(g), bin(b)) for (r, g, b) in rlst]  # 转换成二进制

    # 将要写入的数据，字符串换成二进制
    firstdata = bin(len(strings)).lstrip('0b').zfill(8)  # 先计算数据的长度，放在最前面的
    # 返回一串二进制字符串
    binary = firstdata + ''.join([bin(ord(c)).lstrip('0b').zfill(8) for c in strings])

    # 将要写入的数据，写进图片并保存
    # a = evenpix    # 待写入的位置
    # b = binary  # 待写入的数据
    c = 0
    t = ()  # 元组
    z = []  # 中转列表
    l = []  # 最后列表
    for i in rlst:
        for j in i:
            if c == len(binary):
                z.append(j)
            else:
                z.append(j + int(binary[c]))
                c = c + 1
            t = tuple(z)
        l.append(t)
        z = []
        t = ()

    image.putdata(l)
    return image

'''
解密图片，先获得数据长度
'''

# 获得图片数据
def decodeimg(image):
    # 先得到头3个像素，获取数据量
    rgblst = list(image.getdata())[:3]
    # 先右位移再左位移，如果跟原来的数字相等，说明其二进制尾数是0，返回False,否则返回True
    binary = ''.join(
        [str(int(r >> 1 << 1 != r)) + str(int(g >> 1 << 1 != g)) + str(int(b >> 1 << 1 != b)) for (r, g, b) in
         rgblst])
    length = int(binary[:8], 2)  # 求出数据量了
    # 所需数据的位
    datalength = (length + 1) * 8
    # 把隐藏数据的像素列举出来
    codelst = list(image.getdata())[:datalength // 3 + 1]
    #
    binary2 = ''.join(
        [str(int(r >> 1 << 1 != r)) + str(int(g >> 1 << 1 != g)) + str(int(b >> 1 << 1 != b)) for (r, g, b) in
         codelst])
    binaryfinal = binary2[8:datalength]
    # 将获得的数据，从二进制变成字符串
    decodetxt = ''
    for ch in range(0, len(binaryfinal), 8):
        decodetxt += chr(int(binaryfinal[ch:ch + 8], 2))
    return decodetxt

# 加密并保存为新图片
encodeimg(image,strings).save('bkx.bmp')    # run and report error
# 对新图片解码
print(decodeimg(Image.open('bkx.bmp')))
