# coding=utf-8
"""
DATE:   2021/12/15
AUTHOR: TesterCC
"""

import kafka

kafka_consumer = None
gid = None

topic = 'ae'
server = '127.0.0.1:9092'

# kafka偏移为开始 auto_offset_reset='earliest'
consumer = kafka.KafkaConsumer(topic, auto_offset_reset='earliest', bootstrap_servers=[server])  # group_id=xxx

for msg in consumer:
    print(msg)
    print(int(msg.timestamp / 1000))
    exit()    # 需要更多就注释掉，全打印吧

# python3 kafka_read_earliest.py >> test.log