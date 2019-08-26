# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '2019-08-23 11:41'

import datetime

def format_price_time(price_units):
    new_price_units = []
    for p in price_units:
        price_end_time = datetime.datetime.strptime(p['end_time'], '%Y-%m-%d %H:%M')
        now = datetime.datetime.now()
        delta = price_end_time - now
        day = delta.days
        if day <= 5:
            seconds = delta.seconds
            h = seconds / (60*60)
            # m = (second - h*60*60) / 60
            count_down = '{}天{}小时'.format(str(day), str(h))
            p['count_down'] = count_down
        else:
            p['count_down'] = ''
        if price_end_time > datetime.datetime.now():
            new_price_units.append(p)
    return new_price_units


def format_delta_days(start_time):
    now = datetime.datetime.now()
    delta = start_time - now
    delta_day = delta.days
    return delta_day

if __name__ == '__main__':
    ret = format_delta_days(datetime.datetime.now()+ datetime.timedelta(days=44))
    print(ret)
    ret = format_delta_days(datetime.datetime.now()+ datetime.timedelta(days=44, hours=3))
    print(ret)