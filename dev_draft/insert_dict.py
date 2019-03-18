#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-03-15 15:41'

import datetime

html_loop_template = '''<tr>
                                <td>{ticket_name}</td>
                                <td>{current_price}</td>
                                <td>{origin_price}</td>
                                <td>{price_description}</td>
                            </tr>'''


event_content_dict = {'content': ''}
# print(event_content_dict)
# print(html_template.format(ticket_name="1",current_price="2",origin_price="3",price_description="4"))

ticket_list = [{'status': 1,
  'limit_people': '1',
  'original_price': None,
  'stock': 100,
  'price': 0,
  'rank': 1,
  'content': 'free',
  'is_free_vip': 0,
  'begin_time': '2018-10-08 16:27',
  'property': 'free',
  'vip_free_count': -1,
  'id': 225831,
  'end_time': '2019-03-13 18:00'},
 {'status': 1,
  'limit_people': '1',
  'original_price': None,
  'stock': 999,
  'price': 0.01,
  'rank': 1,
  'content': '1129',
  'is_free_vip': 0,
  'begin_time': '2018-11-29 08:00',
  'property': 'test',
  'vip_free_count': -1,
  'id': 229535,
  'end_time': '2019-03-26 17:00'},
 {'status': 1,
  'limit_people': '1',
  'original_price': None,
  'stock': 999,
  'price': 2.22,
  'rank': 1,
  'content': 'test2',
  'is_free_vip': 0,
  'begin_time': '2018-07-07 08:00',
  'property': '会务费',
  'vip_free_count': -1,
  'id': 232648,
  'end_time': '2019-03-12 17:00'},
 {'status': 1,
  'limit_people': '1',
  'original_price': 66,
  'stock': 999,
  'price': 33,
  'rank': 1,
  'content': '',
  'is_free_vip': 0,
  'begin_time': '2019-02-14 08:00',
  'property': '早鸟票',
  'vip_free_count': -1,
  'id': 232882,
  'end_time': '2019-02-27 17:00'},
 {'status': 1,
  'limit_people': '1',
  'original_price': None,
  'stock': 999,
  'price': 10,
  'rank': 1,
  'content': '',
  'is_free_vip': 0,
  'begin_time': '2019-03-05 08:00',
  'property': '会务费',
  'vip_free_count': -1,
  'id': 233922,
  'end_time': '2019-03-29 17:00'}]

current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

html_loop = [html_loop_template.format(ticket_name=ticket.get("property"),current_price=ticket.get("price"),origin_price=ticket.get("original_price"),price_description=ticket.get("content")) for ticket in ticket_list if ticket.get("end_time") > current_time]


html_loop_str = ''.join(html_loop)


html_template_str = '''<table border="1" cellpadding="1" cellspacing="1" style="width:500px">
    <tbody>
        <tr>
            <td>票种名称</td>
            <td>价格</td>
            <td>原价</td>
            <td>票价说明</td>
        </tr>
''' + html_loop_str + '''
    </tbody>
</table>
'''

# print(html_loop_str)

print("*"*80)

print(html_template_str)