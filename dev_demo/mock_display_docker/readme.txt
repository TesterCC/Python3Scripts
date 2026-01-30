基于已有tree.json打入数据操作步骤：
1)清空已有数据库: python3 init_db.py
2)将已写好的tree.json放到系统的 /opt/i_cm/controlled/tree.json 这个位置。
3)确保配置中心多层管控端IP和端口和tree.json中根节点IP和端口一致。
4)根据tree.json写入远程控制设备信息到数据库中：python3 insert_docker_node_data.py


注意: tree.json中的node_heartbeat_time 13位时间戳要注意尽量和系统时间一致，不然导入判断时会把设备标为离线。