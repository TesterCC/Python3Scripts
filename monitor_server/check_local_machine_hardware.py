import wmi

# pip install wmi -i https://pypi.tuna.tsinghua.edu.cn/simple
WMI = wmi.WMI()

# 硬盘信息
for diskinfo in WMI.Win32_DiskDrive():
    if '虚拟' not in diskinfo.Caption:
        Manufacturer = diskinfo.Manufacturer
        SerialNumber = diskinfo.SerialNumber
        Size = diskinfo.Size
        print(f'制造商：{Manufacturer}\n序列号：{SerialNumber}\n硬盘大小：{Size}')

# CPU信息
for cpuinfo in WMI.Win32_Processor():
    Name = cpuinfo.Name
    Manufacturer = cpuinfo.Manufacturer
    ProcessorId = cpuinfo.ProcessorId
    NumberOfCores = cpuinfo.NumberOfCores
    SerialNumber = cpuinfo.SerialNumber
    print(f'名称：{Name}\n制造商：{Manufacturer}\nID号：{ProcessorId}\n序列号：{SerialNumber}\n核心数：{NumberOfCores}')

# 主板信息
for boardinfo in WMI.Win32_BaseBoard():
    Manufacturer = boardinfo.Manufacturer
    Product = boardinfo.Product
    SerialNumber = boardinfo.SerialNumber
    print(f'制造商：{Manufacturer}\n产品号：{Product}\n序列号：{SerialNumber}')

# 网卡信息
for NetworkAdapter in WMI.Win32_NetworkAdapter():
    MACAddress = NetworkAdapter.MACAddress
    if MACAddress:
        Name = NetworkAdapter.Name
        Manufacturer = NetworkAdapter.Manufacturer
        print(f'名称：{Name}\n制造商：{Manufacturer}\nMAC地址：{MACAddress}')

# bios信息
for biosinfo in WMI.Win32_BIOS():
    Name = biosinfo.Name
    Manufacturer = biosinfo.Manufacturer
    SerialNumber = biosinfo.SerialNumber
    print(f'名称：{Name}\n制造商：{Manufacturer}\n序列号：{SerialNumber}')

# 内存信息
for memoryinfo in WMI.Win32_PhysicalMemory():
    Manufacturer = memoryinfo.Manufacturer
    PartNumber = memoryinfo.PartNumber
    SerialNumber = memoryinfo.SerialNumber
    Capacity = memoryinfo.Capacity
    print(f'制造商：{Manufacturer}\n部件号：{PartNumber}\n序列号：{SerialNumber}\n内存大小：{Capacity}')
