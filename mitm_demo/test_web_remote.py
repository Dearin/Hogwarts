from mitmproxy import http


def request(flow: http.HTTPFlow):
    if 'baidu' in flow.request.url:
        old_url = flow.request.url
        old_url.replace("baidu.com", "ceshiren.com")
