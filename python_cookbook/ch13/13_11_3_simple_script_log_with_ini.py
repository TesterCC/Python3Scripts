import logging
import logging.config

# 13.11 将脚本和程序中的诊断信息写入日志文件。
# 改变输出等级，输出日志格式。

# 使用配置文件配置log_config.ini   # P.S. ini编写略有些麻烦，调用方便
def main():
    # configure the logging system
    logging.config.fileConfig('log_config.ini')
    # variables(to make the calls that follow work)
    hostname = "www.test.com"
    item = "examplelog"
    filename = "data.csv"
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning("Feature is deprecated")
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')


'''
用 critical error warning info debug 以降序方式表示不同的严重级别。
basicConfig() 的level参数是一个过滤器。所有级别低于此级别的日志消息都会被忽略掉。
每个 logging 操作的参数是一个消息字符串，后面再跟一个或多个参数。
构造最终的日志消息的时候我们使用了 % 操作符来格式化消息字符串。
'''

if __name__ == '__main__':
    main()
