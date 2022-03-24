# coding=utf-8
"""
DATE:   2022/3/22
AUTHOR: TesterCC
"""
import os
import time
import traceback

"""
运维脚本系列
持续监控4个文件内容情况，不包含关键字就做配置文件更新
"""

# 安装包原始配置文件路径
deploy_config_path = "/opt/package/"

def check_exist(file_path, file_name=""):
    if file_path and file_path:
        return os.path.exists(file_path+file_name)

    if not file_name and file_path:
        return os.path.exists(file_path)

def run_shell(cmd):
    res = os.system(cmd)
    if res != 0:
        return False
    else:
        return True

def check_content(file_path, keyword):

    with open(file_path) as f:
        v_list = f.readlines()
    v_list = [i.strip() for i in v_list]

    # print(keyword)
    # print(v_list)
    # print("-"*100)
    if keyword in v_list:
        return True
    else:
        return False

def monitor_la():
    # # 0.监控 la.conf  -  no need  安装部署后有，升级包不会覆盖
    # if not check_exist("/etc/supervisord.d/la.conf"):
    #     ret = run_shell("cp -a {}la.conf /etc/supervisord.d/".format(deploy_config_path))
    #     if ret:
    #         ret2 = run_shell("supervisorctl reload")
    #         if not ret2:
    #             print("config la.conf failed")

    # 1.监控 /opt/ext_sa/map/access_path.json
    ret1 = check_content('/opt/ext_sa/map/access_path.json', '"/define": {"id":"/define", "name":"事件定级"}')
    if not ret1:
        run_shell("/bin/cp -a {}access_path.json /opt/ext_sa/map/".format(deploy_config_path))
        # run_shell("ps aux | grep python3 | cut -c 9-15 | xargs kill -9")

    # 2.监控 /opt/ext_sa/sa.json
    ret2 = check_content('/opt/ext_sa/sa.json', '"/define": [],')
    if not ret2:
        run_shell("/bin/cp -a {}sa.json /opt/ext_sa/".format(deploy_config_path))
        # run_shell("ps aux | grep python3 | cut -c 9-15 | xargs kill -9")

    # 3.监控 /nginx/conf.d/sa.conf        #  'files = /etc/supervisord.d/*.conf' in supervisor  /etc/supervisord.conf
    ret3 = check_content("/etc/nginx/conf.d/sa.conf", "location /la_api/ {")
    if not ret3:
        run_shell("/bin/cp -a {}sa.conf /etc/nginx/conf.d/".format(deploy_config_path))

    # 4.监控 /etc/supersord.conf
    ret4 = check_content("/etc/supervisord.conf", "files = /etc/supervisord.d/*.conf")
    if not ret4:
        run_shell(r"sed -i '$a\[include]' /etc/supervisord.conf")
        run_shell(r"sed -i '$a\files = /etc/supervisord.d/*.conf' /etc/supervisord.conf")

    print(ret1,ret2,ret3,ret4)
    if (not ret1) or (not ret2) or (not ret3) or (not ret4):
        ret = run_shell("supervisorctl reload")
        if ret:
            print(">>> monitor abnormal config, finish update ...")
    else:
        # print("no error")
        pass


if __name__ == '__main__':

    while True:
        # 考虑到程序稳定性，改为30秒，否则会因为重启间隔太短引发报错，或者和系统升级冲突。

        try:
            monitor_la()
            time.sleep(15)  # 15s
        except:
            traceback.print_exc()
            exit()



