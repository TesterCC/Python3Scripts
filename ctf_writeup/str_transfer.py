#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/12/26 10:10 
# @Author : MFC

import sys


def encode_string2base():
    """
    这个函数的功能是将字符串转换成以0b、0o、0d、0x为首的二、八、十、十六进制的数据
    """
    str_input = input("请将需要转换的字符串输入: ")
    result = ''
    for i in range(len(str_input)):
        key = ord(str_input[i])
        if key % 4 == 0:
            result += str(bin(key)) + " "
        elif key % 4 == 1:
            result += str(oct(key)) + " "
        elif key % 4 == 2:
            result += "0d" + str(key) + " "
        elif key % 4 == 3:
            result += str(hex(key)) + " "
        else:
            pass
    print("字符串转二、八、十、十六进制的结果是：", result)


def decode_base2basestring():
    """
    这个函数的功能是将以0b、0o、0d、0x为首的各种格式的数据转换成字符串
    :return:
    """
    s = input("请将以0b、0o、0d、0x为首的各种格式的数据输入：")
    keys = s.split(" ")
    result = ""
    for key in keys:
        if key[0:2] == '0b':
            result += str(chr(int(key[2:], 2)))
        elif key[0:2] == '0o':
            result += str(chr(int(key[2:], 8)))
        elif key[0:2] == '0x':
            result += str(chr(int(key[2:], 16)))
        elif key[0:2] == '0d':
            result += str(chr(int(key[2:])))
        else:
            result += ""
    print("各种进制转换为字符串的结果是:", result)
    s = result
    result1 = ""
    result2 = ""
    result3 = ""
    result4 = ""
    for key in s:
        result1 += str(bin(ord(key))) + " "
        result2 += str(oct(ord(key))) + " "
        result3 += str(hex(ord(key))) + " "
        result4 += str(ord(key)) + " "
    print("字符串转二进制的结果是：\t", result1)
    print("字符串转八进制的结果是：\t", result2)
    print("字符串转十进制的结果是：\t", result4)
    print("字符串转十六进制的结果是：\t", result3)


def strings2bases():
    """
    这个函数的功能是将字符串转换成二、八、十六进制输出出来
    :return:
    """
    s = input("请将您想转换的字符串输入：")
    result1 = ""
    result2 = ""
    result3 = ""
    result4 = ""
    for key in s:
        result1 += str(bin(ord(key))) + " "
        result2 += str(oct(ord(key))) + " "
        result3 += str(hex(ord(key))) + " "
        result4 += str(ord(key)) + " "
    print("字符串转二进制的结果是：\t", result1)
    print("字符串转八进制的结果是：\t", result2)
    print("字符串转十进制的结果是：\t", result4)
    print("字符串转十六进制的结果是：\t", result3)


def num2bases():
    """这个函数的功能十将数字转换成各种进制"""
    res1 = ""
    res2 = ""
    res3 = ""
    try:
        s = int(input("请输入十进制的数据："))
    except:
        print("您的输入我好像不太能理解，请再重新尝试一下吧。")
    else:
        print("您的输入是：", s)
        print("对应的二进制是：", bin(s))
        print("对应的八进制是：", oct(s))
        print("对应的十六进制是：", hex(s))


def menu():
    print("*" * 80)
    print("*\t\t（1）将字符串转换成二、八、十、十六进制的形式                          *")
    print("*\t\t（2）将二、八、十、十六进制的形式转换成字符串并显示各种形式的进制      *")
    print("*\t\t（3）将字符串转换成各种单独的进制形式                                  *")
    print("*\t\t（4）将数字转换成各种单独的进制形式                                    *")
    print("*" * 80)


def run_system():
    while True:
        menu()
        user_choice = input("Please input the number you want to operate: ")
        if user_choice == '1':
            encode_string2base()
            print("")
        elif user_choice == '2':
            decode_base2basestring()
            print("")
        elif user_choice == '3':
            strings2bases()
            print("")
        elif user_choice == '4':
            num2bases()
            print("")
        elif user_choice == 'q':
            sys.exit()
        else:
            print("您的输入看起来我好像理解不了，请重新尝试一下吧\n")


run_system()