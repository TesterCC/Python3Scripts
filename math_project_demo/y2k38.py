from datetime import datetime, timezone

# 定义 Unix 时间戳
timestamp = -2147483648

# 将时间戳转换为 UTC 时间
dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)

# 输出结果
print(dt.strftime('%Y-%m-%d %H:%M:%S UTC'))
# 1901-12-13 20:45:52 UTC