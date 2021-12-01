# coding=utf-8
"""
DATE:   2021/12/1
AUTHOR: TesterCC
"""

import json
import os
import sys
import traceback
import time
from datetime import datetime, timedelta

# 根据文件最后修改时间，删除超一个月未更新过的日志
# 1 hour 3600
# 1 day  86400

try:

    main_file = sys.executable if os.name == 'nt' and not sys.executable.endswith('python.exe') else __file__
    config_path = os.path.dirname(main_file) if os.path.sep in main_file else '.'
    config_file = '%s%s%s' % (config_path, os.path.sep, 'log_proxy.json')

    # 读取当前配置文件信息
    with open(config_file) as f:
        config = json.load(f)
    old_log_file_map = config['log_file']

    print("[+] 1.current_log_file_map: {}".format(old_log_file_map))

    # past_time = datetime.now() - timedelta(seconds=3600*6)  # test
    # past_time = datetime.now() - timedelta(days=1)      # dev
    past_time = datetime.now() - timedelta(days=30)  # online

    ago_timestamp = int(time.mktime(past_time.timetuple()))

    for file_path in list(old_log_file_map.keys()):

        try:

            last_modify_time = os.path.getmtime(file_path)
            if last_modify_time < ago_timestamp:
                # print("last_timestamp: {}, ago_timestamp: {}".format(last_modify_time, ago_timestamp))
                # del log file
                os.remove(file_path)  # 有bug，定时没有生效
                # del config
                del old_log_file_map[file_path]
        except:
            traceback.print_exc()
            pass

    # new config
    config['log_file'] = old_log_file_map
    print("[+] 2. {}, new_config: {}".format(datetime.now(), config))
    # write new config
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)

    # 重启 rc.local 若命令执行成功，则返回0
    res = os.system("systemctl restart rc-local")
    if res != 0:
        print("[x] restart log_proxy fail...")

except:
    traceback.print_exc()
    sys.exit()
