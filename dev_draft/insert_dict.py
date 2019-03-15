#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-15 15:41'


html_template = '''<table border="1" cellpadding="1" cellspacing="1" style="width:500px">
    <tbody>
        <tr>
            <td>票种名称</td>
            <td>价格</td>
            <td>原价</td>
            <td>票价说明</td>
        </tr>
        <tr>
            <td>{ticket_name}</td>
            <td>{current_price}</td>
            <td>{origin_price}</td>
            <td>{price_description}</td>
        </tr>
    </tbody>
</table>
'''

test_dict = {'content': ''}
print(test_dict)
# print(html_template.format(ticket_name="1",current_price="2",origin_price="3",price_description="4"))


test_dict['content'] = html_template.format(ticket_name="1",current_price="2",origin_price="3",price_description="4")
print(test_dict)