# coding=utf-8
# 20211220
import os
import re
import sys
import time
import json
import traceback
import hashlib
import bson

sys.path.append('/opt/sensor')
import sensor

if len(sys.argv) > 1:
    log_name = sys.argv[1]
else:
    log_name = "log_all"

try:
    # unknown_log_path = '/opt/sensor/log_unknown'
    # # 改成备份日志位置
    # unknown_log_path = '/tmp/log_backup'
    # if not os.path.isdir(unknown_log_path):
    #     os.mkdir(unknown_log_path)

    with open('/opt/sensor/convert.json') as f:
        config = json.load(f)
    rule_list = config['rule']
    convert_speed = int(config['speed'])
    filter_map = config['filter']

except:
    traceback.print_exc()
    sys.exit()

# print(f"rule_list: {rule_list}")
# print(f"convert_speed: {convert_speed}")
# print(f"filter_map: {filter_map}")

# timestamp13to10 和数据库时间戳一致
# compute_md5
# convert
# check_convert_speed
# check_filter

def timestamp13to10(timeNum):
    # 13位时间戳转10位时间戳
    # 输入毫秒级的时间(13位时间戳)，转出正常格式的str时间
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # print(otherStyleTime)

    # 将"2011-09-28 10:00:00"转化为时间戳(10位时间戳)
    return int(time.mktime(time.strptime(otherStyleTime,'%Y-%m-%d %H:%M:%S')))

def compute_md5(data):
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()


_id_count = 0
_id_count_time = int(time.time())
k_list = ['id', 'src', 'dst', 'protocol', 'sport', 'dport']
risk_map = {'1': 'low', '2': 'medium', '3': 'high', '4': 'high'}


def convert(log, log_time):
    global _id_count, _id_count_time
    global k_list, risk_map

    ae = None
    ba_map = sensor.init_ba_map()
    for rule in rule_list:
        if 'flag' not in rule or rule['flag'] not in log:
            continue

        # convert
        ae = {'time': log_time}
        for k in k_list:
            ae[k] = '-'
            k_rule = rule.get(k, None)

            try:
                if isinstance(k_rule, list) and len(k_rule) == 2:
                    ae[k] = sensor.get_field(log, k_rule[0], k_rule[1])
                elif isinstance(k_rule, str) and k_rule != '':
                    ae[k] = re.search(k_rule, log).group(0)
            except:
                ae[k] = '-'

        ae['device'] = rule.get('device', '-')
        ae['desc'] = log
        if not ae['id'].isdigit():
            ae['id'] = compute_md5(ae['id'])
        ae['id'] = ae['device'] + '-' + ae['id']

        _id_count += 1
        if time.time() > _id_count_time + 1:
            _id_count = 0
            _id_count_time = int(time.time())
        ae['_id'] = '%s:%d:%d' % (sensor.id, _id_count_time, _id_count)

        ba_id = ba_map.get(ae['id'], {}).get('ba_id', '-')
        ae['risk'] = risk_map.get(ba_id[0], 'low')
        ae['ba_id'] = ba_id[:3]

        break

    else:
        # # write reply unknown log
        # file_name = '/tmp/reply_log_unknown/%s' % time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # with open(file_name, 'a') as f:
        #     f.write(log + '\n')
        pass

    return ae


ae_count = 0
ae_count_time = time.time()


def check_convert_speed():
    global convert_speed
    global ae_count
    global ae_count_time

    if time.time() > ae_count_time + 1:
        ae_count_time = time.time()
        ae_count = 0

    ae_count += 1
    if ae_count >= convert_speed:
        return False

    return True


def check_filter(ae):
    global filter_map

    # if ae == None or ae['src'] == '-' or ae['dst'] == '-':
    if ae == None:
        return True

    for k in filter_map:
        if ae[k] in filter_map[k]:
            return True

    return False


# 这里的data源自kafka，但是我要把log的来源改成文件读取
# 1. get all backup log    sort merge  # todo要读其它文件改这里
with open('/tmp/log_backup/{}'.format(log_name), 'r') as f:
    logs = f.readlines()

# 2. convert backup log to ae
# 3. send sensor log

print(f"sensor log_topic: {sensor.ae_topic}")
# topic_list = [sensor.log_topic]


for log in logs:
    try:
        # data = '1638933060067 {"code":""}'
        msg_time = re.search(r"\d{13}\s", log).group().strip()
        # 读取的为13位时间戳，需要转成10位时间戳
        log_time = timestamp13to10(int(msg_time))
        # print(f"{msg_time}; {log_time}")

        msg = re.search(r"{.+}", log).group()

        # print(f"{msg_time}:::{msg}")

        # convert log to ae
        count = 1
        convert_count = 0

        ae = None
        if check_convert_speed() == True:
            ae = convert(msg, log_time)

        if check_filter(ae) == False:
            kafka_producer = sensor.init_kafka_producer()
            kafka_producer.send(sensor.ae_topic, json.dumps(ae).encode('utf8'))
            # kafka_producer.flush()  # 可能有性能隐患
            print("[*] ae: {}".format(ae))
            time.sleep(0.1)   # 0.05 其实也行
            convert_count = 1

        # sensor log
        sensor.write_sensor_log('convert', 0, count, convert_count)

    except:
        # print(msg)
        traceback.print_exc()

