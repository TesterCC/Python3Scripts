# Socket网络编程

## 客户端/服务端模型

```
server                        client

创建套接字                      创建套接字

绑定（bind）套接字               连接套接字

监听（listen）套接字             发送信息

接收&处理信息
```

# Linux文件描述符 fd

- 进程级的文件描述符表
- 系统级的文件描述符表
- 文件系统的i-Node表


Linux一切皆文件：
- 套接字
- 普通文件
- 目录文件
- 符号链接
- 设备文件
- FIFO

# Linux网络IO模型详解

- 阻塞式IO
- 非阻塞式IO
- IO多路复用：可以在一个线程里处理多个socket
- 信号驱动IO
- 异步IO

## IO多路复用的3种方式
- select: 线性扫描所有监听的文件描述符fd
- poll: 同select，性能有所优化
- epoll: 使用红黑树管理数据结构，性能好

# process

协程原理从入门到精通 9-5