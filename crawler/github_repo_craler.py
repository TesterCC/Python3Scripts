from github import Github
import sqlite3
import git
import os
import shutil
import time
# from dingtalkchatbot.chatbot import DingtalkChatbot

# Github API token
API_TOKEN = 'ghp_xxxxxxxxxx'

# Github API URL
API_URL = 'https://api.github.com'

# Current user name
USER_NAME = 'adysec'
sorts = ['stars','forks','help-wanted-issues','updated']
keywords = ['ddos','spooling','sqlmap','水泽','fofa','360quake','yaklang','日志审计','堡垒机','Malware','入侵防御','入侵检测','重保','护网','frp','nps','反向代理','横向渗透','应急响应中心','bugcrowd','漏洞','补天','hackerone','defcon','hack','hacker','蜜罐','sms','smsboom','CVE','CNVD','CNNVD','security','cybersecurity','POC','威胁情报','gartner','代码审计','渗透测试','资产测绘','cobaltstrike','漏洞','scan','GPT','网络安全','社工钓鱼','社会工程学','钓鱼','WEB渗透','资产探测','burp','burpsuite','APP小程序渗透','漏洞扫描','漏洞利用','内网渗透','隧道代理','免杀','Windows及linux应急响应','应急响应','网络安全靶场','内网穿透','暴力破解','哥斯拉','冰蝎','蚁剑','未授权访问','host碰撞','EDR','被动扫描','黑盒扫描','漏洞管理','扫描资产','污点分析','xss','csrf','ssrf','RCE','远程代码执行','Mimikatz','子域名收集','红队','甲方安全运营','安全会议','安全管理','安全运营','取证分析','弱口令','后渗透','漏扫','动态爬虫','域前置','域渗透','goby','nessus','反编译','chatGPT','C2','webshell','远控','命令与控制','windows提权','linux提权','提权漏洞','反序列化','域横向','内网信息收集','远控免杀','Gh0st','Nuclei','xscan','vulmap','dirsearch','反弹shell','内存马','bypass','空间测绘','网络空间测绘','ZeroTier','frp','Bitvise','SQL注入','nmap','命令执行','XXE','文件包含','0day','1day','nday','JNDI注入','Mozi','Swagger未授权','struts2远程代码执行','fastjson漏洞','编码绕过','权限绕过','HW','护网','安全会议','安全标准','密码学','密码字典','OWASP','ZAP','AWVS','御剑','逆向工程','IDA','fortify','badusb','winhex','ollydebug','x64dbg','隐写术','yara','appscan','fiddler','7kbscan','masscan','msf','metasploit','xray','52pj','52pojie','吾爱破解','t00ls','process hacker','sysmon','scaner']



# Function to sync a forked repo
def sync_forked_repo(forked_repo):
        # Get forked repo details
        forked_name = forked_repo.name
        forked_url = forked_repo.clone_url

        # Get parent repo details
        parent_name = forked_repo.parent.name
        parent_owner = forked_repo.parent.owner.login
        parent_url = forked_repo.parent.clone_url

        # Add parent repo as remote to local fork
        repo = git.Repo(forked_name)
        remote_name = f"{parent_owner}_{parent_name}"
        remote_url = parent_url.replace(parent_owner, f"{USER_NAME}:")

        try:
                remote = repo.create_remote(remote_name, url=remote_url)
        except:
                remote = repo.remote(remote_name)
                remote.set_url(remote_url)

        # Fetch parent repo changes
        remote.fetch()

        # Merge changes with local fork
        branch = forked_repo.default_branch
        repo.git.checkout('-B', branch, f"{remote_name}/{branch}")
        repo.git.merge(f"{remote_name}/{branch}")

        # Push changes to local fork
        repo.git.push('origin', branch)

# Main function
def main(keyword,sort):
        # Authenticate with Github API using token
        g = Github(API_TOKEN)

        # Get the authenticated user
        user = g.get_user()

        # Auto Fork security repository to the authenticated user's account
        repos = g.search_repositories(query=keyword, sort=sort)
        for repo in repos:
                if not repo.fork:
                        try:
                                user.create_fork(repo)
                                print(f'Forking {repo.full_name} to {user.login}')
                                time.sleep(60)
                        except:
                                pass

        # Get all forked repos of the current user
        user_repos = user.get_repos(type='forks', sort=sort)
        # Sync each forked repo
        for repo in user_repos:
                try:
                        sync_forked_repo(repo)
                except:
                        pass

if __name__ == "__main__":
        for sort in sorts:
                for keyword in keywords:
                        try:
                                main(keyword,sort)
                                time.sleep(60)
                        except:
                                pass
