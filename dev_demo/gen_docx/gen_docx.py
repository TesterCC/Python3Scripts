# coding=utf-8
"""
DATE:   2020/10/23
AUTHOR: Yanxi Li
"""
# pip install docxtpl
import docxtpl

# read template docx
# 需要自定义 template.docx 文件模板
docx = docxtpl.DocxTemplate('template.docx')

# set value
context_map = {
    't1':'产品授权',
    't2':'XXXXX公司',
    't3':'XXXXX软件基础版',
    't4':'1',
    't5':'2019-07-18',
    't6':'3',
    't7':'ASSS-BCCC-77AA-88BB',
    't8':'2020-08-18',
}

# render
docx.render(context_map)

# save
docx.save('test.docx')
