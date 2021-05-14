# coding=utf8
# yum -y install epel-release
# yum -y install gcc
# yum -y install python36-devel
# pip3 install psutil

# from dzls: 是以前写的一个监控脚本，可以根据需求自己修改  e.g. suspicious process analysis

import psutil
import time


monitor_interval = 1
log_file = 'network_monitor.log'


'''
psutil.pids() # 所有进程ID
p = psutil.Process(18320) # 获取指定进程
p = psutil.Process() # 获取当前进程
p.name()        # 进程名
p.exe()         # 进程路径
p.cwd()         # 进程工作目录
p.cmdline()     # 进程启动命令行
p.ppid()        # 父进程
p.children()    # 子进程列表
p.status()      # 进程状态
p.username()    # 进程用户名
p.create_time() # 进程创建时间
p.terminal()    # 进程终端
p.cpu_times()   # 进程使用的CPU时间
p.cpu_percent(1)# cpu占用率，括号内为统计时间
p.memory_info() # 进程使用的内存
p.open_files()  # 进程打开的文件
p.connections() # 进程相关网络连接
p.num_threads() # 进程的线程数量
p.threads()     # 所有线程信息
p.environ()     # 进程环境变量
p.terminate()   # 结束进程
'''


def write_log(log):
    global log_file
    
    file = open(log_file, 'a')
    file.write(log + '\n')
    file.close()


last_status = {}
while True:
    status = {}
    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
            conn_list = p.connections()
            for conn in conn_list:
                if conn.raddr == ():
                    continue

                src = conn.laddr[0]
                sport = conn.laddr[1]
                dst = conn.raddr[0]
                dport = conn.raddr[1]
                key = '%s:%s > %s:%s' % (src, sport, dst, dport)

                # process, addr, cmd, username, parent_process
                info = '%s, %s, %s, %s, %s' % (p.username(), key, p.exe(), ' '.join(p.cmdline()), psutil.Process(p.ppid()).exe())
                status[key] = info

        except Exception as e:
            pass

    for key in status:
        if key not in last_status:
            strftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            log = '[%s] ESTABLISHED, %s' % (strftime, status[key])
            write_log(log)

    for key in last_status:
        if key not in status:
            strftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            log = '[%s] CLOSED, %s' % (strftime, last_status[key])
            #write_log(log)

    last_status = status
    time.sleep(monitor_interval)

