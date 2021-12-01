# Deployment

## ext_ftp_log.py

```shell
vi /etc/rc.local

写入：
nohup /usr/bin/python3 /opt/kbdtd_log_proxy/ext_ftp_log.py &
保存后退出

执行：
systemctl restart rc-local
```

## ext_clear_ftp_log.py

```shell
crontab -e

写入（举例 从0开始每3小时执行一次）：
0 */3 * * * nohup /usr/bin/python3 /opt/kbdtd_log_proxy/ext_clear_ftp_log.py >> /opt/kbdtd_log_proxy/nohup_clear_ftp_log.out 2>&1 &
保存后退出

检查配置：
crontab -l

等待脚本按照定时开始执行
```

## crontab执行设置参考

每隔多少分钟，每隔多少小时，每天/每周/每月/每年的crontab设置总结
```shell

每五分钟执行      */5 * * * *
每五小时执行      0 */5 * * *
每天执行          0 0 * * *
每周执行          0 0 * * 0
每月执行          0 0 1 * *
每年执行          0 0 1 1 *
```
