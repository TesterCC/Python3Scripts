#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

'''
ps、top命令查找不到进程的解决方案
netstat -anpt发现一个奇怪的连接，但是ps和top命令确查不到此进程，这很可能是因为因为ps和top命令被替换了导致这些进程被过滤掉了。
'''
def get_max_pid():
    out = os.popen('cat /proc/sys/kernel/pid_max')
    content = out.readline().strip('\n')
    if content.isdigit():
        return int(content)

def get_ps_proc_list():
    pid_list = []
    out = os.popen('ps -e --no-header')
    lines = out.readlines()
    for line in lines:
        parts = line.split(' ')
        for part in parts:
            if part == '':
                parts.remove(part)

        pid = int(parts[0])
        pid_list.append(pid)

    return pid_list


def get_ps_lwp_list():
    lwp_list = []
    out = os.popen('ps --no-header -eL o lwp')
    lines = out.readlines()
    for line in lines:
        tid = int(line)
        lwp_list.append(tid)

    return lwp_list


def print_badpid_info(pid):
    out = os.popen('ls -l /proc/%d/exe' % pid)
    lines = out.readlines()
    print(lines)


def main():
    max_pid = get_max_pid()
    print('max pid is %d' % max_pid)
    if max_pid < 0 or max_pid > 50000:
        return

    ps_pid_list = get_ps_proc_list()
    ps_lwp_list = get_ps_lwp_list()

    self_pid = os.getpid()
    for pid in range(2, max_pid):

        #print("handle pid: %d" % pid)

        if pid == self_pid:
            continue

        if pid in ps_pid_list or pid in ps_lwp_list:
            continue

        if not os.path.exists('/proc/' + str(pid)):
            continue

        print("found process not in ps list: %d" % pid)

        print_badpid_info(pid)

if __name__ == '__main__':
    main()