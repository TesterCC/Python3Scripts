#!/usr/bin/env python
#coding=utf-8

import csv

# csv Reader -- P266-P267    line_num获取当前行行号，但实际好像不是
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)

print(exampleData[0][0])
print(exampleData[0][1])
print(exampleData[1][1])
print(exampleReader.line_num)
print(exampleData)
print("-------------------------------")

for row in exampleData:
    print('Row: '+ str(exampleReader.line_num) + ' ' + str(row))   # something error
