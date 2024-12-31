#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/12/4 23:26 
# @Author : MFC

Z=[]
k=[]
Q="K78m)hm=|cwsXhbH}uq5w4sJbPrw6"
def Fun(inp):
    st=[]
    for i in range (len(inp)):
        st.append(chr(ord(inp[i])^1))
    return(''.join(st))
def FuN(inp):
    for i in range(len(inp)):
        if(i<11):
            Z.append(chr(ord(inp[i])+i+5))
        else:
            Z.append(chr(ord(inp[i])+4))
    return(''.join(Z))

def fuN(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isnumeric()):
            result+=(chr(ord(char)-1))
        elif(char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result+=(chr(ord(char)^1))
    return result

X=input("Enter input:")
k=FuN(Fun(X))   # FuN(Fun(X)) = "K78m)hm=|cwsXhbH}uq5w4sJbPrw6"
if(Q!=k):
    print("NO")
else:
    print("Flag: shaktictf{"+X+"}")