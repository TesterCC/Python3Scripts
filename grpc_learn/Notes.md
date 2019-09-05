## learn grpc with python

gRPC + Django:
http://flagzeta.org/blog/using-grpc-with-django/

官方文档：
https://grpc.io/docs/quickstart/python/
https://grpc.io/docs/tutorials/basic/python/

REF：
[https://www.cnblogs.com/yuzhenjie/p/9387677.html](https://www.cnblogs.com/yuzhenjie/p/9387677.html)
[https://www.cnblogs.com/yuzhenjie/p/9398569.html](https://www.cnblogs.com/yuzhenjie/p/9398569.html)



## gRPC 服务开发流程

#### 1.创建.proto文件 （e.g. test.proto）
```
syntax = "proto3";

package order;
message OrderRequest {
  string phone = 1;
  string price = 2;
  map<string, string> request_arg = 3;//便于字段扩展
}

message JSONResponse{
 string rst_string = 1; //统一返回json字符串作处理
 }

service OrderHandler {
// format a list of events.
rpc create_order (OrderRequest) returns (JSONResponse) {}
}
```

#### 2.编译.proto文件 (Python3)
```
cd ~/grpc_learn/

python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ ./*.proto

```
会在 /grpc_learn 目录下生成 order_pb2.py 和 order_pb2_grpc.py 两个文件


#### 3.编写server对应的view文件 views.py   (可能需要在Django环境下做开发)

#### 4.编写server端代码  server.py

#### 5.编写client代码进行测试 client.py

#### 运行
```
python server.py
```


关于gRPC知识推荐：

https://www.zhihu.com/question/299774677/answer/517361296
gRPC在django中如何使用？

```
1、RPC 是远程过程调用RPC（RemoteProcedureCall Protocol）——远程过程调用协议，它是一种通过网络从远程计算机程序上请求服务，而不需要了解底层网络技术的协议。
该协议允许运行于一台计算机的程序调用另一台计算机的子程序，而程序员无需额外地为这个交互作用编程。
RPC协议假定某些传输协议的存在，如TCP或UDP，为通信程序之间携带信息数据。在OSI网络通信模型中，RPC跨越了传输层和应用层。
RPC使得开发包括网络分布式多程序在内的应用程序更加容易。

2、grpc 分服务端，和客户端，服务端提供服务，客户端调用服务。

3、可以在Django代码中用grpc的客户端调用grpc服务端提供的服务，得到数据，然后在Django中使用。
如何使用这些数据？
有两种方法：
a): 在views 中调用grpc 客户端得到数据，进行计算推送到模板中，展示到html中。 
b): Django restful api 中利用grpc 中的数据对外提供api服务。

正好都遇到过
```