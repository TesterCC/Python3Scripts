# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/7 00:08'

"""
http://www.jb51.net/article/114316.htm

作为开发者，我们可以通过以下3中方式来配置logging:
1）使用Python代码显式的创建loggers, handlers和formatters并分别调用它们的配置函数；
2）创建一个日志配置文件，然后使用fileConfig()函数来读取该文件的内容；
3）创建一个包含配置信息的dict，然后把它传递个dictConfig()函数；

需要说明的是，logging.basicConfig()也属于第一种方式，
它只是对loggers, handlers和formatters的配置函数进行了封装。

另外，第二种配置方式相对于第一种配置方式的优点在于，它将配置信息和代码进行了分离，
一方面降低了日志的维护成本，同时还使得非开发人员也能够去很容易地修改日志配置。
"""
import logging.config

# 使用fileConfig()函数来读取配置文件
# 读取日志配置文件内容
logging.config.fileConfig('logging.conf')

# 创建一个日志器logger
logger = logging.getLogger('CustomExample')

# 日志console输出
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

# 日志写入log文件
logging.info("test info level")
logging.warning("test warning level")

# 试着用一个没有在配置文件中定义的logger名称来获取logger
logger = logging.getLogger('TestExample')
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')