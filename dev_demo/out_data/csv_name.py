import csv
import json

json_file = "./data/11.json"
with open(json_file, 'r', encoding='utf-8') as f:
    out_dict = json.load(f)

print(type(out_dict), len(out_dict))  # 155

print(out_dict[:2])

db_name = [i['name'] for i in out_dict]  # 155

# print(f"len1:{len(db_cve)}")
#
# db_cve = list(set(db_cve))   # no repeat
#
# print(f"len2:{len(db_cve)}")

print("=" * 66)
import_name = ['Adobe Acrobat Reader任意代码执行漏洞',
               'Weblogic远程代码执行漏洞',
               'GoAnywhereMFT反序列化漏洞',
               'Joomla未授权访问漏洞',
               'OpenSSH双重释放漏洞',
               'OpenEMR任意文件读取',
               'Sudoedit权限提升漏洞',
               'pyload代码执行漏洞',
               'linux权限提升漏洞',
               'Kardex Control Center代码执行漏洞',
               'Bonitasoft远程代码执行漏洞',
               'Webmin命令注入',
               'Atlassian Bitbucket命令注入',
               'GitLab命令注入漏洞',
               'Confluence OGNL注入漏洞',
               'Apache Commons Text代码注入漏洞',
               'Django SQL注入漏洞',
               'Apache Shiro认证绕过漏洞',
               'Spring Data MongoDB SpEL表达式注入漏洞',
               'Apache Commons Configuration代码',
               'ADTRAN SmartRG Router安全漏洞',
               'Spring Security认证绕过漏洞',
               'Zimbra任意文件上传漏洞',
               'Jira身份验证绕过漏洞',
               'Elementor远程命令执行漏洞',
               'Apache CouchDB访问控制错误漏洞',
               'WSO2 API Manager远程代码执行漏洞',
               'Spring Framework代码注入漏洞',
               'Spring Cloud Gateway远程代码执行漏洞',
               'CheckPoint 防火墙本地权限提升漏洞-1',
               'CheckPoint 防火墙本地权限提升漏洞-2',
               'CheckPoint 防火墙本地权限提升漏洞-3',
               'CheckPoint 防火墙本地权限提升漏洞-4',
               'Cisco ASA 匿名拒绝服务漏洞-1',
               'Cisco ASA 匿名文件删除漏洞',
               'Cisco ASA 匿名远程代码执行漏洞-1',
               'Cisco ASA 匿名拒绝服务漏洞-2',
               'Cisco ASA 匿名远程信息获取漏洞-2',
               'Cisco ASA 认证后权限提升漏洞-1',
               'Cisco ASA 认证后权限提升漏洞-2',
               'Cisco ACS 匿名远程代码执行漏洞',
               'Cisco RV 授权后拒绝服务漏洞',
               'Cisco RV 认证后权限提升漏洞',
               'Cisco RV 认证后权限提升漏洞',
               'Cisco RV 匿名远程代码执行漏洞',
               'Cisco RV 匿名远程代码执行漏洞',
               'Cisco RV 匿名远程代码执行漏洞',
               'Cisco RV 匿名远程代码执行漏洞',
               'Cisco RV 匿名远程代码执行漏洞',
               'Cisco RV 匿名远程代码执行漏洞',
               'Cisco RV 匿名远程代码执行漏洞',
               'Cisco RV 匿名远程代码执行漏洞',
               'Cisco IOS 匿名远程代码执行漏洞',
               'Cisco Router 匿名远程代码执行漏洞',
               'Cisco Switch 匿名远程代码执行漏洞',
               'Cisco Switch 匿名远程代码执行漏洞',
               'Citrix Gateway 匿名远程代码执行漏洞-1',
               'Citrix Gateway 匿名远程文件读取漏洞-1',
               'Citrix Gateway 本地权限提升漏洞-1',
               'Citrix Gateway 本地权限提升漏洞-2',
               'Cyberoam 本地权限提升漏洞',
               'Cyberoam 匿名远程代码执行漏洞-1',
               'Cyberoam 匿名远程代码执行漏洞-2',
               'D-Link 匿名远程代码执行漏洞',
               'F5 BIG-IP TLS-SSL堆栈漏洞',
               'F5 BIG-IP 匿名拒绝服务漏洞-1',
               'F5 BIG-IP 匿名远程代码执行漏洞-1',
               'F5 BIG-IP 匿名远程代码执行漏洞-2',
               'F5 BIG-IP 匿名远程代码执行漏洞-3',
               'F5 BIG-IP CSRF 提权漏洞',
               'F5 BIG-IP_本地权限提升漏洞',
               'F5 BIG-IP 匿名远程代码执行漏洞-4',
               'F5 BIG-IP 授权后目录遍历漏洞',
               'F5 BIG-IP 本地权限提升漏洞-1',
               'FortiOS 5.x 本地权限提升漏洞-1',
               'FortiOS 5.x 本地权限提升漏洞-2',
               'FortiOS 6.x本地权限提升漏洞',
               'FortiOS LDAP服务器登录凭据获取漏洞',
               'FortiOS SSL VPN用户密码匿名修改漏洞',
               'FortiOS SSL VPN用户双因子认证绕过漏洞',
               'FortiOS 匿名拒绝服务漏洞-1',
               'FortiOS 匿名拒绝服务漏洞-2',
               'FortiOS 匿名拒绝服务漏洞-3',
               'FortiOS 匿名远程信息获取漏洞',
               'FortiOS 匿名远程登录漏洞',
               'FortiOS 匿名远程代码执行漏洞',
               'FortiOS 认证后本地拒绝服务漏洞',
               'HuaWei 匿名远程代码执行漏洞',
               'Juniper JunOS信息泄露漏洞-1',
               'Juniper JunOS信息泄露漏洞-2',
               'Juniper JunOS信息泄露漏洞-3',
               'Juniper JunOS本地权限提升漏洞-1',
               'Juniper JunOS本地权限提升漏洞-2',
               'Juniper JunOS本地权限提升漏洞-3',
               'Juniper Pulse Secure匿名远程信息获取漏洞-1',
               'Juniper Pulse Secure本地权限提升漏洞-1',
               'Juniper Pulse Secure本地权限提升漏洞-2',
               'Juniper Pulse Secure本地权限提升漏洞-3',
               'Juniper Pulse Secure本地权限提升漏洞-4',
               'Juniper Pulse Secure本地权限提升漏洞-5',
               'Juniper Pulse Secure认证后文件读取漏洞',
               'Juniper SRX 匿名远程代码执行漏洞-1',
               'Juniper SRX 匿名远程代码执行漏洞-2',
               'Juniper SRX 本地权限提升漏洞',
               'Juniper SRX 本地权限提升漏洞',
               'Juniper 匿名远程代码执行漏洞',
               'Juniper SSG VPN加密信息匿名获取漏洞',
               'Juniper SSG 匿名远程登录漏洞',
               'Mikrotik RouterOS匿名代码执行漏洞-1',
               'Mikrotik RouterOS匿名代码执行漏洞-2',
               'Mikrotik RouterOS匿名拒绝服务漏洞-1',
               'Mikrotik RouterOS匿名拒绝服务漏洞-2',
               'Mikrotik RouterOS匿名拒绝服务漏洞-3',
               'Mikrotik RouterOS匿名拒绝服务漏洞-4',
               'Mikrotik RouterOS匿名远程信息获取漏洞-1',
               'Netgear Firewall 匿名远程代码执行漏洞',
               'Netgear Firewall 本地权限提升漏洞',
               'Netgear 匿名远程代码执行漏洞',
               'Netgear router 认证绕过漏洞-1',
               'Netgear router 认证绕过漏洞-2',
               'Netgear router 认证绕过漏洞-3',
               'Netgear router 认证绕过漏洞-4',
               'Netgear router 认证绕过漏洞-5',
               'Netgear router 修改密码漏洞',
               'Netgear router 本地权限提升漏洞',
               'Netgear router 匿名拒绝服务漏洞',
               'Netgear switch 匿名任意上传漏洞',
               'Netgear router 信息泄露漏洞',
               'Netgear router 匿名远程代码执行漏洞-1',
               'Netgear router 匿名远程代码执行漏洞-2',
               'Netgear router 匿名远程代码执行漏洞-3',
               'Netgear router 匿名远程代码执行漏洞-4',
               'Netgear router 匿名远程代码执行漏洞-5',
               'Netgear router 匿名远程代码执行漏洞-6',
               'Palo Alto 匿名拒绝服务漏洞-1',
               'Palo Alto 匿名远程代码执行漏洞-1',
               'Palo Alto 匿名远程代码执行漏洞-2',
               'Palo Alto 本地权限提升漏洞-1',
               'Palo Alto 本地权限提升漏洞-2',
               'PfSense CSRF本地权限提升漏洞',
               'PfSense 本地权限提升漏洞-1',
               'PfSense 本地权限提升漏洞-2',
               'PfSense 本地权限提升漏洞-3',
               'Pfsense 本地权限提升漏洞-4',
               'Pfsense 本地权限提升漏洞-5',
               'Pfsense 匿名远程代码执行漏洞',
               'Sonicwall SRA匿名代码执行漏洞-1',
               'Sonicwall SRA SMA匿名代码执行漏洞',
               'Sonicwall SRA授权后拒绝服务漏洞',
               'Sonicwall SRA SMA匿名拒绝服务漏洞',
               'Sonicwall SRA本地权限提升漏洞-1',
               'Sonicwall SRA本地权限提升漏洞-2',
               'Sonicwall SRA本地权限提升漏洞-3',
               'Sonicwall SRA本地权限提升漏洞-4',
               'Sonicwall SRA本地权限提升漏洞-5',
               'Sonicwall SRA SMA本地权限提升漏洞-1',
               'Sonicwall SRA SMA本地权限提升漏洞-2',
               'Sonicwall SRA SMA匿名管理员密码获取漏洞',
               'Sonicwall SRA SMA匿名管理员密码重置漏洞',
               'Sophos XG匿名远程代码执行漏洞-1',
               'Sophos XG匿名远程代码执行漏洞-2',
               'Sophos XG匿名远程代码执行漏洞-3',
               'Sophos XG匿名远程代码执行漏洞-4',
               'Sophos XG授权后SQL注入漏洞',
               'Sophos XG授权后命令执行漏洞',
               'Sophos XG本地权限提升漏洞',
               'Sophos XG路径遍历漏洞',
               'SpamTitan-Gateway 匿名远程代码执行漏洞',
               'SpamTitan-Gateway 本地权限提升漏洞-1',
               'SpamTitan-Gateway 任意文件读取漏洞',
               'SpamTitan-Gateway 本地权限提升漏洞-2',
               'SpamTitan-Gateway 本地权限提升漏洞-3',
               'SpamTitan-Gateway 本地权限提升漏洞-4',
               'Tenda 本地权限提升漏洞',
               'Tp-Link 匿名远程代码执行漏洞',
               'WatchGuard 本地权限提升漏洞-1',
               'ZeroShell 匿名远程代码执行漏洞-1',
               'ZeroShell 匿名远程代码执行漏洞-2',
               'Zyxel 硬编码后门漏洞']

# 在db_cve，不在import_cve
print(f"[D] total db names: {len(db_name)}")

repeat_name = []
no_repeat_name = []

for j in db_name:

    if j in import_name:
        repeat_name.append(j)
    else:
        no_repeat_name.append(j)

print(f"[D] repeat: {len(repeat_name)}")

print(f"[D] no repeat: {len(no_repeat_name)}")
print(no_repeat_name)

print("-" * 66)
print("[I] write csv ...")

csv_header = ['漏洞名称',
              '适用版本',
              '影响范围',
              '利用效果',
              '应用分类',
              '运行环境',
              '漏洞分类',
              'CVE编号',
              '利用条件',
              '修补时间',
              '开发平台',
              '负面影响']

rows = []


def get_vul_type(name: str):
    ret = name
    if "代码执行" in name:
        ret = "代码执行"
    if "代码注入" in name:
        ret = "代码执行"
    if "CSRF" in name:
        ret = "代码执行"

    if "提权" in name:
        ret = "本地提权"
    if "越权" in name:
        ret = "本地提权"
    if "权限提升" in name:
        ret = "本地提权"

    if "远程提权" in name:
        ret = "远程提权"
    if "SQL" in name:
        ret = "SQL注入"
    if "命令注入" in name:
        ret = "命令注入"
    if "命令执行" in name:
        ret = "命令注入"

    if "信息泄露" in name:
        ret = "信息泄露"
    if "路径遍历" in name:
        ret = "信息泄露"
    if "文件读取" in name:
        ret = "信息泄露"

    if "信息远程获取" in name:
        ret = "信息泄露"

    if "信息获取" in name:
        ret = "信息泄露"

    if "认证绕过" in name:
        ret = "认证绕过"

    if "验证绕过" in name:
        ret = "认证绕过"

    if "拒绝服务" in name:
        ret = "拒绝服务"

    return ret


def handle_cve_number(cve_number: str):
    if not cve_number:
        cve_number = ""
    if "自主发现" in cve_number:
        cve_number = "1Day"
    if "no cve" in cve_number:
        cve_number = "1Day"
    return cve_number


def get_app_type(name: str):
    ret = name
    if "Cyberoam" in name:
        ret = "防火墙"
    if "PfSense" in name:
        ret = "防火墙"
    if "Forti" in name:
        ret = "防火墙"
    if "Palo Alto" in name:
        ret = "防火墙"
    if "Sonicwall SRA" in name:
        ret = "防火墙"
    if "Sophos XG" in name:
        ret = "防火墙"
    if "WatchGuard" in name:
        ret = "防火墙"
    if "防火墙" in name:
        ret = "防火墙"

    if "Juniper" in name:
        ret = "路由器"
    if "Router" in name:
        ret = "路由器"
    if "Cisco" in name:
        ret = "路由器"

    if "SpamTitan-Gateway" in name:
        ret = "交换机"

    if "Windows" in name:
        ret = "操作系统"
    return ret


for i in out_dict:
    if i.get('name') in no_repeat_name:
        td = dict()
        td['漏洞名称'] = i.get('name')
        td['适用版本'] = ""  # 不填,留空
        td['影响范围'] = i.get('version')
        td['利用效果'] = i.get('useage')
        td['应用分类'] = get_app_type(i.get('name'))  # 人工：路由器 交换机 防火墙  操作系统 应用软件
        td['运行环境'] = i.get('operating')
        td['漏洞分类'] = get_vul_type(i.get('name'))  # 写个自动判断的函数，减少人工分类工作量
        td['CVE编号'] = handle_cve_number(i.get('cve_number'))  # 写个自动判断的函数，减少人工分类工作量
        td['利用条件'] = i.get('func')
        td['修补时间'] = i.get('repair_time')
        td['开发平台'] = i.get('development')
        td['负面影响'] = "" if i.get('negative') == "无" else i.get('negative')

        rows.append(td)

print(f"no repeat data length: {len(rows)}")

# dict write
with open('filter_db.csv', 'w', newline='') as f:
    f_csv = csv.DictWriter(f, csv_header)
    f_csv.writeheader()
    f_csv.writerows(rows)
