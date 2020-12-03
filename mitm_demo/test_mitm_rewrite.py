"""
进行数据rewrite的主要思想是：
1- 先接收到接口返回的信息
2- 针对信息作出修改
3- 返回修改的信息
"""
import json

from mitmproxy import http


class XQEvents:
    def response(flow: http.HTTPFlow):
        if "quote.json" in flow.request.url and "x=" in flow.request.url:
            # 把数据转换为json格式
            data = json.loads(flow.response.content)
            print("=======================修改前的数据=======================")
            print(data)

            # 针对数据做一些修改
            data["data"]["items"][0]["quote"]["name"] = data["data"]["items"][0]["quote"]["name"] + "test_rewrite"
            data["data"]["items"][1]["quote"]["name"] += data["data"]["items"][1]["quote"]["name"]
            data["data"]["items"][2]["quote"]["name"] = ""

            print("+++++++++++++++++++++修改后的数据+++++++++++++++++++++++")
            print(data)
            flow.response.text = json.dumps(data)


addons = [XQEvents()]
