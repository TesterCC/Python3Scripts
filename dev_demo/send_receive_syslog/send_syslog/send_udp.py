import os
import json
import time
import socket
import traceback


# 18000/30 = 600s
# 18000/100 = 180s
eps = 100


addr = ('10.0.0.201', 514)



root_path = os.path.dirname(__file__)
send_json_file = '%s/send.json' % root_path
syslog_log_file = '%s/syslog.log' % root_path

try:
    with open(send_json_file) as f:
        config = json.load(f)
except:
    config = {'start':0}
    
with open(syslog_log_file) as f:
    syslog_list = f.readlines()

config = {'start':0}

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   # udp

# tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   # tcp
# tcp_socket.connect(addr)
while True:
    try:
        count = 0
        save_time = time.time()
        for syslog in syslog_list[config['start']:]:
            date = time.strftime('%B %d %H:%M:%S', time.localtime())
            syslog = syslog.replace('{{date}}', date)
            udp_socket.sendto(syslog.encode('utf8'),addr)
            count += 1
            time.sleep(1/eps)
            if time.time() > save_time + 1:
                save_time = time.time()
                config['start'] = count
                with open(send_json_file, 'w') as f:
                    json.dump(config, f, indent=4)

        config['start'] = 0
        with open(send_json_file, 'w') as f:
            json.dump(config, f, indent=4)

    except:
        traceback.print_exc()
        time.sleep(5)
        tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_DREAM)   # UDP
        # tcp_socket.connect(addr)

    break

'''
template = '<188> {{date}} h3c_ips %%10IPS/4/IPS_IPV4_INTERZONE: AttackID(1089)={{id}}; Protocol(1001)=TCP; SrcIPAddr(1003)={{src}}; SrcPort(1004)={{sport}}; DstIPAddr(1007)={{dst}}; DstPort(1008)={{dport}}; \n'
'''

