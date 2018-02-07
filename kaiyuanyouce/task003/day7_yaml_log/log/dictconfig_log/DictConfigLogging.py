# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/7 14:13'


"""
http://www.jb51.net/article/114316.htm

作为开发者，我们可以通过以下3中方式来配置logging:
1）使用Python代码显式的创建loggers, handlers和formatters并分别调用它们的配置函数；
2）创建一个日志配置文件，然后使用fileConfig()函数来读取该文件的内容；
3）创建一个包含配置信息的dict，然后把它传递个dictConfig()函数；

Python 3.2中引入的一种新的配置日志记录的方法--用字典来保存logging配置信息。
这相对于上面所讲的基于配置文件来保存logging配置信息的方式来说，功能更加强大，更加灵活，因为我们可把很多的数据转换成字典。
比如，我们可以使用JSON格式的配置文件、YAML格式的配置文件，然后将它们填充到一个配置字典中；
或者，我们也可以用Python代码构建这个配置字典，或者通过socket接收pickled序列化后的配置信息。
总之，你可以使用你的应用程序可以操作的任何方法来构建这个配置字典。

这个例子中，我们将使用YAML格式来完成与上面同样的日志配置。
首先需要安装PyYAML模块： pip install PyYAML
"""

import logging.config
import yaml


with open('logging.yml', 'r') as f_conf:
    dict_conf = yaml.load(f_conf)

logging.config.dictConfig(dict_conf)

logger = logging.getLogger("DictExample")
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')



