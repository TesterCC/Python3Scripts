import requests
from bs4 import BeautifulSoup
import time

# pip install BeautifulSoup4

start_index= 1
end_index = 38

qid = 0

def get_detail_info(page_id):
    # 目标URL
    url = f"https://www.mianshi.icu/case/detail?id={page_id}"

    # 请求头信息
    headers = {
        "GET": f"/case/detail?id={page_id} HTTP/1.1",
        "Host": "www.mianshi.icu",
        # "Cookie": "ssid=",  # 请替换为有效的ssid值
        "Cookie": "",  # 请替换为有效的ssid值
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"macOS\"",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.mianshi.icu/question",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
        "Priority": "u=0, i",
        "Connection": "keep-alive"
    }

    try:
        # 发送请求
        response = requests.get(url, headers=headers, timeout=5)
        print(response.status_code)
        response.raise_for_status()  # 检查HTTP错误状态

        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 检查<title>标签 <h2>
        title_tag = soup.find('h2')
        if not title_tag or not title_tag.string.strip():
            # print("页面标题不存在或为空")  // don't print
            return

        title = title_tag.string.strip()

        global qid
        qid += 1

        output_info = f"{qid}. {title}\npage url: {url}"
        print(output_info)

        # 追加写入文件
        print(f"page id: {page_id}")
        with open('backup/case_with_answer_v2.txt', 'a+') as f:
            f.write(output_info+"\n")

            # 提取所有<p>标签的文本内容，即为免费用户可看的答案
            # print(f"{qid}-{page_id}-答案：")  # debug
            f.write(f"{qid}-{page_id}-答案："+"\n")
            for p in soup.find_all('p'):
                text = p.get_text(strip=True).replace('\xa0', '')  # 去除标签并合并空白; 处理 &nbsp
                # print(text)  # debug
                f.write(f"{text}"+"\n")
            f.write("\n")
            f.write("-" * 30 +"\n")
            f.write("\n")

    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")



def main():
    for page_id in range(start_index, end_index + 1):
        get_detail_info(page_id)
        time.sleep(0.5)

if __name__ == "__main__":
    main()