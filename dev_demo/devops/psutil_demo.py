import psutil

# 获取磁盘使用情况
disk_usage = psutil.disk_usage('/')
print(f"Total: {disk_usage.total} bytes")
print(f"Used: {disk_usage.used} bytes")
print(f"Free: {disk_usage.free} bytes")
print(f"Disk Usage: {disk_usage.percent:.2f}%")   # :.2f 保留2位小鼠

# 获取CPU使用情况
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage:.2f}%")

# 获取内存使用情况
memory_usage = psutil.virtual_memory()
print(f"Total: {memory_usage.total} bytes")
print(f"Available: {memory_usage.available} bytes")
print(f"Used: {memory_usage.used} bytes")
print(f"Mem Usage: {memory_usage.percent:.2f}%")
