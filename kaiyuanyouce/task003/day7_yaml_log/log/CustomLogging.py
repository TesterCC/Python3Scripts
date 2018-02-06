# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/6 23:45'

"""
对日志模块logging进行了简单的分享，对于其更强大的功能请自行去学习和实践。例如：

1.用配置文件来控制日志输出
2.实现日志回滚
"""

import logging

LOGGING_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'


class CustomLogging:
    def __init__(self,
                 level=logging.DEBUG,
                 format=LOGGING_FORMAT,
                 datefmt="%a, %d %b %Y %H:%M:%S",
                 filename='custom_log.log',
                 filemode="w"):
        self.level = level
        self.format = format
        self.datefmt = datefmt
        self.filename = filename
        self.filemode = filemode

        # 初始化日志同时输出到console和日志文件  # 可以创建一个config.ini来管理
        logging.basicConfig(level=self.level,
                            format=self.format,
                            datefmt=self.datefmt,
                            filename=self.filename,
                            filemode=self.filemode)

        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，
        # 并将其添加到当前的日志处理对象
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('CustomLogger').addHandler(console)
        self.log = logging.getLogger("CustomLogger")

    def output(self, msg, level=logging.DEBUG):
        if level == logging.DEBUG:
            # 调试信息
            self.log.debug(msg)
        elif level == logging.INFO:
            # 一般的信息
            self.log.info(msg)
        elif level == logging.WARNING:
            # 警告信息
            self.log.warning(msg)
        elif level == logging.ERROR:
            # 错误信息
            self.log.error(msg)
        else:
            # 关键信息
            self.log.critical(msg)

    def set_level(self, level=logging.DEBUG):
        self.log.setLevel(level)


if __name__ == '__main__':
    print("python logging实例 ")

    log = CustomLogging()

    log.output("it's debug msg", level=logging.DEBUG)
    log.output("it's info msg", level=logging.INFO)
    log.output("it's warning msg", level=logging.WARNING)
    log.output("it's error msg", level=logging.ERROR)
    log.output("it's fuck msg", level=logging.CRITICAL)

