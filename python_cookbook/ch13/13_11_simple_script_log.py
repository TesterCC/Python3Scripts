import logging


# 13.11 将脚本和程序中的诊断信息写入日志文件。


def main():
    # configure the logging system
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR
    )

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


if __name__ == '__main__':
    main()
