# pcap生成提取程序说明

- gen_pcap.py  生成加密pcap（将发送的数据也存入了pcap）
- extract_pcap.py 解密pcap并从中提取出文件

python3环境，需要安装pycryptodome和scapy。
开发自测在Kali2022.2

## 使用说明

1.生成加密pcap

```
python3 gen_pcap.py -c send_eth.json -f ./file/blue.jpg
-c 生成pcap需要的配置信息
-f 本地要发送出去的文件路径

执行后将在程序当前目录生成 output.pcap 文件。
```

2.从加密pcap中还原文件

```
python3 extract_pcap.py -c recv_eth.json -f output.pcap
-c 解析pcap需要的配置信息
-f 指定需要解析的文件

执行后如有还原出文件，将在当前目录下显示。
```

