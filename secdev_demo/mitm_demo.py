# pip install mitmproxy -i https://mirrors.aliyun.com/pypi/simple/
# brew install mitmproxy, 会同时安装 mitmproxy, mitmdump, mitmweb

from mitmproxy import http


def request(flow: http.HTTPFlow):
    # redirect to different host
    if flow.request.pretty_host == "example.com":
        flow.request.host = "mitmproxy.org"
    # answer from proxy
    elif flow.request.path.endswith("/brew"):
        flow.response = http.Response.make(
            418, b"I'm a honeypot",
        )
